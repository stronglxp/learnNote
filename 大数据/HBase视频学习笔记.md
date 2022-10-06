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

![image-20220822222441732](HBase视频学习笔记.assets/image-20220822222441732-1178283.png)

架构角色：

（1）Master

实现类为HMaster，负责监控集群中所有的RegionServer实例。主要作用如下：

- 管理元数据表格hbase:meta，接收用户对表格创建修改删除的命令并执行。
- 监控region是否需要进行负载均衡、故障转移和region的拆分。

通过启动多个后台线程监控实现上述功能：

- **LoadBalancer负载均衡器**：周期性监控region分布在regionServer上面是否均衡，由参数hbase.balancer.period控制周期时间，默认5min。
- **CatalogJanitor元数据管理器**：定期检查和清理hbase:meta中的数据。
- **MasterProcWAL master预写日志处理器**：把master需要执行的任务记录在预写日志WAL中，如果master宕机，让backupMaster读取日志继续干。

（2）Region Server

Region Server实现类为HRegionServer，主要作用如下：

- 负责数据cell的处理，例如写入数据put，查询数据get等。
- 拆分合并region的实际执行者，有master监控，有regionServer执行。

（3）zookeeper

HBase通过Zookeeper来做master的高可用，记录RegionServer的部署信息，并且存储有meta表的位置信息。

HBase对于数据的读写操作时直接访问Zookeeper，在2.3版本推出Master Registry模式，客户端可以直接访问master。使用此功能，会加大master的压力，减轻对zookeeper的压力。

（4）HDFS

HDFS为HBase提供最终的底层数据存储服务，同时为HBase提供高容错的支持。

### 二、HBase快速入门

#### 2.1 HBase安装部署

使用三台机器进行安装部署，分别为hadoop1，hadoop2，hadoop3。

##### 2.1.1 Zookeeper部署

按照官方文档在三台机器安装zookeeper并启动。

##### 2.1.2 Hadoop部署

按照官方文档在三台机器安装hadoop并启动。

##### 2.1.3 HBase安装

将HBase解压到指定目录，配置环境变量

```shell
vi /etc/profile.d/my_env.sh
export HBASE_HOME=hbase文件夹路径
export PATH=$PATH:$HBAS_HOME/bin
source /etc/profile.d/my_env.sh
```

修改配置文件

```shell
# hbase-env.sh
vi /opt/module/hbase/conf/hbase-env.sh
# 默认为true，表示使用hbase自带的zk
export HBASE_MANAGES_ZK=false

# hbase-site.xml
vi /opt/module/hbase/conf/hbase-site.xml
# 将默认配置清空，改成下面内容
<property>
	<name>hbase.cluster.distributed</name>
	<value>true</value>
</property>
<property>
	<name>hbase.zookeeper.quorum</name>
	<value>hadoop1,hadoop2,hadoop3</value>
</property>
<property>
	<name>hbase.rootdir</name>
	<value>hdfs://hadoop2:8020/hbase</value>
</property>

# regionservers
vi /opt/module/hbase/conf/regionservers
# 清空默认内容，改成下面的
hadoop1
hadoop2
hadoop3
```

解决HBase和Hadoop的log4j兼容性问题，修改HBase的jar包，使用Hadoop的jar包

```shell
mv /opt/module/hbase/lib/client-facing-thirdparty/slf4j-reload4j-1.7.33.jar /opt/module/hbase/lib/client-facing-thirdparty/slf4j-reload4j-1.7.33.jar.bak
```

三台机器的配置文件进行同步。

启动HBase（在哪台机器启动，HMaster就在哪台机器上）

```shell
bin/start-hbase.sh
```

##### 2.1.4 HBase高可用

在HBase中HMaster负责监控HRegionServer的生命周期，均衡RegionServer的负载，如果HMaster挂了，那么整个Hbase集群将不可用，所以HBase支持对HMaster的高可用配置。

```shell
# 先关闭集群
bin/stop-hbase.sh
# 在conf目录下创建backup-masters文件
touch conf/backup-masters
echo hadoop3 > conf/backup-masters
```

将`backup-masters`文件分发到其他机器，然后启动hbase，查看web页面。

当hadoop2的master挂掉后，hadoop3的backup master会变成master。当hadoop2上的master正常后，会变成backup master。

#### 2.2 HBase shell

进入hbase shell后，使用`help`命令就行了。

### 三、HBase API使用

官方API文档：https://hbase.apache.org/2.4/apidocs/index.html

#### 3.1 环境准备

idea新建maven项目，在pom里导入相关的依赖

