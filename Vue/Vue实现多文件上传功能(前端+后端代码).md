**本人业余前端开发，因为公司(很坑)觉得我很牛逼，所以让我前后端一起玩，无奈的我只能磕磕碰碰的研究起了vue**。

开发项目的时候，用到文件上传的功能很常见，包括单文件上传和多文件上传，上传各种类型的文件。在vue里面要实现多文件上传功能，还是很方便的。

本文就一起来学习一下，如何把多文件上传功能封装成一个组件，后面需要使用的时候，直接两三行代码就能搞定。

### 1、前端代码

首先我们先看前端，如何把它封装成一个组件。我们在调用它的时候，可能需要从外部传入一些参数给它，所以我们需要定义一些传入参数。这些参数我们可以放到props里面

```js
export default {
  props: {
    // 值
    value: [String, Object, Array],
    // 大小限制(MB)
    fileSize: {
      type: Number,
      default: 2,
    },
    // 文件类型, 例如['png', 'jpg', 'jpeg']
    fileType: {
      type: Array,
      default: () => [".jpg", ".jpeg", ".png", ".doc", ".xls", ".xlsx", ".ppt", ".txt", ".pdf"],
    },
    // 是否显示提示
    isShowTip: {
      type: Boolean,
      default: true
    },
    // 单据id
    billId: {
      type: Number,
      require: true
    },
    // 单据类型
    billType: {
      type: Number,
      required: true
    }
  }
}
```
上面定义了一些文件大小，文件类型等，如果没有传入，则为默认值。单据类型和单据id是必须要传入的，这里可以依照实际开发需要进行定义即可。

文件上传组件，我们可以使用element的`el-upload`，在页面引入，我们点击后一般唤醒的是一个文件上传弹窗，可以使用`el-dialog`标签包围。完整代码如下
```js
<template>
  <el-dialog title="附件上传" :visible.sync="visible" width="800px" :close-on-click-modal="false" @close="cancel">
    <div class="upload-file">
      <el-upload
        :action="action"
        :before-upload="handleBeforeUpload"
        :file-list="fileList"
        :limit="3"
        multiple
        :accept="accept"
        :on-error="handleUploadError"
        :on-exceed="handleExceed"
        :on-success="handleUploadSuccess"
        :on-change="handChange"
        :http-request="httpRequest"
        :show-file-list="true"
        :auto-upload="false"
        class="upload-file-uploader"
        ref="upload"
      >
        <!-- 上传按钮 -->
        <el-button slot="trigger" size="mini" type="primary">选取文件</el-button>
        <el-button style="margin-left: 10px;" :disabled="fileList.length < 1" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
        <!-- 上传提示 -->
        <div class="el-upload__tip" slot="tip" v-if="showTip">
          请上传
          <template v-if="fileSize"> 大小不超过 <b style="color: #f56c6c">{{ fileSize }}MB</b> </template>
          <template v-if="fileType"> 格式为 <b style="color: #f56c6c">{{ fileType.join("/") }}</b> </template>
          的文件
        </div>
      </el-upload>

      <!-- 文件列表 -->
      <transition-group class="upload-file-list el-upload-list el-upload-list--text" name="el-fade-in-linear" tag="ul">
        <li :key="file.uid" class="el-upload-list__item ele-upload-list__item-content" v-for="(file, index) in list">
          <el-link :href="file.url" :underline="false" target="_blank">
            <span class="el-icon-document"> {{ getFileName(file.name) }} </span>
          </el-link>
          <div class="ele-upload-list__item-content-action">
            <el-link :underline="false" @click="handleDelete(index)" type="danger">删除</el-link>
          </div>
        </li>
      </transition-group>
    </div>
  </el-dialog>
</template>
```
上面用到的几个变量，我们需要在data里面定义
```js
data() {
    return {
      // 已选择文件列表
      fileList: [],
      // 是否显示文件上传弹窗
      visible: false,
      // 可上传的文件类型
      accept: '',
      action: 'action'
    };
  },
```
`accept`字段需要在页面创建后，通过传入或默认的`fileType`字段进行拼接得到
```js
created() {
    this.fileList = this.list
    // 拼接
    this.fileType.forEach(el => {
      this.accept += el
      this.accept += ','
    })
    this.fileType.slice(0, this.fileList.length - 2)
  },
```
接下来就是文件上传相关的方法，这里我们使用选择文件后手动上传的方式，请看下面的代码
```js
<el-upload
        :action="action"  // 手动上传，这个参数没有用，但因为是必填的，所以随便填一个值就行
        :before-upload="handleBeforeUpload"  // 文件上传之前进行的操作
        :file-list="fileList"   // 已选择文件列表
        :limit="3"   // 一次最多上传几个文件
        multiple   // 可以多选
        :accept="accept"   // 可以上传的文件类型
        :on-error="handleUploadError"   // 上传出错时调用
        :on-exceed="handleExceed"   // 文件数量超过限制时调用
        :on-success="handleUploadSuccess"   // 上传成功时调用
        :on-change="handChange"   // 文件发生变化时调用
        :http-request="httpRequest"   // 自定义的文件上传方法，我们手动点击上传按钮后会调用
        :show-file-list="true"   // 是否显示文件列表
        :auto-upload="false"   // 关闭自动上传
        class="upload-file-uploader" 
        ref="upload"
      >

<!-- 上传按钮 -->
<el-button slot="trigger" size="mini" type="primary">选取文件</el-button>
<el-button style="margin-left: 10px;" :disabled="fileList.length < 1" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
```
点击上传到服务器后，就触发`submitUpload`调用我们自定义的方法。

