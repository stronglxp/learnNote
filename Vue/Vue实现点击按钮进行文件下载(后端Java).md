最近项目中需要实现点击按钮下载文件的需求，前端用的vue，因为文件是各种类型的，比如图片、pdf、word之类的。这里后端是可以返回文件的地址给前端的，但我看了下网上各种五花八门的答案，感觉都不是我想要的。

因为不确定文件是哪种类型的，所以我们在保存文件到数据库的时候，应该把文件的`Content-Type`一起存入，这样从数据库取出返回前端的时候，带上`Content-Type`标识是哪种类型的文件，前端解析即可。

### 1、后端代码

这里我先写后端的接口，考虑一下后端需要什么东西。因为文件信息已经提前存入数据库，所以我们只需要传入主键id就可以拿到文件的信息。确定参数后，就需要确定一下返回值类型。这里可以使用`ResponseEntity`返回。`ResponseEntity`可以一次返回多个信息，包括状态码，响应头信息，响应内容等。

话不多说，看代码。

```java
/**
 * 下载附件
 * @param attachmentId
 * @return
 */
public ResponseEntity<byte[]> download(Long attachmentId) {
    // 查询附件是否存在
    SysAttachment sysAttachment = sysAttachmentMapper.selectSysAttachmentById(attachmentId);
    if (StringUtils.isNull(sysAttachment)) {
        return null;
    }

    ByteArrayOutputStream bos = null;
    InputStream ins = null;
    try {
        String fileName = sysAttachment.getOrgFileName();
        String ossFileName = sysAttachment.getUrl();
        bos = new ByteArrayOutputStream();
        ins = OssUtils.getInstance().getObject(ossFileName).getObjectContent();
        // 取流中的数据
        int len = 0;
        byte[] buf = new byte[256];
        while ((len = ins.read(buf, 0, 256)) > -1) {
            bos.write(buf, 0, len);
        }

        // 防止中文乱码
        fileName = URLEncoder.encode(fileName, "utf-8");
        // 设置响应头
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Disposition", "attachment;filename=" + fileName);
        headers.add("Content-Type", sysAttachment.getContentType());
        // 设置响应吗
        HttpStatus statusCode = HttpStatus.OK;
        ResponseEntity<byte[]> response = new ResponseEntity<byte[]>(bos.toByteArray(), headers, statusCode);
        return response;
    } catch (Exception e) {
        throw new CustomException("下载失败");
    } finally {
        try {
            if (ins != null) {
                ins.close();
            }
            if (bos != null) {
                bos.close();
            }
        } catch (Exception e) {
            throw new CustomException("下载失败");
        }
    }
}
```

这里我们从数据库拿出文件的url后，再通过阿里云oss拿到文件的输入流，接着把文件输出为二进制，封装到`ResponseEntity`中，并把文件的类型设置到`Content-Type`中，同时为了防止文件名带有中文名乱码，设置`utf-8`编码，至此后端接口完成。

通过上面的信息，我们在数据库保存文件信息时，至少应该保存下面几个字段：文件的url（一般在上传到oss后会给你一个）、文件的类型、原始文件名、文件大小等。

### 2、前端代码

有了后端接口，接下来就是前端了。这里可以把文件下载的方法封装成一个通用方法全局挂载，之后需要使用的地方直接使用即可。

我们需要标识不同的文件，所以我们需要一个键值对表示不同的文件。

```js
const mimeMap = {
  xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  xls: 'application/vnd.ms-excel',
  zip: 'application/zip',
  jpg: 'image/jpg',
  jpeg: 'image/jpeg',
  png: 'image/png',
  doc: 'application/msword',
  docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  ppt: 'application/vnd.ms-powerpoint',
  txt: 'text/plain',
  pdf: 'application/pdf'
}
```

有需要的可以继续补充。接下来自然就是发请求了，这里的返回类型可以设置为`blob`，使用axios直接发送

```js
/**
 * 下载附件
 * @param path 接口地址
 * @param param  请求参数
 */
export function downloadAttachment(path, param) {
  var url = baseUrl + path + param
  axios({
    method: 'get',
    url: url,
    responseType: 'blob',
    headers: { 'Authorization': getToken() }
  }).then(res => {
    resolveBlob(res, res.data.type)
  })
}
```

接口地址和请求参数从外部传入。同时需要携带token，不然会跨域访问。拿到后端返回的数据后，需要解析二进制文件，这里定义`resolveBlob`方法，该方法有两个参数，返回对象和文件的类型，文件的类型，我们在后端已经放入`Content-Type`中了，这里直接取。

```js
/**
 * 解析blob响应内容并下载
 * @param {*} res blob响应内容
 * @param {String} mimeType MIME类型
 */
export function resolveBlob(res, mimeType) {
  const aLink = document.createElement('a')
  var blob = new Blob([res.data], { type: mimeType })
  // 从response的headers中获取filename, 后端response.setHeader("Content-disposition", "attachment; filename=xxxx.docx") 设置的文件名;
  var patt = new RegExp('filename=([^;]+\\.[^\\.;]+);*')
  var contentDisposition = decodeURI(res.headers['content-disposition'])
  var result = patt.exec(contentDisposition)
  var fileName = result[1]
  fileName = fileName.replace(/\"/g, '')
  aLink.href = URL.createObjectURL(blob)
  aLink.setAttribute('download', fileName) // 设置下载文件名称
  document.body.appendChild(aLink)
  aLink.click()
  document.body.removeChild(aLink);
}
```

这代码不用多解释了吧，前端大佬们自然看得懂。OK了啊，到这里前后端代码都完成了。

### 3、使用

使用那就更简单啦。先挂载到全局

```js
import { downloadAttachment } from "@/utils/download"
Vue.prototype.downloadAttac = downloadAttachment
```

在使用的地方直接调用即可

```js
<el-button
    type="text"
    icon="el-icon-download"
    size="mini"
    @click="downloadAttachRow(scope.row.attachmentId)"
    ></el-button>

/** 下载附件 */
downloadAttachRow(attachId) {
    this.$confirm('是否确认下载该文件?', "警告", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
    }).then(() => {
        this.downloadAttac('/system/attachment/download/', attachId)
    }).then(() => {
        this.msgSuccess("下载成功")
    }).catch(() => {})
}
```

到此结束。如果过程中遇到什么问题，可以在下方留言，我会回复的。

##### 觉得好的可以帮忙点个赞啊，也可以关注我的公众号【秃头哥编程】