```xml
<dependencies>
  <dependency>
    <groupId>org.apache.hbase</groupId>
    <artifactId>hbase-client</artifactId>
    <version>2.4.11</version>
  </dependency>
</dependencies>

<repositories>
  <repository>
    <id>HDPReleases2</id>
    <name>HDPReleases2</name>
    <url>https://repo.hortonworks.com/content/repositories/releases/</url>
    <layout>default</layout>
    <releases>
      <enabled>true</enabled>
      <updatePolicy>daily</updatePolicy>
      <checksumPolicy>warn</checksumPolicy>
    </releases>
    <snapshots>
      <enabled>false</enabled>
      <updatePolicy>never</updatePolicy>
      <checksumPolicy>fail</checksumPolicy>
    </snapshots>
  </repository>
</repositories>
```

#### 3.2 创建连接

根据官方文档介绍，HBase 的客户端连接由 ConnectionFactory 类来创建，用户使用完成之后需要手动关闭连接。同时连接是一个重量级的，推荐一个进程使用一个连接，对 HBase的命令通过连接中的两个属性 Admin 和 Table 来实现。

##### 3.2.1 单线程创建连接

```java
package com.codeliu;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.client.AsyncConnection;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;

import java.io.IOException;
import java.util.concurrent.CompletableFuture;

public class SingleThreadConnect {
    public static void main( String[] args ) throws IOException {
        Configuration conf = new Configuration();
        conf.set("hbase.zookeeper.quorum", "doraemon");

        Connection connection = ConnectionFactory.createConnection(conf);
        CompletableFuture<AsyncConnection> asyncConnection = ConnectionFactory.createAsyncConnection(conf);

        System.out.println(connection);
        System.out.println(asyncConnection);

        connection.close();
    }
}
```

##### 3.2.2 多线程创建连接

使用单例模式，确保只会存在一个连接实例。

```java
package com.codeliu;

import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;

import java.io.IOException;

public class HBaseConnection {
    private static Connection connection = null;
    private HBaseConnection() {}

    static {
        try {
            // 默认会去加载resources下面的hbase-default.xml和hbase-site.xml文件里的配置
            connection = ConnectionFactory.createConnection();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static Connection getConnection() {
        return connection;
    }

    public static void close() throws IOException {
        if (connection != null) {
            connection.close();
        }
    }
}
```

在resources文件夹下面创建文件hbase-site.xml，其中`doraemon`是服务器的域名，需要配置hosts文件

```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>doraemon</value>
    </property>
</configuration>
```

#### 3.3 DDL

##### 3.3.1 创建命名空间

```java
public static void createNameSpace(String nameSpace) throws IOException {
    Connection connection = HBaseConnection.getConnection();
    Admin admin = connection.getAdmin();
     admin.createNamespace(NamespaceDescriptor.create(nameSpace).addConfiguration("create", "CodeTiger").build());
    HBaseConnection.close();
}
```

报错，但是在hbase shell中使用命令是正常的。

![image-20220909224303675](HBase视频学习笔记.assets/image-20220909224303675-2734585.png)

查看zk的日志，发现使用java调用的时候有报错

![image-20220909224425197](HBase视频学习笔记.assets/image-20220909224425197-2734666.png)

再查看sn的日志，发现集群id不一致报错

![image-20220910104506590](HBase视频学习笔记.assets/image-20220910104506590-2777907.png)

修复

```shell
[root@ ~]#: cp -r /tmp/hadoop-root/dfs/name/current/VERSION /tmp/hadoop-root/dfs/namesecondary/current/
cp: overwrite ‘/tmp/hadoop-root/dfs/namesecondary/current/VERSION’? y

[root@ hadoop-3.1.3]#: ./sbin/hadoop-daemon.sh stop secondarynamenode
WARNING: Use of this script to stop HDFS daemons is deprecated.
WARNING: Attempting to execute replacement "hdfs --daemon stop" instead.

[root@ hadoop-3.1.3]#: ./sbin/hadoop-daemon.sh start secondarynamenode
WARNING: Use of this script to start HDFS daemons is deprecated.
WARNING: Attempting to execute replacement "hdfs --daemon start" instead.
```

还是连不上。。

##### 3.3.2 判断表是否存在

```java
public static boolean isTableExists(String namespace, String tableName) throws IOException {
    Connection connection = HBaseConnection.getConnection();
    Admin admin = connection.getAdmin();
    boolean b = admin.tableExists(TableName.valueOf(namespace, tableName));
    admin.close();
    connection.close();
    return b;
}
```

