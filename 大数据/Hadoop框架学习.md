### 一、Hadoop概述

#### 1、Hadoop是什么

- Hadoop是一个由Apache基金会所开发的**分布式系统基础架构**。
- 主要解决海量数据的存储和海量数据的分析计算问题。
- 广义上来说，Hadoop通常是指Hadoop生态圈，包括HBase、HDFS、Zookeeper等框架。

根据官网的描述，Hadoop包含下面几个modules：

- **Hadoop Common**: The common utilities that support the other Hadoop modules.
- **Hadoop Distributed File System (HDFS™)**: A distributed file system that provides high-throughput access to application data.
- **Hadoop YARN**: A framework for job scheduling and cluster resource management.
- **Hadoop MapReduce**: A YARN-based system for parallel processing of large data sets.

![image-20220403223408489](Hadoop框架学习.assets/image-20220403223408489-8996450.png)

#### 2、Hadoop发展历程

（1）Hadoop创始人Doug Cutting为了实现类似于Google的全文搜索功能，基于Lucene框架进行优化升级查询引擎和索引引擎。

（2）2001年年底Lucene成为Apache基金会的一个子项目。 

（3）对于海量数据的场景，Lucene框 架面 对与Google同样的困难，**存储海量数据困难，检索海量速度慢**。

（4）学习和模仿Google解决这些问题的办法 ：微型版Nutch。 

（5）Google在大数据方面的三篇论文，奠定了Hadoop的基础。**GFS --->HDFS**，**Map-Reduce --->MR**，**BigTable --->HBase**。

（6）2003-2004年，Google公开了部分GFS和MapReduce思想的细节，以此为基础Doug Cutting等人用

了2年业余时间实现了DFS和MapReduce机制，使Nutch性能飙升。

（7）2005 年Hadoop 作为 Lucene的子项目 Nutch的一部分正式引入Apache基金会。 

（8）2006 年 3 月份，Map-Reduce和Nutch Distributed File System （NDFS）分别被纳入到 Hadoop 项目

中，Hadoop就此正式诞生，标志着大数据时代来临。 

（9）名字来源于Doug Cutting儿子的玩具大象。

#### 3、Hadoop的三大发行版本

Hadoop 三大发行版本：Apache、Cloudera、Hortonworks。

- Apache 版本最原始（最基础）的版本，对于入门学习最好。2006

- Cloudera 内部集成了很多大数据框架，对应产品 CDH。2008

- Hortonworks 文档较好，对应产品 Hortonworks Data Platform（HDP）。2011

- Hortonworks 现在已经被 Cloudera 公司收购，推出新的品牌 CDP。

#### 4、Hadoop的优势

##### 4.1 高可靠性

底层维护多个数据副本，所以即使Hadoop某个计算元素或存储出现故障，也不会导致数据丢失。

##### 4.2 高扩展性

在集群间分配任务数据，可方便的扩展数以千计的节点。

##### 4.3 高效性

在MapReduce的思想下，Hadoop是并行工作的，以加快任务处理速度。

##### 4.4 高容错性

能够自动将失败的任务重新分配。

#### 5、Hadoop的组成

##### 5.1 Hadoop1.x 2.x 3.x的区别

在Hadoop1.x时，MapReduce同时处理业务逻辑运算和资源的调度，耦合性较大。

在Hadoop2.x时代，增加了Yarn，Yarn负责资源的调度，MapReduce负责运算。

Hadoop3.x在组成上没有变化。

![image-20220404184349901](Hadoop框架学习.assets/image-20220404184349901-9069031.png)

##### 5.2 HDFS概述

Hadoop Distributed File System，分布式文件系统，简称HDFS。几个主要的概念如下：

（1）**NameNode**：存储文件的元数据。如文件名、文件目录结构、文件属性（生存时间、副本数、文件权限），以及每个文件的块列表和块所在的DataNode等。

（2）**DataNode**：在本地文件系统存储文件块数据，以及块数据的校验和。

（3）**Secondary NameNode**：每隔一定时间对NameNode元数据进行备份。

![image-20220404191309653](Hadoop框架学习.assets/image-20220404191309653-9070791.png)

##### 5.3 Yarn概述

Yet Another Resource Negotiator简称Yarn，是一种资源协调者，是Hadoop的**资源管理器**。几个主要的概念如下：

（1）**ResourceManager**：管理整个集群的资源（CPU、内存等）

（2）**NodeManager**：管理单个节点服务器资源。

（3）**ApplicationMaster**：运行单个任务。

（4）**Container**：容器，相当于一台独立的服务器，里面封装了任务所需要的资源，比如CPU、内存、网络等。

![image-20220404192745413](Hadoop框架学习.assets/image-20220404192745413-9071666.png)

注意：

（1）client可以有多个。

（2）集群上可以运行很多个ApplicationMaster。

（3）每个NodeManager可以有多个Container。

##### 5.4 MapReduce概述

MapReduce将计算过程分为两个阶段：Map和Reduce。

- Map阶段并行处理输入数据。
- Reduce阶段对Map结果进行汇总。

![image-20220404194505212](Hadoop框架学习.assets/image-20220404194505212-9072706.png)

##### 5.5 HDFS、YARN和MR的关系

![image-20220404205634814](Hadoop框架学习.assets/image-20220404205634814-9076996.png)

##### 5.6 大数据技术生态体系

![image-20220404213052823](Hadoop框架学习.assets/image-20220404213052823-9079054.png)

（1）**Sqoop**：Sqoop 是一款开源的工具，主要用于在 Hadoop、Hive 与传统的数据库（MySQL）间进行数据的传递，可以将一个关系型数据库（例如 ：MySQL，Oracle 等）中的数据导进到 Hadoop 的 HDFS 中，也可以将 HDFS 的数据导进到关系型数据库中。

（2）**Flume**：Flume 是一个高可用的，高可靠的，分布式的海量日志采集、聚合和传输的系统，Flume 支持在日志系统中定制各类数据发送方，用于收集数据；

（3）**Kafka**：Kafka 是一种高吞吐量的分布式发布订阅消息系统；

（4）**Spark**：Spark 是当前最流行的开源大数据**内存计算**框架。可以基于 Hadoop 上存储的大数据进行计算。

（5）**Flink**：Flink 是当前最流行的开源大数据内存计算框架。用于实时计算的场景较多。

（6）**Oozie**：Oozie 是一个管理 Hadoop 作业（job）的工作流程调度管理系统。

（7）**HBase**：HBase 是一个分布式的、面向列的开源数据库。HBase 不同于一般的关系数据库，它是一个适合于非结构化数据存储的数据库。

（8）**Hive**：Hive 是基于 Hadoop 的一个数据仓库工具，可以将结构化的数据文件映射为一张数据库表，并提供简单的 SQL 查询功能，可以将 SQL 语句转换为 MapReduce 任务进行运行。其优点是学习成本低，可以通过类 SQL 语句快速实现简单的 MapReduce 统计，不必开发专门的 MapReduce 应用，十分适合数据仓库的统计分析。

（9）**Zookeeper**：它是一个针对大型分布式系统的可靠协调系统，提供的功能包括：配置维护、名字服务、分布式同步、组服务等。