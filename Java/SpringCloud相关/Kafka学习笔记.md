[官方文档](https://kafka.apache.org/documentation/)

### 一、Kafka概述

#### 1.1 kafka是什么

![image-20220130204829505](Kafka学习笔记.assets/image-20220130204829505-3546911.png)

根据官网的文档，kafka是一个事件流平台，一般有以下用途：

- 发布（写入）和订阅（读取）事件流，包括从其他系统持续导入/导出数据。
- 根据需要持久可靠地存储事件流。
- 在事件发生时或回顾性地处理事件流。

所有这些功能都以分布式、高度可扩展、弹性、容错和安全的方式提供。 Kafka 可以部署在裸机硬件、虚拟机和容器上，也可以部署在本地和云端。您可以在自行管理 Kafka 环境和使用各种供应商提供的完全托管服务之间进行选择。

何为事件流，根据官网的描述：

> Technically speaking, event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed. Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time.

从技术上讲，事件流是从事件源（如数据库、传感器、移动设备、云服务和软件应用程序）以事件流的形式实时捕获数据的实践； 持久存储这些事件流以供以后检索； 实时和回顾性地操作、处理和响应事件流； 并根据需要将事件流路由到不同的目标技术。 因此，事件流确保了数据的连续流动和解释，以便正确的信息在正确的时间出现在正确的位置。

听这意思就像是一个数据中转站，它可以暂存/持久存储数据，在需要的时候去里面取数据。而kafka最常用的也是作为消息队列，**它是一个分布式的基于发布/订阅的消息队列**。

#### 1.2 消息队列

对于一个网站注册的示例，一般情况下是按照用户填写注册信息、注册信息写入数据库、返回注册成功的顺序执行。

![image-20220131094444219](Kafka学习笔记.assets/image-20220131094444219-3593486.png)

加入消息队列后，可以把发送短信的请求暂存在消息队列中，立刻把响应结果返回给用户，同时可以处理消息队列中的请求。

![image-20220131095026203](Kafka学习笔记.assets/image-20220131095026203-3593827.png)

使用消息队列的好处：

（1）**异步**：很多情况下，用户不想也不需要立即处理消息。消息队列提供了异步处理机制，允许用户把消息放入队列中，然后在需要的时候再去处理。

（2）**削峰**：在访问量突然剧增的情况下，使用消息队列可以使关键组件顶住突发的访问压力，不会因为超负荷的请求而完全崩溃。

（3）**解耦**：允许独立的扩展或修改两边的处理过程，只要确保它们遵守同样的接口约束。当系统中一部分组件失效时，不会影响到整个系统

消息队列一般有两种模式：**点对点模式**和**发布订阅模式**。

（1）**点对点模式**：一对一，消费者主动拉取数据，消费后清除消息。生产者生产消息发送到Queue 中，然后消费者从Queue 中取出并且消费消息。消息被消费以后，queue 中不再有存储，所以消费者不可能消费到已经被消费的消息。Queue 支持存在多个消费者， 但是对一个消息而言， 只会有一个消费者可以消费。

![image-20220131215431123](Kafka学习笔记.assets/image-20220131215431123-3637272.png)

（2）**发布/订阅模式**：一对多，消费者消费后不会清除消息。生产者（发布）将消息发布到 topic 中，同时有多个消费者（订阅）消费该消息。和点对点方式不同，发布到 topic 的消息会被所有订阅者消费。

![image-20220131220038642](Kafka学习笔记.assets/image-20220131220038642-3637639.png)

#### 1.3 kafka基础架构