注意这里选取文件的按钮需要加上`slot="trigger"`属性，不然点击上传到服务器按钮后，也会触发选择文件弹框。

接下来看相关的方法

```js
methods: {
	// 外部调用这个方法，显示文件上传弹窗
    show() {
      this.visible = true
    },
    // 上传前校检格式和大小
    handleBeforeUpload(file) {
      // 校检文件类型
      if (this.fileType) {
        let fileExtension = "";
        if (file.name.lastIndexOf(".") > -1) {
          fileExtension = file.name.slice(file.name.lastIndexOf("."));
        }
        const isTypeOk = this.fileType.some((type) => {
          if (file.type.indexOf(type) > -1) return true;
          if (fileExtension && fileExtension.indexOf(type) > -1) return true;
          return false;
        });
        if (!isTypeOk) {
          this.$message.error(`文件格式不正确, 请上传${this.fileType.join("/")}格式文件!`);
          return false;
        }
      }
      // 校检文件大小
      if (this.fileSize) {
        const isLt = file.size / 1024 / 1024 < this.fileSize;
        if (!isLt) {
          this.$message.error(`上传文件大小不能超过 ${this.fileSize} MB!`);
          return false;
        }
      }
      return true;
    },
    // 文件个数超出
    handleExceed() {
      this.$message.error(`只允许上传3个文件`);
    },
    // 上传失败
    handleUploadError(err) {
      this.$message.error("上传失败, 请重试");
    },
    // 上传成功回调
    handleUploadSuccess(res, file) {
      this.$message.success("上传成功");
      this.cancel()
    },
    /** 文件状态改变时调用 */
    handChange(file, fileList) {
      this.fileList = fileList
    },
    // 删除文件
    handleDelete(index) {
      this.fileList.splice(index, 1);
    },
    // 获取文件名称
    getFileName(name) {
      if (name.lastIndexOf("/") > -1) {
        return name.slice(name.lastIndexOf("/") + 1).toLowerCase();
      } else {
        return "";
      }
    },
    /** 手动提交上传 */
    submitUpload() {
      if (this.fileList.length <= 0) {
        return false
      }
      this.$refs.upload.submit()
    },
    /** 关闭上传弹框 */
    cancel() {
      this.fileList = []
      this.visible = false
    },
    /** 调用接口上传 */
    httpRequest(param) {
      const formData = new FormData()
      formData.append("billId", this.billId)
      formData.append("formType", this.billType)
      formData.append('file', param.file)
      uploadFormFile(formData).then(res => {
        if(res.code === 200){
          // 自定义上传时，需自己执行成功回调函数
          param.onSuccess()
          this.$refs.upload.clearFiles()
          this.msgSuccess("上传成功")
          // 回调方法，文件上传成功后，会调用`input`指定的方法，在调用方定义
          this.$emit("input", res.data)
        }
      }).catch((err)=>{})
    }
  }
```
其他方法都还好，主要看看这个`httpRequest`方法，如果直接使用url的方式进行调用，会出现跨域问题，你需要把token放到请求头里。我这里是通过封装后的api接口进行调用的，已经做了全局的token验证，所以只需要把相关的参数带上即可。

