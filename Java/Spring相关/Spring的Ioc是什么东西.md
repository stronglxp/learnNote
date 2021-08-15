### 0、写在前面

本文源码都是基于Spring5，官方文档[链接](https://docs.spring.io/spring-framework/docs/current/reference/html/)

### 1、什么是Ioc

**控制反转**（英语：Inversion of Control，缩写为**IoC**），是面向对象编程中的一种设计原则，可以用来减低计算机代码之间的耦合度)。其中最常见的方式叫做**依赖注入**（Dependency Injection，简称**DI**），还有一种方式叫“依赖查找”（Dependency Lookup）。

在Spring中，简单的说，**控制反转就是把对象创建和对象之间的调用过程交给Spring来管理**。这样可以降低代码之间的耦合度。

### 2、Ioc底层技术

（1）XML解析

（2）工厂模式

（3）反射

### 3、Bean管理

spring有两种bean，普通bean和工厂bean（factoryBean）

**普通bean**：在配置文件中定义bean类型就是返回类型。

**工厂bean**：在配置文件中定义bean类型可以和返回类型不一样。

### 4、Bean作用域

单例（singleton）和多例（prototype）。

设置scope属性为singleton的时候，加载Spring配置文件的时候就会创建单实例对象。

设置scope属性为prototype的时候，在调用getBean方法的时候创建对象。

### 5、Bean生命周期

从对象创建到销毁的过程。

（1）通过构造器创建bean实例（无参数构造）

（2）为bean的属性设置值和对其他bean引用（调用set方法）

（3）bean实例传递给后置处理器`BeanPostProcessor`的`postProcessBeforeInitialization`方法

（4）调用bean的初始化方法（需要配置初始化的方法）

（5）bean实例传递给后置处理器`BeanPostProcessor`的`postProcessAfterInitialization`方法

（6）使用bean（对象获取到了）

（7）当容器关闭的时候，调用bean销毁的方法（需要配置销毁的方法）