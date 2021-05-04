## java操作excel

### 1、POI和EasyExcel

> POI

api参考：https://poi.apache.org/apidocs/5.0/index.html

[Apache](https://baike.baidu.com/item/Apache/6265) POI [1] 是用[Java](https://baike.baidu.com/item/Java/85979)编写的免费开源的跨平台的 Java API，Apache POI提供API给Java程式对[Microsoft Office](https://baike.baidu.com/item/Microsoft Office)格式档案读和写的功能。POI为“Poor Obfuscation Implementation”的首字母缩写，意为“简洁版的模糊实现”。

HSSF  － 提供读写Microsoft Excel XLS格式档案的功能。（XLS即为.xls后缀的excel，最多65536行）
XSSF  － 提供读写Microsoft Excel OOXML XLSX格式档案的功能。（XLSX即为.xlsx后缀的excel，行数没有上限）
HWPF  － 提供读写Microsoft Word DOC格式档案的功能。
HSLF  － 提供读写Microsoft PowerPoint格式档案的功能。
HDGF  － 提供读Microsoft Visio格式档案的功能。
HPBF  － 提供读Microsoft Publisher格式档案的功能。
HSMF  － 提供读Microsoft Outlook格式档案的功能。

> EasyExcel

Java解析、生成Excel比较有名的框架有Apache poi、jxl。但他们都存在一个严重的问题就是非常的耗内存，poi有一套SAX模式的API可以一定程度的解决一些内存溢出的问题，但POI还是有一些缺陷，比如07版Excel解压缩以及解压后存储都是在内存中完成的，内存消耗依然很大。easyexcel重写了poi对07版Excel的解析，能够原本一个3M的excel用POI sax依然需要100M左右内存降低到几M，并且再大的excel不会出现内存溢出，03版依赖POI的sax模式。在上层做了模型转换的封装，让使用者更加简单方便

官方文档：https://www.yuque.com/easyexcel/doc/easyexcel

EasyExcel能大大减少占用内存的主要原因是在解析Excel的时候没有将文件数据一次性加载到内存中，而是从磁盘上一行行读取数据，逐个解析。

![image-20210403132443148](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210403132443148.png)

### 2、POI-Excel写

#### 2.1创建一个maven

```xml
    <dependencies>
        <!--xls-->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi</artifactId>
            <version>3.9</version>
        </dependency>

        <!--xlsx-->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml</artifactId>
            <version>3.9</version>
        </dependency>

        <!--日期格式化工具-->
        <dependency>
            <groupId>joda-time</groupId>
            <artifactId>joda-time</artifactId>
            <version>2.10.1</version>
        </dependency>

        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>RELEASE</version>
            <scope>compile</scope>
        </dependency>
    </dependencies> 
```

#### 2.2 HSSF写入.xls文件

```java
public class ExcelWriteTest {

    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 生成.xls文件
     * @throws Exception
     */
    @Test
    public void testWriteXls() throws Exception {
        // 1、创建一个工作蒲
        Workbook workbook = new HSSFWorkbook();
        // 2、创建一个工作表
        Sheet sheet = workbook.createSheet("工作表1");
        // 3、创建第一行
        Row row1 = sheet.createRow(0);
        // 4、创建一个单元格
        Cell cell11 = row1.createCell(0);
        cell11.setCellValue("序号");

        Cell cell12 = row1.createCell(1);
        cell12.setCellValue("姓名");

        // 3、创建第二行
        Row row2 = sheet.createRow(1);
        // 4、创建一个单元格
        Cell cell21 = row2.createCell(0);
        cell21.setCellValue("1");

        Cell cell22 = row2.createCell(1);
        cell22.setCellValue("CodeTiger");

        FileOutputStream fileOutputStream = new FileOutputStream(path + "test.xls");
        workbook.write(fileOutputStream);
        fileOutputStream.close();
    }
}
```

#### 2.3 XSSF写入.xlsx文件

```java
public class ExcelWriteTest {

    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 生成.xlsx文件
     * @throws Exception
     */
    @Test
    public void testWriteXlsx() throws Exception {
        // 1、创建一个工作蒲
        Workbook workbook = new XSSFWorkbook();
        // 2、创建一个工作表
        Sheet sheet = workbook.createSheet("工作表1");
        // 3、创建第一行
        Row row1 = sheet.createRow(0);
        // 4、创建一个单元格
        Cell cell11 = row1.createCell(0);
        cell11.setCellValue("序号");

        Cell cell12 = row1.createCell(1);
        cell12.setCellValue("姓名");

        // 3、创建第二行
        Row row2 = sheet.createRow(1);
        // 4、创建一个单元格
        Cell cell21 = row2.createCell(0);
        cell21.setCellValue("1");

        Cell cell22 = row2.createCell(1);
        cell22.setCellValue("CodeTiger");

        FileOutputStream fileOutputStream = new FileOutputStream(path + "test.xlsx");
        workbook.write(fileOutputStream);
        fileOutputStream.close();
    }
}
```

#### 2.4 HSSF写大文件

缺点：最多只能处理65536行，否则会抛出异常

```java
java.lang.IllegalArgumentException: Invalid row number (65536) outside allowable range (0..65535)
```

优点：过程中写入缓存，不操作磁盘，最后一次性写入磁盘，速度快。

```java
package com.codeliu;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.api.Test;

import java.io.FileOutputStream;

public class ExcelWriteTest {

    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 写入大批量数据到xls文件
     */
    @Test
    public void testWriteBigDataXls() throws Exception {
        long startTime = System.currentTimeMillis();

        Workbook workbook = new HSSFWorkbook();
        Sheet sheet = workbook.createSheet("工作表1");

        // xls文件最多65536行，超过会报错
        for (int i = 0; i < 65536; i++) {
            Row row = sheet.createRow(i);
            for (int j = 0; j < 10; j++) {
                Cell cell = row.createCell(j);
                cell.setCellValue(j + 1);
            }
        }

        FileOutputStream fileOutputStream = new FileOutputStream(path + "bigdata.xls");
        workbook.write(fileOutputStream);
        fileOutputStream.close();

        long endTime = System.currentTimeMillis();
        System.out.println((double)(endTime - startTime) / 1000);
    }
}
```

![image-20210403183855668](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210403183855668.png)

写65536行用了1.264s。

#### 2.5 XSSF写大文件

缺点：写数据时非常慢，非常耗内存，也会发生内存溢出，比如100万条。

优点：可以写较大的数据量，如20w条。

```java
package com.codeliu;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.api.Test;

import java.io.FileOutputStream;

public class ExcelWriteTest {

    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 写入大批量数据到xlsx文件
     */
    @Test
    public void testWriteBigDataXlsx() throws Exception {
        long startTime = System.currentTimeMillis();

        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("工作表1");

        for (int i = 0; i < 65537; i++) {
            Row row = sheet.createRow(i);
            for (int j = 0; j < 10; j++) {
                Cell cell = row.createCell(j);
                cell.setCellValue(j + 1);
            }
        }

        FileOutputStream fileOutputStream = new FileOutputStream(path + "bigdata.xlsx");
        workbook.write(fileOutputStream);
        fileOutputStream.close();

        long endTime = System.currentTimeMillis();
        System.out.println((double)(endTime - startTime) / 1000);
    }
}

```

同样的内容，写65537行耗时7.478s

![image-20210403184412465](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210403184412465.png)

20w条数据，耗时23.976s

![image-20210403184655683](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210403184655683.png)

#### 2.6 SXSSF写大文件

XSSF的升级版。

优点：可以写非常大的数据量，如100w条甚至更多，写数据的速度更快，占用的内存更少。

**注意**：

过程中会产生临时文件，需要清理临时文件。

默认有100条记录被保存在内存中，如果超过这个数量，则最前面的数据被写入临时文件。

如果想自定义内存中数据的数量，可以使用new SXSSFWorkbook(数量);

```java
package com.codeliu;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.streaming.SXSSFWorkbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.api.Test;

import java.io.FileOutputStream;

public class ExcelWriteTest {

    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * SXSSFWorkbook写入大批量数据到xlsx文件
     */
    @Test
    public void testWriteBigDatasXlsx() throws Exception {
        long startTime = System.currentTimeMillis();

        Workbook workbook = new SXSSFWorkbook();
        Sheet sheet = workbook.createSheet("工作表1");

        for (int i = 0; i < 200000; i++) {
            Row row = sheet.createRow(i);
            for (int j = 0; j < 10; j++) {
                Cell cell = row.createCell(j);
                cell.setCellValue(j + 1);
            }
        }

        FileOutputStream fileOutputStream = new FileOutputStream(path + "bigdatas.xlsx");
        workbook.write(fileOutputStream);
        fileOutputStream.close();
        // 清除临时文件
        ((SXSSFWorkbook)workbook).dispose();

        long endTime = System.currentTimeMillis();
        System.out.println((double)(endTime - startTime) / 1000);
    }
}
```

写20w条数据，耗时2.903s

![image-20210403185841454](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210403185841454.png)

SXSSFWorkbook官方的解释：实现“BigGridDemo”策略的流式XSSFWorkbook版本，这允许写入非常大的文件而不会耗尽内存，因为任何时候只有可配置的行部分被保存在内存中。

请注意，仍然可能会消耗大量内存，这些内存基于你正在使用的功能，例如合并区域，注释.....仍然只存储在内存中，因此如果广泛使用，可能需要大量内存。

### 3. POI-Excel读

#### 3.1 读excel文件

```java
package com.codeliu;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.api.Test;

import java.io.FileInputStream;

public class ExcelReadTest {
    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 读 xls文件
     * @throws Exception
     */
    @Test
    public void testReadXls() throws Exception {
        // 获取文件流
        FileInputStream fileInputStream = new FileInputStream(path + "test.xls");

        Workbook workbook = new HSSFWorkbook(fileInputStream);
        Sheet sheet = workbook.getSheetAt(0);
        for (int i = 0; i < sheet.getPhysicalNumberOfRows(); i++) {
            Row row = sheet.getRow(i);
            for (int j = 0; j < row.getPhysicalNumberOfCells(); j++) {
                Cell cell = row.getCell(j);
                System.out.println(cell.getStringCellValue());
            }
        }

        fileInputStream.close();
    }

    /**
     * 读 xlsx文件
     * @throws Exception
     */
    @Test
    public void testReadXlsx() throws Exception {
        // 获取文件流
        FileInputStream fileInputStream = new FileInputStream(path + "test.xlsx");

        Workbook workbook = new XSSFWorkbook(fileInputStream);
        Sheet sheet = workbook.getSheetAt(0);
        for (int i = 0; i < sheet.getPhysicalNumberOfRows(); i++) {
            Row row = sheet.getRow(i);
            for (int j = 0; j < row.getPhysicalNumberOfCells(); j++) {
                Cell cell = row.getCell(j);
                System.out.println(cell.getStringCellValue());
            }
        }

        fileInputStream.close();
    }
}
```

#### 3.2 读取不同类型的列

```java
package com.codeliu;

import org.apache.poi.hssf.usermodel.HSSFDateUtil;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.joda.time.DateTime;
import org.junit.jupiter.api.Test;

import java.io.FileInputStream;
import java.util.Date;

public class ExcelReadTest {
    String path = "D:\\project\\idea-demo\\excelUtil\\poi-excel\\";

    /**
     * 测试读取不同类型的列
     */
    @Test
    public void testCellType() throws Exception {
        // 获取文件流
        FileInputStream fileInputStream = new FileInputStream(path + "test.xlsx");

        Workbook workbook = new XSSFWorkbook(fileInputStream);
        Sheet sheet = workbook.getSheetAt(0);
        for (int i = 0; i < sheet.getPhysicalNumberOfRows(); i++) {
            Row row = sheet.getRow(i);
            for (int j = 0; j < row.getPhysicalNumberOfCells(); j++) {
                Cell cell = row.getCell(j);
                // 获取列的字段类型
                int cellType = cell.getCellType();
                String cellValue = "";

                switch (cellType) {
                    case Cell.CELL_TYPE_NUMERIC:
                        System.out.print("【NUMERIC】");
                        // 判断是数字还是时间
                        if (HSSFDateUtil.isCellDateFormatted(cell)) {
                            System.out.print("【日期】");
                            Date date = cell.getDateCellValue();
                            cellValue = new DateTime(date).toString("yyyy-MM-dd");
                        } else {
                            System.out.print("【数字】");
                            // 先转化为字符串，防止溢出
                            cell.setCellType(Cell.CELL_TYPE_STRING);
                            cellValue = cell.getStringCellValue();
                        }

                        break;
                    case Cell.CELL_TYPE_STRING:
                        System.out.print("【字符串】");
                        cellValue = cell.getStringCellValue();
                        break;
                    case Cell.CELL_TYPE_FORMULA:
                        break;
                    case Cell.CELL_TYPE_BLANK:
                        System.out.print("【空】");
                        break;
                    case Cell.CELL_TYPE_BOOLEAN:
                        System.out.print("【boolean】");
                        cellValue = String.valueOf(cell.getBooleanCellValue());
                        break;
                    case Cell.CELL_TYPE_ERROR:
                        System.out.print("【error】");
                        break;
                }

                System.out.print(cellValue);
            }
            System.out.println();
        }

        fileInputStream.close();
    }
}
```

### 4、EasyExcel

> 引入jar包

```xml
<groupId>com.alibaba</groupId>
<artifactId>easyexcel</artifactId>
<version>2.2.7</version>
```

> 操作

官方文档：https://www.yuque.com/easyexcel/doc/easyexcel