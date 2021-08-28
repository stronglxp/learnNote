#### 1、String、StringBuffer和StringBuilder的区别是什么？String为啥是不可变的？

`String`类内部使用`final char value[]`存储值，所以是不可变的。

![image-20210825215337942](Java基础.assets/image-20210825215337942.png)

而StringBuilder和StringBuffer都继承自`AbstractStringBuilder`类，该类内部使用`char[] value`存储值，所以是可变的。

![image-20210825215459449](Java基础.assets/image-20210825215459449.png)