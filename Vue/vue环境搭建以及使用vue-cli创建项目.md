我要跑vue项目，所以我要搞vue。

### 1、环境搭建

进入[node官网](https://nodejs.org/en/download/)下载对应版本的node，一步步安装即可。

![image-20210629150150436](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629150150436.png)

安装会自动配置路径和npm包管理环境，通过`node -v`进行验证

![image-20210629151411651](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629151411651.png)

### 2、安装vue-cli脚手架

Vue CLI文档：https://cli.vuejs.org/zh/guide/

```cmd
# 卸载旧版本
npm uninstall vue-cli -g
# 指定地址安装，加快速度
npm install -g @vue/cli --registry=https://registry.npm.taobao.org
```

![image-20210629153701958](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629153701958.png)

安装完成后，进行验证

```cmd
vue
vue --version
```

![image-20210629153815991](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629153815991.png)

完成上面的步骤后，我们就可以使用vue-cli新建项目。

### 3、使用vue-cli新建项目

#### 3.1 图形化界面创建项目

使用`vue ui`命令，会打开一个网页

```cmd
C:\Users\lxp>vue ui
🚀  Starting GUI...
🌠  Ready on http://localhost:8000
```

![image-20210629154122991](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629154122991.png)

按提示走应该就可以了，下面试试命令行创建。

#### 3.2 命令行创建项目

运行以下命令来创建一个新项目：

```cmd
vue create 项目名
```

首先进入某个特定文件夹，输入创建命令，注意**项目名不能包含大写字母**

![image-20210629154756766](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629154756766.png)

命令输入正确的情况下， 会让你选择创建vue-2还是vue-3的项目，根据需要选择，然后等待项目创建成功

![image-20210629155034152](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629155034152.png)

生成的项目结构如下

![image-20210629155155509](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629155155509.png)

根据它的提示启动项目

```cmd
cd vue-test
# 等同于npm run dev
npm run serve
```

![image-20210629155424743](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629155424743.png)

访问即可

![image-20210629155444224](vue环境搭建以及使用vue-cli创建项目.assets/image-20210629155444224.png)