##### 3.3.3 创建表格

```java
public static void createTable(String namespace, String tableName, String ... columnFamilies) throws IOException {
    if (columnFamilies.length == 0) {
      log.error("列族不能为空");
      return;
    }
    if (isTableExists(namespace, tableName)) {
      log.error("表格已经存在");
      return;
    }
    Connection connection = HBaseConnection.getConnection();
    Admin admin = connection.getAdmin();
    TableDescriptorBuilder tableDescriptorBuilder = TableDescriptorBuilder.newBuilder(TableName.valueOf(namespace, tableName));
    for (String columnFamily : columnFamilies) {
      tableDescriptorBuilder.setColumnFamily(ColumnFamilyDescriptorBuilder.newBuilder(Bytes.toBytes(columnFamily)).setMaxVersions(3).build());
    }
    admin.createTable(tableDescriptorBuilder.build());
    admin.close();
    connection.close();
}
```

##### 3.3.4 修改表格

```java
public static void modifyTable(String namespace, String tableName, String columnFamily, Integer version) throws IOException {
    Connection connection = HBaseConnection.getConnection();
    Admin admin = connection.getAdmin();
    // 获取原先的
    TableDescriptor descriptor = admin.getDescriptor(TableName.valueOf(namespace, tableName));
    TableDescriptorBuilder tableDescriptorBuilder = TableDescriptorBuilder.newBuilder(descriptor);

    ColumnFamilyDescriptor columnFamily1 = descriptor.getColumnFamily(Bytes.toBytes(columnFamily));
    tableDescriptorBuilder.modifyColumnFamily(ColumnFamilyDescriptorBuilder.newBuilder(columnFamily1).setMaxVersions(version).build());
    admin.modifyTable(tableDescriptorBuilder.build());

    admin.close();
    connection.close();
}
```

##### 3.3.5 删除表格

```java
public static void deleteTable(String namespace, String tableName) throws IOException {
    Connection connection = HBaseConnection.getConnection();
    Admin admin = connection.getAdmin();

    admin.disableTable(TableName.valueOf(namespace, tableName));
    admin.deleteTable(TableName.valueOf(namespace, tableName));

    admin.close();
    connection.close();
}
```

#### 3.4 DML

##### 3.4.1 插入数据

```java
		public static void putCell(String namespace, String tableName, String rowKey, String columnFamily, String columnName, String value) throws IOException {
        Table table = connection.getTable(TableName.valueOf(namespace, tableName));
        Put put = new Put(Bytes.toBytes(rowKey));
        put.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), Bytes.toBytes(value));
        table.put(put);
        table.close();
    }
```

##### 3.4.2 读取数据

```java
public static void getCells(String namespace, String tableName, String rowKey, String columnFamily, String columnName) throws IOException {
    Table table = connection.getTable(TableName.valueOf(namespace, tableName));
    Get get = new Get(Bytes.toBytes(rowKey));
    get.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));
    get.readAllVersions();
    Result result = table.get(get);
    Arrays.stream(result.rawCells()).forEach(cell -> System.out.println(new String(CellUtil.cloneValue(cell))));
}
```

##### 3.4.3 扫描数据

```java
public static void scanRows(String namespace, String tableName, String startRow, String stopRow) throws IOException {
    Table table = connection.getTable(TableName.valueOf(namespace, tableName));
    Scan scan = new Scan();
    // 默认包含startRow
    scan.withStartRow(Bytes.toBytes(startRow));
    // 默认不包含stopRow
    scan.withStopRow(Bytes.toBytes(stopRow));
    ResultScanner scanner = table.getScanner(scan);
    for (Result result : scanner) {
      Cell[] cells = result.rawCells();
      for (Cell cell : cells) {
        System.out.print(new String(CellUtil.cloneRow(cell)) + "-" + new String(CellUtil.cloneFamily(cell)) +
                         "-" + new String(CellUtil.cloneQualifier(cell)) + "-" + new String(CellUtil.cloneValue(cell)) + "\t");
      }
      System.out.println();
    }
    table.close();
}
```

##### 3.4.4 过滤数据

