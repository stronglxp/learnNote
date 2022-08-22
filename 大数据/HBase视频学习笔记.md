### 一、HBase简介

#### 1.1 HBase定义

根据官网的介绍，[Apache](https://www.apache.org/) HBase™ is the [Hadoop](https://hadoop.apache.org/) database, a distributed, scalable, big data store。Use Apache HBase™ when you need random, realtime read/write access to your Big Data. This project's goal is the hosting of very large tables -- billions of rows X millions of columns -- atop clusters of commodity hardware. 

Apache HBase是以hdfs为数据存储的，一种分布式、可扩展的NoSQL数据库。

#### 1.2 HBase数据模型

HBase的设计理念依据Google的BigTable论文，论文中对于数据模型的首句介绍：**BigTable是一个稀疏的、分布式的、持久的多维排序map**。

之后对于映射的解释如下：该映射由行键、列键和时间戳索引，映射中的每个值都是一个未解释（经过序列化）的字节数组。

最终HBase关于数据模型和BigTable的对应关系如下：HBase使用与BigTable非常相似的数据模型，用户将数据行存储在带标签的表中。数据行具有可排序的键和任意数量的列，该表存储稀疏，因此如果用户喜欢，同一表中的行可以具有疯狂变化的列。

理解HBase数据模型的关键在于**稀疏、分布式、多维、排序**的映射，其中映射map指代非关系型数据库的key-value结构。

##### 1.2.1 HBase逻辑结构

HBase可以用于存储多种结构的数据，以JSON为例，存储的数据原貌为：

```json
{
  "row_key1": {
    "personal_info": {
      "name": "zhangsan",
      "city": "北京",
      "phone": "131********"
    },
    "office_info": {
      "tel": "010-11111111",
      "address": "atguigu"
    }
  },
  "row_key11": {
    "personal_info": {
      "city": "上海",
      "phone": "132********"
    },
    "office_info": {
      "tel": "010-11111111"
    }
  },
  "row_key2": {
    ......
  }
}
```

存储数据稀疏，数据存储多维，不同的行具有不同的列。

数据存储整体有序，按照RowKey的字典序排列，RowKey为Byte数组。

![image-20220821224521666](HBase视频学习笔记.assets/image-20220821224521666-1093123.png)

##### 1.2.2 HBase物理存储结构

物理存储结构即为数据映射关系，而在概念视图的空单元格，底层实际根本不存储。

![image-20220821225037295](HBase视频学习笔记.assets/image-20220821225037295-1093438.png)

##### 1.2.3 数据模型

（1）NameSpace

命名空间，类似于关系型数据库的database概念，每个命名空间下有多个表。HBase有两个自带的命名空间，分别是hbase和default，hbase中存放的是HBase内置的表，default是用户默认使用的命名空间。

（2）Table

类似于关系型数据库的表概念。不同的是，Hbase定义表时只需要声明列族即可，不需要声明具体的列。因为数据存储是稀疏的，所以往HBase写入数据时，字段可以动态、按需指定。因此，和关系型数据库相比，HBas能够轻松应对字段变更的场景。

（3）Row

HBase表中的每一行数据都由一个RowKey和多个Column（列）组成，数据是按照RowKey的字典顺序存储的，并且查询数据时只能根据RowKey进行检索，所以RowKey的设计十分重要。

（4）Column

Hbase中的每个列都由Column Family（列族）和Column Qualifier（列限定符）进行限定，例如info:name, info:age。建表时，只需要指明列族，而列限定符无需预先定义。

（5）TimeStamp

用于标识数据的不同版本（version），每条数据写入时，系统会自动为其加上该字段，其值为写入HBase的时间。

（6）Cell

由{rowkey, column family:column qualifier, timestamp}唯一确定的单元，cell中的数据全部是字节码形式存储。

#### 1.3 HBase基础架构