使用`formData `带上需要的参数。上传成功后，使用`this.$emit("input", res.data)`执行上传成功后的逻辑。

这就封装好了一个文件上传的组件，接下来看看怎么使用。

### 2、使用组件
在使用的页面，首先需要引入组件
```js
import FileUpload from '@/components/FileUpload'
```
然后再页面内进行调用

```js
<file-upload ref="fileUploadDialog" :billId="this.form.noticeId" :billType="10" @input="getAttachList"></file-upload>
```
`billId`和`billType`是我们动态传入的参数，其他的参数使用默认值，`getAttachList`方法在文件上传成功后执行。

我们需要一个按钮唤醒文件上传框
```js
<el-button
       type="primary"
       plain
       icon="el-icon-plus"
       size="mini"
       @click="handleAdd"
       :disabled="notEdit"
     >上传</el-button>
```
定义`hangAdd`方法，直接调用组件里定义的`show`方法即可
```js
handleAdd() {
   this.$refs.fileUploadDialog.show()
 },
```
然后定义文件上传成功后的方法，获取已上传文件列表即可。
```js
 getAttachList() {
   this.loading = true
   this.attachQuery.billId = this.form.noticeId
   this.attachQuery.billType = 10
   listAttachment(this.attachQuery).then(response => {
     this.attachList = response.rows
     this.attachList.forEach(el => {
       // 转为kb，取小数点后2位
       el.fileSize = parseFloat(el.fileSize / 1024).toFixed(2)
     })
     this.attachTotal = response.total
     this.loading = false
   }).catch(() => {})
 },
```
到这里前端代码就大功告成了。

![在这里插入图片描述](Vue实现多文件上传功能(前端+后端代码).assets/57c39a1734974d42a8d4c9771e0e2562.png)
### 3、后端代码
我这里选择上传图片到阿里云服务器，上传到哪里不重要
```java
/**
 * 单据附件上传
 * @param billId 单据id
 * @param formType 单据类型
 * @param file 上传的文件
 * @return
 * @throws Exception
 */
@PostMapping("/form/attachment/upload")
public AjaxResult uploadFormFile(@RequestParam(value = "billId") Long billId,
                             @RequestParam(value = "formType") Integer formType,
                             @RequestParam("file") MultipartFile[] file) throws Exception {
    try {
        // 文件上传后的路径
        List<String> pathList = new ArrayList<>();

        for (MultipartFile f : file) {
            if (!f.isEmpty()) {
                // 调用接口上传照片
                AjaxResult result = uploadService.uploadFormFile(f, billId, formType);
                if (!result.get("code").toString().equals("200")) {
                    return AjaxResult.error("上传文件异常，请联系管理员");
                }
                pathList.add(result.get("data").toString());
            }
        }

        // 返回图片路径
        return AjaxResult.success(pathList);
    } catch (Exception e) {
        return AjaxResult.error(e.getMessage());
    }
}
```
这里我们使用一个`MultipartFile`数组接受文件，然后调用方法判断文件的一些属性上传文件即可，具体的上传方法这里就不贴了，各有不同，具体情况具体分析。

到这里，本文就ok了。关于MIME 类型列表，可以[点击这里](https://www.w3school.com.cn/media/media_mimeref.asp)查看。如果过程中遇到什么问题，可以在下方留言，我会回复的。

##### 觉得好的可以帮忙点个赞啊，也可以关注我的公众号【秃头哥编程】