```java
public static void filterRows(String namespace, String tableName, String startRow, String stopRow, String columnFamily, String columnName, String value) throws IOException {
    Table table = connection.getTable(TableName.valueOf(namespace, tableName));
    Scan scan = new Scan();
    // 默认包含startRow
    scan.withStartRow(Bytes.toBytes(startRow));
    // 默认不包含stopRow
    scan.withStopRow(Bytes.toBytes(stopRow));

    FilterList filterList = new FilterList();
    // 结果只保留当前列的数据
    ColumnValueFilter columnValueFilter = new ColumnValueFilter(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), CompareOperator.EQUAL, Bytes.toBytes(value));
    filterList.addFilter(columnValueFilter);
    // 结果会保留整行数据，如果rowKey没有对应的column，也会被保留
    SingleColumnValueFilter singleColumnValueFilter = new SingleColumnValueFilter(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), CompareOperator.EQUAL, Bytes.toBytes(value));
    filterList.addFilter(singleColumnValueFilter);
    scan.setFilter(filterList);
    ResultScanner scanner = table.getScanner(scan);
    for (Result result : scanner) {
      Cell[] cells = result.rawCells();
      for (Cell cell : cells) {
        System.out.print(new String(CellUtil.cloneRow(cell)) + "-" + new String(CellUtil.cloneFamily(cell)) +
                         "-" + new String(CellUtil.cloneQualifier(cell)) + "-" + new String(CellUtil.cloneValue(cell)) + "\t");
      }
      System.out.println();
    }
    table.close();
}
```

##### 3.4.5 删除数据

```java
public static void deleteColumn(String namespace, String tableName, String rowKey, String columnFamily, String columnName) throws IOException {
    Table table = connection.getTable(TableName.valueOf(namespace, tableName));
    Delete delete = new Delete(Bytes.toBytes(rowKey));
    // 删除单个版本
    delete.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));
    // 删除所有版本
    delete.addColumns(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));
    // 删除列族
    delete.addFamily(Bytes.toBytes(columnFamily));

    table.delete(delete);
    table.close();
}
```

### 四、HBase架构

#### 4.1 Master架构

![image-20220925132417087](HBase视频学习笔记.assets/image-20220925132417087-4083459.png)

**meta表介绍**

全称hbase:meta，只是在list命令中被过滤了，本质上和hbase其他表一样。

RowKey：([table], [region start key], [region id])即表名，region起始位置和regionID。

列：

（1）info:regioninfo为region信息，存储一个HRegionInfo对象。

（2）info:server，当前region所处的RegionServer信息，包含端口号。

（3）info:serverstartcode，当前region被分到RegionServer的起始时间。

如果一个表处于切分的过程中，即region切分，还会多出两列info:splitA和info:splitB，存储值也是HRegionInfo对象，拆分结束后，删除这两列。

注意：在客户端对元数据进行操作的时候才会连接master，如果对数据进行读写，直接连接zookeeper读取目录/hbase/meta-region-server节点信息，会记录meta表格的位置。直接读取即可，不需要访问master，这样可以减轻master的压力，相当于master专注meta表的写操作，客户端直接读取meta表。

在hbase 2.3版本更新了一种新模式：master registry。客户端可以访问master来读取meta表信息，加大了master的压力，减轻了zookeeper的压力。

#### 4.2 RegionServer架构

![image-20220925215254124](HBase视频学习笔记.assets/image-20220925215254124-4113976.png)

（1）MemStore

写缓存，由于HFile中的数据要求是有序的，所以数据是先存储在MemStore中，排好序后，等到达刷写时机才会刷写到HFile，每次刷写都会形成一个新的HFile，写入到对应的文件夹store中。

（2）WAL

由于数据要经过MemStore排序后才能刷写到HFile，但把数据保存在内存中有很高的概率会导致数据丢失，为了解决这个问题，数据会写到一个叫做Write-Ahead-Logfile的文件中，然后再写入到MemStore中。所以在系统出现故障的时候，数据可以通过这个日志文件重建。

（3）BlockCache

读缓存，每次查询出的数据会缓存在BlockCache中，方便下次查询。

#### 4.3 写流程

![image-20220925221236336](HBase视频学习笔记.assets/image-20220925221236336-4115157.png)

写数据的时候首先会创建hbase的重量级连接

（1）首先访问zookeeper，获取hbase:meta表位于哪个Region Server。

（2）访问对应的Region Server，获取hbase:meta表，将其缓存到连接中，作为连接属性MetaCache，由于Meta表具有一定的数据量，导致了创建连接比较慢。

之后使用创建的连接获取table，这是一个轻量级的连接，只会在第一次创建的时候去访问RegionServer检查表格是否存在，之后在获取table的时候不会访问RegionServer。

（3）调用table的put方法写入数据，此时还需要解析RowKey，对照缓存的MetaCache，查看具体的写入位置有哪个RegionServer。

（4）将数据顺序写入（追加）到WAL，此处写入是直接落盘的，并设置专门的线程控制WAL预写日志的滚动（类似Flume）。

（5）根据写入命令的RowKey和ColumnFamily查看具体写入到哪个MemStory，并且在MemStory中排序。

（6）向客户端发送ack。

（7）等达到MemStore的刷写时机后，将数据刷写到对应的story中。

#### 4.4 MemStore Flush

MemStore刷写由多个线程控制，条件相互独立。

主要的刷写规则是控制刷写文件的大小，在每一个刷写线程中都会进行监控。

（1）当某个memstore的大小达到了`hbase.hregion.memstore.flush.size`(默认值128M)，其所在region的所有memstore都会刷写。

当memstore的大小达到了`hbase.hregion.memstore.flush.size * hbase.hregion.memstore.block.multiplier`(128M * 4)的时候，会刷写同时阻止继续往该memstore写数据（由于线程监控是周期性的，所以有可能面对数据洪峰，尽管可能性比较小）

（2）由HRegionServer中的属性MemStoreFlusher内部线程FlushHandler控制。标准为`LOWER_MARK`（低水位线）和`HIGH_MARK`（高水位线），意义在于避免写缓存使用过多的内存造成OOM。

当region server中memstore的总大小达到低水位线`java_heapsize * hbase.regionserver.global.memstore.size（默认值0.4） * hbase.regionserver.global.memstore.size.lower.limit（默认值0.95）`，region会按照其所有memstore的大小顺序（由大到小）依次进行刷写，直到region server中所有memstore的总大小减小到上述值以下。

当region server中memstore的总大小达到高水位线`java_heapsize * hbase.regionserver.global.memstore.size（默认值0.4）`时，会同时阻止继续往所有的memstore写数据。

（3）为了避免数据长时间处于内存中，到达自动刷写时间也会触发memstore flush。由HRegionServer的属性PeriodicMemStoreFlusher控制进行，由于重要性比较低，5min才会执行一次。

自动刷新的时间间隔由该属性进行配置`hbase.regionserver.optionalcacheflushinterval`（默认1h）。

（4）当WAL文件的数量超过`hbase.regionserver.max.logs`，region会按照时间顺序依次进行刷写，直到WAL文件数量减小到`hbase.regionserver.max.logs`以下（该属性名已经废弃，现在无需手动设置，最大值为32）。

#### 4.5 读流程

##### 4.5.1 HFile结构

在了解读流程之前，需要先知道读取的数据是什么样子的。

HFile是存储在HDFS上每一个store文件夹下实际存储数据的文件，里面存储多种内容，包括数据本身（KV键值对）、元数据记录、文件信息、数据索引、元数据索引和一个固定长度的尾部信息（记录文件的修改情况）。

键值对按照块大小（默认64K）保存在文件中，数据索引按照块创建，块越多，索引越大。每一个HFile还会维护一个布隆过滤器（读取时可以大致判断要get的key是否存在HFile中）。

KV内容如下：

- rowlength：key的长度
- row：key的值
- columnfamilylength：列族长度
- columnfamily：列族
- columnqualifier：列名
- timestamp：时间戳，默认系统时间
- keytype：Put

由于HFile存储经过序列化，所以无法直接查看。可以通过HBase提供的命令来查看存储在HDFS上面的HFile元数据内容。

```shell
bin/hbase hfile -m -f /hbase/data/命名空间/表名/regionID/列族/HFile名
```

##### 4.5.2 读流程

![image-20221006215348521](HBase视频学习笔记.assets/image-20221006215348521-5064429.png)

创建连接同写流程。

（1）创建Table对象发送get请求。

（2）优先访问Block Cache，查找之前是否读取过，并且可以读取HFile的索引信息和布隆过滤器。

（3）不管读缓存中是否有数据（可能已经过期了），都需要再次读取写缓存和store中的文件。

（4）最终将所有读取到的数据合并版本，按照get的要求返回即可。

##### 4.5.3 合并读取数据优化

每次读取数据都要读取三个位置，最后进行版本的合并，效率比较低，所以需要对此优化。

（1）HFile带有索引文件，读取对应RowKey数据会比较快。

（2）Block Cache会缓存之前读取的内容和元数据信息，如果HFile没有发生变化（记录在HFile尾信息中），则不需要再次读取。

（3）使用布隆过滤器能够快速过滤当前HFile是否存在对应的RowKey，从而避免读取文件。（布隆过滤器使用HASH选法，不是绝对准确的，出错会造成多扫描一个文件，多读取数据结果没有影响）