

## Docker学习

## 一、基础篇

### 1、Docker安装

#### 1.1 docker的基本组成

![img](https://kuangstudy.oss-cn-beijing.aliyuncs.com/bbs/2021/01/26/kuangstudy5f4abab7-20ef-47f1-88d8-3f910da48ad6.jpg?d=1616079346140)

#### 1.2 查看linux的版本

```shell
# 查看linux版本
[root@ ~]#: uname -r
3.10.0-514.26.2.el7.x86_64
```

#### 1.3 根据官方文档进行安装

```shell
# 1、uninstall old versions
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
                  
# 2、Install using the repository
sudo yum install -y yum-utils
 
# 3、set up the stable repository
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo # 默认是国外的镜像
    
sudo yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo # 推荐使用阿里云镜像

# 升级yum包索引
yum makecache fast

# 4、安装docker ce是社区版，ee是企业版
sudo yum install docker-ce docker-ce-cli containerd.io

# 也可以指定版本实现，具体看官方文档
```

![image-20210314210337122](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314210337122.png)

```shell
# 5、启动docker
sudo systemctl start docker
```

![image-20210314210438515](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314210438515.png)

```shell
# 6、运行hello world镜像
sudo docker run hello-world
```

![image-20210314210829000](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314210829000.png)

```shell
# 7、 查看下载的镜像
[root@ ~]#: docker images
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
hello-world   latest    d1165f221234   8 days ago   13.3kB
```

如果要卸载docker

```shell
# 1、Uninstall the Docker Engine, CLI, and Containerd packages:
sudo yum remove docker-ce docker-ce-cli containerd.io
 
# 2、Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

#### 1.4 阿里云镜像加速

![image-20210314221050590](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314221050590.png)

在服务器上进行如下配置

```shell
sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://mwg4rae3.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload

sudo systemctl restart docker
```

#### 1.5 回顾Hello World流程

![image-20210314210829000](file://C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314210829000.png?lastModify=1615732784)

如上图，可以知道运行一个镜像时的大致流程如下：

![image-20210314224508859](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314224508859.png)

#### 1.6 底层原理

**Docker是怎么工作的？**

Docker是一个CLient-Server的结构系统，Docker的守护进程运行在主机上。通过Socket从客户端访问。

DockerService接收到DockerClient的命令，就会执行这个命令。

![image-20210314230606493](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314230606493.png)

**Docker为什么比VM快**

- Docker有着比VM更少的抽象层。
- Docker利用的是宿主机的内核，VM需要guest os。

![img](https://upload-images.jianshu.io/upload_images/2338406-7c5c214656b58749.png?imageMogr2/auto-orient/strip|imageView2/2/w/1140/format/webp)

所以说，新建一个容器的时候，docker不需要像VM一样重新加载一个操作系统内核，避免引导。虚拟机是加载guest os，而docker是利用宿主机的操作系统，省去了这个复杂的过程。

![image-20210314230904938](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210314230904938.png)



### 2、Docker的常用命令

#### 2.1 帮助命令

```shell
docker version  # 显示docker的版本信息
docker info     # 显示docker的系统信息，包括容器和镜像的数量
docker --help   # 帮助命令
```

也可以参考官方的文档命令：https://docs.docker.com/reference/#command-line-interfaces-clis

#### 2.2 镜像命令

##### 2.2.1 docker images 

列出本地所有镜像

```shell
[root@ ~]#: docker images
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
hello-world   latest    d1165f221234   9 days ago   13.3kB

# REPOSITORY: 镜像的仓库源
# TAG: 镜像的标签
# IMAGE ID: 镜像的id
# CREATED: 镜像的创建时间
# SIZE: 镜像的大小

[root@ ~]#: docker images --help

Usage:  docker images [OPTIONS] [REPOSITORY[:TAG]]

List images

Options:
  -a, --all             Show all images (default hides intermediate images)
      --digests         Show digests
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print images using a Go template
      --no-trunc        Don't truncate output
  -q, --quiet           Only show image IDs
```

##### 2.2.2 docker search 

搜索镜像

![image-20210315224534134](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210315224534134.png)

```shell
[root@ ~]#: docker search --help

Usage:  docker search [OPTIONS] TERM

Search the Docker Hub for images

Options:
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print search using a Go template
      --limit int       Max number of search results (default 25)
      --no-trunc        Don't truncate output

# 搜索start数量大于5000的镜像
[root@ ~]#: docker search mysql --filter=STARS=5000   
NAME      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql     MySQL is a widely used, open-source relation…   10612     [OK]

```

##### 2.2.3 docker pull  

下载镜像

```shell
[root@ ~]#: docker pull --help

Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Pull an image or a repository from a registry

Options:
  -a, --all-tags                Download all tagged images in the repository
      --disable-content-trust   Skip image verification (default true)
      --platform string         Set platform if server is multi-platform capable
  -q, --quiet                   Suppress verbose output

[root@ ~]#: docker pull mysql
Using default tag: latest   # 不知道版本的话，默认版本是最新版latest
latest: Pulling from library/mysql
a076a628af6f: Pull complete  # 分层下载，docker image的核心，联合文件系统
f6c208f3f991: Pull complete
88a9455a9165: Pull complete
406c9b8427c6: Pull complete
7c88599c0b25: Pull complete
25b5c6debdaf: Pull complete
43a5816f1617: Pull complete
1a8c919e89bf: Pull complete
9f3cf4bd1a07: Pull complete
80539cea118d: Pull complete
201b3cad54ce: Pull complete
944ba37e1c06: Pull complete
Digest: sha256:feada149cb8ff54eade1336da7c1d080c4a1c7ed82b5e320efb5beebed85ae8c  # 签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest  # 镜像的真实地址，等价于docker pull docker.io/library/mysql:latest

[root@ ~]#: docker pull mysql:5.7
5.7: Pulling from library/mysql   # 指定5.7版本下载
a076a628af6f: Already exists  # 可以共用，已经下载的就不会再下载
f6c208f3f991: Already exists
88a9455a9165: Already exists
406c9b8427c6: Already exists
7c88599c0b25: Already exists
25b5c6debdaf: Already exists
43a5816f1617: Already exists
1831ac1245f4: Pull complete
37677b8c1f79: Pull complete
27e4ac3b0f6e: Pull complete
7227baa8c445: Pull complete
Digest: sha256:b3d1eff023f698cd433695c9506171f0d08a8f92a0c8063c1a4d9db9a55808df
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7

[root@ ~]#: docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    d1165f221234   9 days ago    13.3kB
mysql         5.7       a70d36bc331a   7 weeks ago   449MB
mysql         latest    c8562eaf9d81   7 weeks ago   546MB
```

##### 2.2.4 docker rmi

删除镜像

```shell
[root@ ~]#: docker rmi --help

Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images

Options:
  -f, --force      Force removal of the image
      --no-prune   Do not delete untagged parents

[root@ ~]#: docker rmi -f IMAGE ID   # 删除指定id的镜像 
[root@ ~]#: docker rmi -f IMAGE ID IMAGE ID IMAGE ID    # 删除多个指定id的镜像 
[root@ ~]#: docker rmi -f $(docker images -aq)   # 删除所有的镜像
```

#### 2.3 容器命令

**有了镜像，才可以创建容器。**下载一个centos的镜像进行学习。

```shell
docker pull centos
```

##### 2.3.1 新建容器并启动

```shell
docker run [可选参数] image

# 参数说明
--name = "name"  # 容器的名字  tomcat01，tomcat02，用来区分容器
-d               # 后台方式运行
-it              # 使用交互方式运行，进入容器查看内容
-p               # 指定容器的端口
	-p ip:主机端口:容器端口
	-p 主机端口:容器端口（常用）
    -p 容器端口
    容器端口
-P  # 随机指定端口

# 以交互方式启动容器
[root@ ~]#: docker run -it centos /bin/bash
[root@ca6ba4820f8f /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

# 退出容器
[root@ca6ba4820f8f /]# exit
exit
```

##### 2.3.2 列出所有运行的容器

```shell
docker ps   # 列出当前正在运行的容器
-a  # 列出所有容器，包括正在运行的和曾经运行的
-n=?  # 显示最近创建的?个容器
-q    # 只显示容器的编号

[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@ ~]#: docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS                          PORTS     NAMES
27d4179559d6   centos         "/bin/bash"   2 minutes ago   Exited (0) About a minute ago             beautiful_bardeen
a3924479b852   centos         "/bin/bash"   4 minutes ago   Exited (0) 3 minutes ago                  condescending_colden
ca6ba4820f8f   centos         "/bin/bash"   4 minutes ago   Exited (0) 4 minutes ago                  angry_jones
9806ba877da7   d1165f221234   "/hello"      3 days ago      Exited (0) 3 days ago                     nervous_faraday
8c7ad6faa5d4   d1165f221234   "/hello"      3 days ago      Exited (0) 3 days ago                     nostalgic_pasteur

```

##### 2.3.3 退出容器

```shell
exit   # 容器停止并退出
Ctrl + P + Q   # 容器不停止退出
```

##### 2.3.4 删除容器

```shell
docker rm 容器id   # 删除某个容器，但不能删除正在运行中的容器，强制删除使用rm -f
docker rm -f $(docker ps -aq)   # 删除所有容器
```

##### 2.3.5 启动和停止容器

```shell
docker start 容器id    # 启动容器
docker restart 容器id  # 重启容器
docker stop 容器id     # 停止容器
docker kill 容器id     # 强制停止当前容器
```

#### 2.4 其他常用命令

##### 2.4.1 后台启动容器

```shell
docker run -d 镜像名称

[root@ ~]#: docker run -d centos
f66e178b45ff7ca8a504a814841e57763bae1beedaa6433da004dfc9a9c747a5
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# 使用后台方式运行容器后，docker ps发现并没有正在运行的容器。原因是docker容器使用后台运行，就必须要有一个前台进程，不然docker发现没有应用，就会自动停止。
```

##### 2.4.2 查看日志

```shell
# 后台启动容器，同时每秒打印一次CodeTiger
[root@ ~]#: docker run -d centos /bin/bash -c "while true;do echo CodeTiger;sleep 1;done"
da4eab79a9c46486dc9bec10e384aca941ad0501cc3f64aaca80aed138a1f66f
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
da4eab79a9c4   centos    "/bin/bash -c 'while…"   4 seconds ago   Up 3 seconds             condescending_clarke

# 显示日志
[root@ ~]#: docker logs -tf --tail 10 da4eab79a9c4
2021-03-18T13:14:09.160931683Z CodeTiger
2021-03-18T13:14:10.162581267Z CodeTiger
2021-03-18T13:14:11.164348373Z CodeTiger
2021-03-18T13:14:12.166027616Z CodeTiger
2021-03-18T13:14:13.167761562Z CodeTiger
2021-03-18T13:14:14.169477290Z CodeTiger
2021-03-18T13:14:15.171136110Z CodeTiger
2021-03-18T13:14:16.172875315Z CodeTiger
2021-03-18T13:14:17.174586497Z CodeTiger
2021-03-18T13:14:18.176378839Z CodeTiger
2021-03-18T13:14:19.177982611Z CodeTiger
2021-03-18T13:14:20.179750901Z CodeTiger
2021-03-18T13:14:21.181485704Z CodeTiger
```

##### 2.4.3 查看容器中进程信息

```shell
[root@ ~]#: docker top 7efd96c256a1
UID           PID           PPID                C                   STIME               TTY  root         7488           7455                0                   21:18               ?    root         7558           7488                0                   21:19               ?   

```

##### 2.4.4 查看镜像的元数据

```shell
[root@ ~]#: docker inspect 7efd96c256a1
[
    {
        "Id": "7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be",
        "Created": "2021-03-18T13:18:56.635919677Z",
        "Path": "/bin/bash",
        "Args": [
            "-c",
            "while true;do echo CodeTiger;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 7488,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-03-18T13:18:56.987106052Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
        "ResolvConfPath": "/var/lib/docker/containers/7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be/hostname",
        "HostsPath": "/var/lib/docker/containers/7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be/hosts",
        "LogPath": "/var/lib/docker/containers/7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be/7efd96c256a1b5ab1ce03364043e92f4782ab3779dbec6c29c042e7ca0fe70be-json.log",
        "Name": "/frosty_goldwasser",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/26b5063329fc677502adff59ba9f01ff9de86a115570d5df9bac08786f8bd120-init/diff:/var/lib/docker/overlay2/25cdc25ed53f1d4ad8a5a7c76f8771e5ca13bb7e38ed7c9d6aafd552e217a88b/diff",
                "MergedDir": "/var/lib/docker/overlay2/26b5063329fc677502adff59ba9f01ff9de86a115570d5df9bac08786f8bd120/merged",
                "UpperDir": "/var/lib/docker/overlay2/26b5063329fc677502adff59ba9f01ff9de86a115570d5df9bac08786f8bd120/diff",
                "WorkDir": "/var/lib/docker/overlay2/26b5063329fc677502adff59ba9f01ff9de86a115570d5df9bac08786f8bd120/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "7efd96c256a1",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash",
                "-c",
                "while true;do echo CodeTiger;sleep 1;done"
            ],
            "Image": "centos",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20201204",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "84e2d81f86f2a4e3829328b0073b6e53144d8eb89d6e7bc552a6d3c8f1154647",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/84e2d81f86f2",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "3143e16381a426a1035ad09703212c668bf1e948635d9608a37be442745ded94",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "2718fe2feb075c9b748868e931a886193017c91c66843790ba2d728a2a77e919",
                    "EndpointID": "3143e16381a426a1035ad09703212c668bf1e948635d9608a37be442745ded94",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

##### 2.4.5 进入当前正在运行的容器

```shell
# 方式一，至少要有两个参数
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
[root@ ~]#: docker exec -it 2bf59a1d4601 /bin/bash
[root@2bf59a1d4601 /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

# 方式二
docker attach [OPTIONS] CONTAINER
[root@ ~]#: docker attach 2bf59a1d4601

# 方式一进入容器后开启一个新的终端，可以在里面操作（常用）
# 方式二进入容器正在执行的终端，不会启动新的进程。
```

##### 2.4.6 从容器内拷贝文件到主机上

```shell
docker cp 容器id:容器内路径 目标路径

[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@ ~]#: docker run -it centos

# ctrl + P + Q退出容器，但保持容器运行
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
880f454bd93d   centos    "/bin/bash"   21 seconds ago   Up 20 seconds             jolly_poitras
[root@ ~]#: ls
ctags  jenkins  os

# 重新进入容器
[root@ ~]#: docker attach 880f454bd93d
[root@880f454bd93d /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@880f454bd93d /]# cd home
[root@880f454bd93d home]# ls
[root@880f454bd93d home]# vi test.txt
[root@880f454bd93d home]# ls
test.txt
[root@880f454bd93d home]# exit
exit
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@ ~]#: docker cp 880f454bd93d:/home/test.txt /root
[root@ ~]#: ls
ctags  jenkins  os  test.txt
[root@ ~]#: vi test.txt

# docker cp是手动拷贝的过程，使用 -v 卷的技术，可以实现自动同步数据。
```

##### 2.4.7 小结

![image-20210318225725321](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210318225725321.png)

```shell
  attach      Attach local standard input, output, and error streams to a running container
  #当前shell下 attach连接指定运行的镜像
  build       Build an image from a Dockerfile # 通过Dockerfile定制镜像
  commit      Create a new image from a container's changes #提交当前容器为新的镜像
  cp          Copy files/folders between a container and the local filesystem #拷贝文件
  create      Create a new container #创建一个新的容器
  diff        Inspect changes to files or directories on a container's filesystem #查看docker容器的变化
  events      Get real time events from the server # 从服务获取容器实时时间
  exec        Run a command in a running container # 在运行中的容器上运行命令
  export      Export a container's filesystem as a tar archive #导出容器文件系统作为一个tar归档文件[对应import]
  history     Show the history of an image # 展示一个镜像形成历史
  images      List images #列出系统当前的镜像
  import      Import the contents from a tarball to create a filesystem image #从tar包中导入内容创建一个文件系统镜像
  info        Display system-wide information # 显示全系统信息
  inspect     Return low-level information on Docker objects #查看容器详细信息
  kill        Kill one or more running containers # kill指定docker容器
  load        Load an image from a tar archive or STDIN #从一个tar包或标准输入中加载一个镜像[对应save]
  login       Log in to a Docker registry #
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes
```

#### 2.5 作业

> **实战---部署一个nginx**

**（1）搜索镜像**

```shell
docker search nginx
```

**（2）下载镜像**

```shell
docker pull nginx
```

**（3）启动容器测试**

```shell
[root@ ~]#: docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f6d0b4767a6c   2 months ago   133MB
centos       latest    300e315adb2f   3 months ago   209MB

# -d  后台运行
# --name  指定容器的名称
# -p 宿主机端口:容器内部端口
[root@ ~]#: docker run -d --name nginx01 -p 8888:80 nginx
befa8275ea7da23018af54639af8f6bb6984562820ebab2ec1b0bf858198e614
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
befa8275ea7d   nginx     "/docker-entrypoint.…"   3 seconds ago   Up 2 seconds   0.0.0.0:8888->80/tcp   nginx01
[root@ ~]#: curl localhost:8888
```

**遇到问题了**

```shell
[root@ ~]#: docker run -d --name nginx01 -p 8888:80 nginx
0db91c62b8568b9fb4071fefe97e87238af68802b523297d78a9793dd9f11e72
docker: Error response from daemon: driver failed programming external connectivity on endpoint nginx01 (94c83de32bbae1f38b6260638be5882b3a452513ef2352937290d67ec003a1ab):  (iptables failed: iptables --wait -t nat -A DOCKER -p tcp -d 0/0 --dport 8888 -j DNAT --to-destination 172.17.0.2:80 ! -i docker0: iptables: No chain/target/match by that name.
 (exit status 1)).
```

重启docker解决

```shell
[root@ ~]#: systemctl restart docker
```

这里映射到服务器8888端口后，发现通过浏览器无法访问。

首先要在服务器的防火墙开启8888端口

```shell
# 照着复制一行改成8888端口
[root@ ~]#: vi /etc/sysconfig/iptables
# 重启防火墙
[root@ ~]#: service iptables restartd
```

做完上面的这步还不行，还需要去阿里云把服务器的8888端口打开就能正常访问了。

![image-20210318234955625](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210318234955625.png)

> **实战---部署一个tomcat**

```shell
# 根据官方文档，有下面的用法
docker run -it --rm docker:9.0
-it  # 交互方式运行
--rm  # 用完就是删除镜像，这里启动完tomcat后就会删除镜像，一般用来测试

[root@ ~]#: docker pull tomcat:9.0
[root@ ~]#: docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
tomcat       9.0       040bdb29ab37   2 months ago   649MB
nginx        latest    f6d0b4767a6c   2 months ago   133MB
centos       latest    300e315adb2f   3 months ago   209MB

# 启动tomcat镜像，使用浏览器访问404
[root@ ~]#: docker run -d -p 8888:8080 --name tomcat02 tomcat:9.0

# 进入正在运行的容器，发现tomcat的webapps目录下面是空的，所以访问出现404
[root@ ~]#: docker exec -it 7c1a30039eba /bin/bash
root@7c1a30039eba:/usr/local/tomcat# ls
BUILDING.txt     LICENSE  README.md      RUNNING.txt  conf  logs            temp     webapps.dist
CONTRIBUTING.md  NOTICE   RELEASE-NOTES  bin          lib   native-jni-lib  webapps  work
root@7c1a30039eba:/usr/local/tomcat# cd webapps
root@7c1a30039eba:/usr/local/tomcat/webapps# ls
root@7c1a30039eba:/usr/local/tomcat/webapps#

# 把webapps.dist下面的文件夹全部拷贝到webapps下面，再访问就正常了。
root@7c1a30039eba:/usr/local/tomcat# cd webapps.dist/
root@7c1a30039eba:/usr/local/tomcat/webapps.dist# ls
ROOT  docs  examples  host-manager  manager
root@7c1a30039eba:/usr/local/tomcat/webapps.dist# cd ..
root@7c1a30039eba:/usr/local/tomcat# cp -r webapps.dist/* webapps

# 出现这种现象是因为，阿里云镜像默认是最小的可运行的镜像，其他不必要的都被剔除掉。
```

![image-20210319230558860](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210319230558860.png)

> **实战---部署ES + Kibana**

```shell
# 1、es暴露的端口很多
# 2、es十分耗内存
# 3、es的数据一般要放到安全目录挂载

# 启动elasticsearch   --net somenetwork  网络配置
docker run -d --name elasticsearch01 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:tag

# 按照上面的命令直接启动会很卡，因为服务器只有1核2G，所以需要加上-e参数修改配置文件，增加内存的限制（限制es运行内存在64M到512M之间）
docker run -d --name elasticsearch01 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx512m" elasticsearch:7.6.2

# 测试启动成功
[root@ ~]#: curl localhost:9200
{
  "name" : "c65463179994",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "MrIl9p3BT_-8N6ZKw6QodQ",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
    "build_date" : "2020-03-26T06:34:37.794943Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

[root@ ~]#: docker stats c65463179994
```

![](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210320100645708.png)

使用kibana连接es，网络如何才能连接过去？

![img](https://i.loli.net/2021/01/27/XrG142kUCQMVnZx.png?d=1616234493438)

### 3、Docker镜像讲解

#### 3.1 镜像是什么

镜像是一种轻量级的可执行的软件包，用来打包软件运行的环境和基于运行环境开发的软件。它包含软件运行所需要的全部内容，包括代码、依赖库、环境变量、配置文件。

所有的应用，直接打包docker镜像，就可以直接运行。

**如何得到镜像**：

- 从远程仓库下载
- 朋友拷贝给你
- 自己制作一个镜像 DockerFile

#### 3.2 Docker镜像加载原理

> UnionFS（联合文件系统）

UnionFS（联合文件系统）是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下。Union文件系统是Docker镜像的基础。镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。

特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录。

> Docker镜像加载原理

bootfs(file system) 主要包含bootloader和kernel，boot加载器主要是引导加载内核，linux刚启动时会加载bootfs文件系统，在Docker镜像的最底层是bootfs。这一层与我们典型Linux/Unix系统是一样的，包含boot加载器和内核。当boot加载完成之后整个内核就在内存中了，此时内存使用权已有bootfs转交给内核，此时系统会卸载bootfs。

rootfs(root file system)是bootfs之上，包含的就是典型的Linux系统中的/dev、/proc、/bin、/etc等标准目录和文件。
rootfs就是各种不同操作系统发行版，比如Ubuntu,Centos等等。

![img](https://i.loli.net/2021/01/24/OPUwEy8cHLkl4Iv.png?d=1616249572216)

平时我们安装到虚拟机的centos都是好几个G，在docker里却只有几百兆。对于一个精简的os，rootfs可以很小，只需要包含最基本的命令、工具和程序库就可以了。因为底层直接用Host的kernel，自己只需要提供rootfs就可以了。

由此可见对于Linux的不同发行版，bootfs基本都是一样的，rootfs会有差别，因此不同发行版可以公用bootfs.

虚拟机是分钟级别，容器是秒级！

#### 3.3 分层理解

```shell
[root@ ~]#: docker image inspect nginx:latest
[
    {
        "Id": "sha256:f6d0b4767a6c466c178bf718f99bea0d3742b26679081e52dbf8e0c7c4c42d74",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:10b8cc432d56da8b61b070f4c7d2543a9ed17c2b23010b43af434fd40e2ca4aa"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2021-01-12T10:17:41.649267496Z",
        "Container": "faa742a137cfbf261402d359c09203c3fd894fa49689e4f4952a657ea80d9107",
        "ContainerConfig": {
            "Hostname": "faa742a137cf",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.19.6",
                "NJS_VERSION=0.5.0",
                "PKG_RELEASE=1~buster"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:a5531bdc09faaa444e565e6f9ec98ed4474970ed6fdd5db6b8b255534b220689",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "DockerVersion": "19.03.12",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.19.6",
                "NJS_VERSION=0.5.0",
                "PKG_RELEASE=1~buster"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:a5531bdc09faaa444e565e6f9ec98ed4474970ed6fdd5db6b8b255534b220689",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 132951424,
        "VirtualSize": 132951424,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e1c8267af463488b12de060a222683a5d829aa29945c420e3b3f3491541f97a9/diff:/var/lib/docker/overlay2/82c9a075fecc94616d441120396b56dcc441b1c52a9660298afa9b6379ea7fe1/diff:/var/lib/docker/overlay2/06587896b2e0d3401dccf6362dabba6ea235522ac11a25934dcb96c8380a8c19/diff:/var/lib/docker/overlay2/0c995d62818ad5e415fd881cc1bd5ceb03fd9406d7dd623cfef684c7732f6cbf/diff",
                "MergedDir": "/var/lib/docker/overlay2/71c8debfe1eaed94a111fa2002686ba5c8d7afac3e459a05efe9ef3aa162fb33/merged",
                "UpperDir": "/var/lib/docker/overlay2/71c8debfe1eaed94a111fa2002686ba5c8d7afac3e459a05efe9ef3aa162fb33/diff",
                "WorkDir": "/var/lib/docker/overlay2/71c8debfe1eaed94a111fa2002686ba5c8d7afac3e459a05efe9ef3aa162fb33/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:cb42413394c4059335228c137fe884ff3ab8946a014014309676c25e3ac86864",
                "sha256:1c91bf69a08b515a1f9c36893d01bd3123d896b38b082e7c21b4b7cc7023525a",
                "sha256:56bc37de0858bc2a5c94db9d69b85b4ded4e0d03684bb44da77e0fe93a829292",
                "sha256:3e5288f7a70f526d6bceb54b3568d13c72952936cebfe28ddcb3386fe3a236ba",
                "sha256:85fcec7ef3efbf3b4e76a0f5fb8ea14eca6a6c7cbc0c52a1d401ad5548a29ba5"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```

上面可以查看nginx镜像的元数据，它的分层结构如下

```shell
"Layers": [
                "sha256:cb42413394c4059335228c137fe884ff3ab8946a014014309676c25e3ac86864",
                "sha256:1c91bf69a08b515a1f9c36893d01bd3123d896b38b082e7c21b4b7cc7023525a",
                "sha256:56bc37de0858bc2a5c94db9d69b85b4ded4e0d03684bb44da77e0fe93a829292",
                "sha256:3e5288f7a70f526d6bceb54b3568d13c72952936cebfe28ddcb3386fe3a236ba",
                "sha256:85fcec7ef3efbf3b4e76a0f5fb8ea14eca6a6c7cbc0c52a1d401ad5548a29ba5"
            ]
```

每次pull命令下载镜像时，都可以看到是分层下载的，比如一个redis7包含7层（Layer），当下载redis8的时候可能只需要下载最新的三层，redis7用的层不需要重新下载。

所有的Docker镜像都起始于一个基础镜像层，当进行修改或增加新的内容时，就会在当前镜像层之上，创建新的镜像层。

比如基于ubuntu16.04创建一个新的镜像，这就是镜像的第一层，如果在该镜像中添加python包，就会在基础镜像之上创建第二个镜像层，如果继续添加一个安全补丁，就会创建第三个镜像层。

![image](https://i.loli.net/2021/01/28/R1Y5wrVhynZvDEc.jpg)

在添加额外的镜像层的同时，镜像始终保持是当前所有镜像的组合。

![image](https://i.loli.net/2021/01/28/sOvuj2GaPMQWJLD.jpg)

上图中文件7是对文件5的修改，在打包镜像的时候，上层镜像层中的文件覆盖了底层镜像层中的文件。这样就使得文件的更新版本作为一个新镜像层添加到镜像当中。

![image](https://i.loli.net/2021/01/28/EDAC5gXNiupm61P.jpg)

比如文件1是mysql，文件2是redis，文件3是tomcat，文件4是maven，文件6是jdk，文件5是我们之间的app1，文件7是app2，那么第一层的三个文件和第二层的两个文件，都是可以被其他镜像共用的。

**docker镜像都是只读的，当容器启动时，一个新的可写层被加载到镜像的顶部。这一层就是我们通常说的容器层，容器之下的都叫镜像层。**

Docker 通过存储引擎（新版本采用快照机制）的方式来实现镜像层堆栈，并保证多镜像层对外展示为统一的文件系统。

![image](https://i.loli.net/2021/01/28/Yr5SOHKwhCsoUxD.jpg)

#### 3.4 commit镜像

```shell
docker commit  # 提交容器成为一个新的副本

# 和git命令类似
docker commit -m="提交的描述信息" -a="作者" 容器id 目标镜像名:[TAG]
```

```shell
# 1、启动tomcat
[root@ ~]#: docker run -d -p 8888:8080 tomcat:9.0
# 2、发现这个默认的tomcat，webapps目录为空，官方默认是没有的。
# 3、从webapps.dist把文件拷贝到webapps下面。
# 4、将我们修改过的容器通过commit提交为一个镜像。
[root@ ~]#: docker commit -a="CodeTiger" -m="add webapps files" 32ee94047743 mytomcat:1.0
sha256:2d15b087fbf776cfc7c8e3c1d11fde2c6605efcb6c5c034df05db83be2d78e42
[root@ ~]#: docker images
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
mytomcat        1.0       2d15b087fbf7   14 seconds ago   654MB
tomcat          9.0       040bdb29ab37   2 months ago     649MB
tomcat          latest    040bdb29ab37   2 months ago     649MB
nginx           latest    f6d0b4767a6c   2 months ago     133MB
centos          latest    300e315adb2f   3 months ago     209MB
elasticsearch   7.6.2     f29a1ee41030   11 months ago    791MB
```

![image-20210320232618673](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210320232618673.png)

### 4、容器数据卷

#### 4.1 什么是容器数据卷

将应用和数据打包成一个镜像后，数据都在容器中，那么如果容器被删除了，数据都会丢失？

<font color='red'>需求：数据可以持久化</font>

容器之间有一个数据共享的技术，docker容器中产生的数据，可以同步到本地，这就是**卷技术**。其实就是将容器内的目录，挂载到Linux上。

![image-20210320234231388](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210320234231388.png)

总结一句话：**容器的持久化和同步操作，容器间也是可以数据共享的。**

#### 4.2 使用数据卷

> 直接使用命令来挂载 -v

```shell
docker run -it -v 主机目录:容器内目录
```

```shell
# 启动容器，可以发现在主机上的root文件夹下会自动创建一个ceshi目录
[root@ ~]#: docker run -it -v /root/ceshi:/root centos

# 查看镜像的元数据信息，可以发现挂载信息
[root@ ~]#: docker inspect d245ea321c52
```

![image-20210321111455031](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210321111455031.png)

如果你在容器内`/root`目录下新建、删除和修改文件，都会自动同步到主机的`/root/ceshi`目录下，反之也是这样。

如果停止容器，在主机上对`/root/ceshi`进行操作，也会自动同步到容器内。

需要占用两倍的存储。

如果容器删除了，主机上的文件不会被删除。

#### 4.3 实战---安装MySQL

```shell
# 下载mysql
[root@ ~]#: docker pull mysql:5.7

# $ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
# 上面是文档中的启动命令，因为mysql在启动的时候需要设置密码

# 启动mysql，并且挂载相应的目录到主机
[root@ ~]#: docker run -d -p 8888:3306 --name mysql01 -e MYSQL_ROOT_PASSWORD=123456 -v /root/mysql/conf:/etc/mysql/conf.d -v /root/mysql/data:/var/lib/mysql mysql:5.7
9ae2bbcf9698d020d0c757e8f24d106d230dbe52eee25e8b1372852855519411
[root@ ~]#: docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                               NAMES
9ae2bbcf9698   mysql:5.7   "docker-entrypoint.s…"   3 seconds ago   Up 3 seconds   33060/tcp, 0.0.0.0:8888->3306/tcp   mysql01

```

![image-20210321142909963](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210321142909963.png)

使用navicat测试，可以发现能够连接成功，说明容器正常启动。

```shell
[root@ data]#: ls
auto.cnf    ca.pem           client-key.pem  ibdata1      ib_logfile1  mysql               private_key.pem  server-cert.pem  sys
ca-key.pem  client-cert.pem  ib_buffer_pool  ib_logfile0  ibtmp1       performance_schema  public_key.pem   server-key.pem
[root@ data]#: pwd
/root/mysql/data
```

主机上`/root/mysql/data`已经有数据了。新建数据库`test`，在主机上也会多出相应的文件夹。

![image-20210321143125451](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210321143125451.png)

**删除该容器，主机上的数据也不会丢失。**

#### 4.4 具名挂载和匿名挂载

```shell
# 匿名挂载
-v 容器内路径

[root@ containers]#: docker run -d -P --name nginx01 -v /etc/nginx nginx
75d2adf36331a5bc596ba713995da5ad8a473b21d3e988e4659c43560a7bbe7e

# 查看所有的volume
[root@ containers]#: docker volume ls
DRIVER    VOLUME NAME
local     ea6cfaf28a9f7e242a20ea6d5f44637cac3526c17124929a6abdb61a2b03fec4

# 具名挂载
-v 卷名:容器内路径

[root@ containers]#: docker run -d -P --name nginx02 -v test-nginx:/etc/nginx nginx
b0f04bf78b458bfd57919e304a777bc7d60622bf5039f6217aa298671ec69602

[root@ containers]#: docker volume ls
DRIVER    VOLUME NAME
local     ea6cfaf28a9f7e242a20ea6d5f44637cac3526c17124929a6abdb61a2b03fec4
local     test-nginx

# 查看这个卷的情况
[root@ containers]#: docker volume inspect test-nginx
[
    {
        "CreatedAt": "2021-03-21T20:42:19+08:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/test-nginx/_data",
        "Name": "test-nginx",
        "Options": null,
        "Scope": "local"
    }
]
```

没有指定目录的情况下，所有的卷都在默认目录`/var/lib/docker/volumes`下面。

```shell
# 如何确定是具名挂载、匿名挂载还是指定路径挂载
-v 容器内路径  # 匿名挂载
-v 卷名:容器内路径  # 具名挂载
-v /主机路径:容器内路径  # 指定路径挂载
```

```shell
# 通过-v 容器内路径:ro/rw 改变读写权限
ro readonly  只读，指定这个权限，则只能通过宿主机来操作，容器内无法操作
rw readwrite  读写

docker run -d -P --name nginx02 -v test-nginx:/etc/nginx:ro nginx
docker run -d -P --name nginx02 -v test-nginx:/etc/nginx:rw nginx
```

#### 4.5 使用Dockerfile挂载卷

**dockerfile是用来构建docker镜像的构建文件。**通过这个脚本可以生成镜像，前面提到过，镜像是一层层的，所以dockerfile里每个命令都是一层。

```shell
# dockerfile文件
# 文件中的内容  指令（大写） 参数
FROM centos

VOLUME ["volume01", "volume02"]

CMD echo "------end------"

CMD /bin/bash

# 这里的每个命令，就是镜像的一层
```

```shell
# 使用dockerfile构建镜像
[root@ docker-test-volumes]#: docker build -f /root/docker-test-volumes/dockerfile -t lxp/centos:1.0 .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM centos
 ---> 300e315adb2f
Step 2/4 : VOLUME ["volume01", "volume02"]
 ---> Running in 42feeb883dde
Removing intermediate container 42feeb883dde
 ---> 3d1b02a793b6
Step 3/4 : CMD echo "------end-------"
 ---> Running in ecf5f1691930
Removing intermediate container ecf5f1691930
 ---> 921f72319b7e
Step 4/4 : CMD /bin/bash
 ---> Running in 0c1f62a71993
Removing intermediate container 0c1f62a71993
 ---> 206e8d77f602
Successfully built 206e8d77f602
Successfully tagged lxp/centos:1.0
```

![image-20210322223110545](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210322223110545.png)

```shell
# 启动自己写的容器
[root@ docker-test-volumes]#: docker run -it 206e8d77f602 /bin/bash
```

![image-20210322223323436](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210322223323436.png)

`volume01`和`volume02`是生成镜像的时候自动挂载的。

```shell
docker inspect e25d51423840   # 查看容器的元数据
```

![image-20210322223701099](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210322223701099.png)

可以发现是匿名挂载，在宿主机上对应的目录是`/var/lib/docker/volumes`。

尝试在容器内`volume01`文件夹下创建一个文件`test.txt`。退出容器进入宿主机对应的目录下，发现也有对应的`test.txt`，说明实现了数据同步。

#### 4.6 数据卷容器

多个容器同步数据。

![image-20210322230433152](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210322230433152.png)

```shell
# 启动一个容器
docker run -it --name centos01 lxp/centos:1.0
# 启动另一个容器 --volumes-from和centos01进行数据同步
docker run -it --name centos02 --volumes-from centos01 lxp/centos:1.0
docker run -it --name centos03 --volumes-from centos01 lxp/centos:1.0
```

![image-20210322230603448](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210322230603448.png)

删除docker01后，docker02和docker03的数据还在。

多个mysql实现数据共享

```shell
docker run -d -p 8888:3306 --name mysql01 -e MYSQL_ROOT_PASSWORD=123456 -v /etc/mysql/conf.d -v /var/lib/mysql mysql:5.7

docker run -d -p 8888:3306 --name mysql02 -e MYSQL_ROOT_PASSWORD=123456 --volumes-from mysql01 mysql:5.7
```

**结论**

容器之间配置信息的传递，数据卷容器的生命周期一直持续到没有容器使用为止。

但是一旦持久化到本地，本地的数据就不会被删除。

### 5、Dockerfile

#### 5.1 Dockerfile介绍

dockerfile是用来构建docker镜像的文件。

构建步骤：

（1）编写dockerfile文件。

（2）docker build构建一个镜像。

（3）docker run运行镜像。

（4）docker push发布镜像（阿里云镜像仓库、DockerHub）。

![image-20210323222106955](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323222106955.png)

![image-20210323222137310](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323222137310.png)

#### 5.2 Dockerfile构建过程

**基础知识**

（1）每个保留关键字（指令）都必须是大写字母。

（2）从上到下顺序执行。

（3）# 表示注释。

（4）每一个指令都会创建一个新的镜像层并提交。

![image-20210323222601979](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323222601979.png)

**Dockerfile**：构建文件，定义了一切步骤和源代码。

**DockerImages**：通过dockerfile构建生成的镜像，最终发布和运行的产品。

**Docker容器**：镜像运行起来后，容器提供服务。

#### 5.3 Dockerfile指令

```shell
FROM         # 基础镜像
MAINTAINER   # 镜像是谁写的，姓名 + 邮箱
RUN          # 镜像构建的时候需要运行的命令
ADD          # 在基础镜像上添加其他的文件
WORKDIR      # 镜像的工作目录
VOLUME       # 挂载的目录
EXPOSE       # 镜像对外暴露的端口
CMD          # 指定这个镜像启动的时候需要运行的命令，只有最后一个命令会生效，可被替代
ENTRYPOINT   # 指定这个镜像启动的时候需要运行的命令，可以追加命令
ONBUILD      # 当容器继承的时候，就会运行ONBUILD指令，触发指令。
COPY         # 类似ADD，将文件拷贝到镜像中
ENV          # 构建镜像的时候设置环境变量
```



![image-20210323224256825](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323224256825.png)

#### 5.4 CMD和ENTRYPOINT的区别

测试CMD命令

```shell
# dockerfile文件的内容
FROM centos
CMD ["ls", "-a"]

# 构建镜像
[root@ docker-test]#: docker build -f /root/docker-test/dockerfile-cmd -t cmd-centos .
Sending build context to Docker daemon  3.072kB
Step 1/2 : FROM centos
 ---> 300e315adb2f
Step 2/2 : CMD ["ls", "-a"]
 ---> Running in b68d50fdfa81
Removing intermediate container b68d50fdfa81
 ---> 7def51550ef9
Successfully built 7def51550ef9
Successfully tagged cmd-centos:latest

# 运行镜像，执行ls -a输出当前面目录下的所有文件
[root@ docker-test]#: docker run 7def51550ef9
.
..
.dockerenv
bin
dev
etc
home
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var

# 后面跟-l参数，发现替换了ls -a，无法识别
[root@ docker-test]#: docker run 7def51550ef9 -l
docker: Error response from daemon: OCI runtime create failed: container_linux.go:367: starting container process caused: exec: "-l": executable file not found in $PATH: unknown.
```

测试ENTRYPOINT命令

```shell
# dockerfile文件的内容
FROM centos
ENTRYPOINT ["ls", "-a"]

# 构建镜像
[root@ docker-test]#: docker build -f /root/docker-test/dockerfile-entrypoint -t entrypoint-centos .
Sending build context to Docker daemon  4.096kB
Step 1/2 : FROM centos
 ---> 300e315adb2f
Step 2/2 : ENTRYPOINT ["ls", "-a"]
 ---> Running in 286618d3d1b1
Removing intermediate container 286618d3d1b1
 ---> 82ea18c35804
Successfully built 82ea18c35804
Successfully tagged entrypoint-centos:latest

# 运行镜像
[root@ docker-test]#: docker run 82ea18c35804
.
..
.dockerenv
bin
dev
etc
home
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var

# 后面使用参数-l，组合成命令ls -al
[root@ docker-test]#: docker run 82ea18c35804 -l
total 56
drwxr-xr-x  1 root root 4096 Mar 25 13:48 .
drwxr-xr-x  1 root root 4096 Mar 25 13:48 ..
-rwxr-xr-x  1 root root    0 Mar 25 13:48 .dockerenv
lrwxrwxrwx  1 root root    7 Nov  3 15:22 bin -> usr/bin
drwxr-xr-x  5 root root  340 Mar 25 13:48 dev
drwxr-xr-x  1 root root 4096 Mar 25 13:48 etc
drwxr-xr-x  2 root root 4096 Nov  3 15:22 home
lrwxrwxrwx  1 root root    7 Nov  3 15:22 lib -> usr/lib
lrwxrwxrwx  1 root root    9 Nov  3 15:22 lib64 -> usr/lib64
drwx------  2 root root 4096 Dec  4 17:37 lost+found
drwxr-xr-x  2 root root 4096 Nov  3 15:22 media
drwxr-xr-x  2 root root 4096 Nov  3 15:22 mnt
drwxr-xr-x  2 root root 4096 Nov  3 15:22 opt
dr-xr-xr-x 90 root root    0 Mar 25 13:48 proc
dr-xr-x---  2 root root 4096 Dec  4 17:37 root
drwxr-xr-x 11 root root 4096 Dec  4 17:37 run
lrwxrwxrwx  1 root root    8 Nov  3 15:22 sbin -> usr/sbin
drwxr-xr-x  2 root root 4096 Nov  3 15:22 srv
dr-xr-xr-x 13 root root    0 Mar 25 13:48 sys
drwxrwxrwt  7 root root 4096 Dec  4 17:37 tmp
drwxr-xr-x 12 root root 4096 Dec  4 17:37 usr
drwxr-xr-x 20 root root 4096 Dec  4 17:37 var
```

#### 5.5 实战

上面看了官方的构建centos镜像的dockerfile文件，第一句就是`FROM scratch`

DockerHub中99%的镜像都是从这个基础镜像开始的。

> **创建一个自己的centos**

```shell
# dockerfile文件
FROM centos
MAINTAINER CodeTiger<18252025311@163.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "-------end--------"
CMD /bin/bash
```

```shell
# 执行命令构建镜像
[root@ docker-test]#: docker build -f /root/docker-test/dockerfile -t mycentos:0.1 .

# 构建成功
Successfully built 16570f5e9ae0
Successfully tagged mycentos:0.1
```

![image-20210323233617174](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323233617174.png)

运行官方的centos镜像

![image-20210323233845101](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323233845101.png)

运行我们自己构建的镜像（基于官方的centos，加了一些东西）

![image-20210323233929783](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323233929783.png)

可以发现，我们在官方镜像的基础上，加入了`vim`和`ifconfig`命令，同时指定进入镜像后的默认目录是`/usr/local`。

可以使用`docker history 镜像id`列出本地镜像的变更历史

![image-20210323234203977](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210323234203977.png)

> **构建tomcat**

1.准备镜像文件tomcat压缩包，jdk压缩包

2.编写dockerfile文件，官方命名Dockerfile，==build时会自动寻找这个文件，就不需要-f指定了==

```shell
FROM centos
MAINTAINER CodeTiger<18252025311@163.com>

COPY readme.txt /usr/local/readme.txt

ADD jdk-15.0.2_linux-x64_bin.tar.gz /usr/local
ADD apache-tomcat-9.0.43.tar.gz /usr/local

RUN yum install -y vim

ENV MYPATH /usr/local
WORKDIR $MYPATH

ENV JAVA_HOME /usr/local/jdk-15.0.2
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.43
ENV CATALINA_BASH /usr/local/apache-tomcat-9.0.43
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

EXPOSE 8080

CMD /usr/local/apache-tomcat-9.0.43/bin/startup.sh && tail -F /usr/local/apache-tomcat-9.0.43/logs/catalina.out
```

3.构建镜像

```shell
[root@localhost tomcat]# docker build -t mytomcat .
Sending build context to Docker daemon  353.4MB
Step 1/15 : FROM centos
 ---> 300e315adb2f
Step 2/15 : MAINTAINER CodeTiger<18252025311@163.com>
 ---> Using cache
 ---> 2417b25aa69e
Step 3/15 : COPY readme.txt /usr/local/readme.txt
 ---> Using cache
 ---> 5a3b06bdbe2d
Step 4/15 : ADD jdk-15.0.2_linux-x64_bin.tar.gz /usr/local
 ---> 323152020842
Step 5/15 : ADD apache-tomcat-9.0.43.tar.gz /usr/local
 ---> 90ab12eb9304
Step 6/15 : RUN yum install -y vim
 ---> Running in d7de62a6ea46
CentOS Linux 8 - AppStream                      549 kB/s | 6.3 MB     00:11    
CentOS Linux 8 - BaseOS                         610 kB/s | 2.3 MB     00:03    
CentOS Linux 8 - Extras                         4.9 kB/s | 8.6 kB     00:01    
Last metadata expiration check: 0:00:01 ago on Sat Feb 20 20:05:27 2021.
Dependencies resolved.
================================================================================
 Package             Arch        Version                   Repository      Size
================================================================================
Installing:
 vim-enhanced        x86_64      2:8.0.1763-15.el8         appstream      1.4 M
Installing dependencies:
 gpm-libs            x86_64      1.20.7-15.el8             appstream       39 k
 vim-common          x86_64      2:8.0.1763-15.el8         appstream      6.3 M
 vim-filesystem      noarch      2:8.0.1763-15.el8         appstream       48 k
 which               x86_64      2.21-12.el8               baseos          49 k
Transaction Summary
================================================================================
Install  5 Packages
Total download size: 7.8 M
Installed size: 30 M
Downloading Packages:
(1/5): gpm-libs-1.20.7-15.el8.x86_64.rpm        121 kB/s |  39 kB     00:00    
(2/5): vim-filesystem-8.0.1763-15.el8.noarch.rp 116 kB/s |  48 kB     00:00    
(3/5): which-2.21-12.el8.x86_64.rpm              82 kB/s |  49 kB     00:00    
(4/5): vim-enhanced-8.0.1763-15.el8.x86_64.rpm  345 kB/s | 1.4 MB     00:04    
(5/5): vim-common-8.0.1763-15.el8.x86_64.rpm    465 kB/s | 6.3 MB     00:13    
--------------------------------------------------------------------------------
Total                                           531 kB/s | 7.8 MB     00:15     
warning: /var/cache/dnf/appstream-02e86d1c976ab532/packages/gpm-libs-1.20.7-15.el8.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID 8483c65d: NOKEY
CentOS Linux 8 - AppStream                      1.6 MB/s | 1.6 kB     00:00    
Importing GPG key 0x8483C65D:
 Userid     : "CentOS (CentOS Official Signing Key) <security@centos.org>"
 Fingerprint: 99DB 70FA E1D7 CE22 7FB6 4882 05B5 55B3 8483 C65D
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
Key imported successfully
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1 
  Installing       : which-2.21-12.el8.x86_64                               1/5 
  Installing       : vim-filesystem-2:8.0.1763-15.el8.noarch                2/5 
  Installing       : vim-common-2:8.0.1763-15.el8.x86_64                    3/5 
  Installing       : gpm-libs-1.20.7-15.el8.x86_64                          4/5 
  Running scriptlet: gpm-libs-1.20.7-15.el8.x86_64                          4/5 
  Installing       : vim-enhanced-2:8.0.1763-15.el8.x86_64                  5/5 
  Running scriptlet: vim-enhanced-2:8.0.1763-15.el8.x86_64                  5/5 
  Running scriptlet: vim-common-2:8.0.1763-15.el8.x86_64                    5/5 
  Verifying        : gpm-libs-1.20.7-15.el8.x86_64                          1/5 
  Verifying        : vim-common-2:8.0.1763-15.el8.x86_64                    2/5 
  Verifying        : vim-enhanced-2:8.0.1763-15.el8.x86_64                  3/5 
  Verifying        : vim-filesystem-2:8.0.1763-15.el8.noarch                4/5 
  Verifying        : which-2.21-12.el8.x86_64                               5/5 
Installed:
  gpm-libs-1.20.7-15.el8.x86_64         vim-common-2:8.0.1763-15.el8.x86_64    
  vim-enhanced-2:8.0.1763-15.el8.x86_64 vim-filesystem-2:8.0.1763-15.el8.noarch
  which-2.21-12.el8.x86_64             
Complete!
Removing intermediate container d7de62a6ea46
 ---> 1588f8d7540c
Step 7/15 : ENV MYPATH /usr/local
 ---> Running in f675d51eb669
Removing intermediate container f675d51eb669
 ---> ea3e1cf22146
Step 8/15 : WORKDIR $MYPATH
 ---> Running in ffd52af5223b
Removing intermediate container ffd52af5223b
 ---> dd7eb7695d2d
Step 9/15 : ENV JAVA_HOME /usr/local/jdk-15.0.2
 ---> Running in 083ea6aa93dc
Removing intermediate container 083ea6aa93dc
 ---> 82dd37ab242c
Step 10/15 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
 ---> Running in c7edfae89295
Removing intermediate container c7edfae89295
 ---> cff8f1250658
Step 11/15 : ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.43
 ---> Running in 52643827841a
Removing intermediate container 52643827841a
 ---> 8317bc605ce0
Step 12/15 : ENV CATALINA_BASH /usr/local/apache-tomcat-9.0.43
 ---> Running in 72d596338a7b
Removing intermediate container 72d596338a7b
 ---> d1d373868c1e
Step 13/15 : ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
 ---> Running in 973c6f7960ee
Removing intermediate container 973c6f7960ee
 ---> 517aaee5614c
Step 14/15 : EXPOSE 8080
 ---> Running in e48634333c5d
Removing intermediate container e48634333c5d
 ---> f01236ad4f1f
Step 15/15 : CMD /usr/local/apache-tomcat-9.0.43/bin/startup.sh && tail -F /usr/local/apache-tomcat-9.0.43/logs/catalina.out
 ---> Running in df10a46ade44
Removing intermediate container df10a46ade44
 ---> 3bfe8e4b7690
Successfully built 3bfe8e4b7690
Successfully tagged lnltomcat:02
```

4.启动镜像

```shell
docker run -d -p 8080:8080 --name tomcat -v /root/tomcat/test:/usr/local/apache-tomcat-9.0.43/webapps/test -v /root/tomcat/tomcatlogs/:/usr/loacl/apache-tomcat-9.0.43/logs tomcat
#为防止踩坑，请务必使用docker logs [容器ID] 来检查错误！
#踩坑1：脚本编写错误  踩坑2：jdk版本太低
```

主机上`/root/tomcat/test`和容器内`/usr/local/apache-tomcat-9.0.43/webapps/test`目录关联，这样你只需要在主机上发布更新自己的项目到`/root/tomcat/test`目录，容器内就会自动同步。

5.发布项目

```shell
[root@bogon WEB-INF]# cat /root/tomcat/test/WEB-INF/web.xml 
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                               http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
           version="2.5">
</web-app>
```

```shell
[root@bogon test]# cat /root/tomcat/test/index.jsp 
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello,lele</title>
</head>
<body>
Hello World!<br/>
<%
System.out.println("---my test---");
%>
</body>
</html>
```

然后访问：http://ip:8080/test/ 就可以访问到项目。

#### 5.6 发布镜像

> 发布镜像到Docker Hub

1、先注册Docker Hub的账号。

2、登录

```shell
[root@ ~]#: docker login -u lxp666
Password:
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

3、push自己的镜像

![image-20210326222858629](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326222858629.png)

报错，拒绝访问，**原因是push的时候需要带上自己Docker Hub的用户名，`用户名/镜像名:版本号`这样的形式**，可以为这个镜像增加一个TAG。

```shell
# 如果不指定版本号，那它会默认去找latest，找不到就报错，所以要指定版本号
[root@ docker-test]#: docker tag mycentos lxp666/mycentos
Error response from daemon: No such image: mycentos:latest

# lxp666是我的Docker Hub的名字
[root@ docker-test]#: docker tag mycentos:0.1 lxp666/mycentos:0.1
[root@ docker-test]#: docker images
REPOSITORY          TAG       IMAGE ID       CREATED              SIZE
mycentos            0.1       878f654a157a   About a minute ago   282MB
lxp666/mycentos     0.1       878f654a157a   About a minute ago   282MB
entrypoint-centos   latest    82ea18c35804   25 hours ago         209MB
cmd-centos          latest    7def51550ef9   25 hours ago         209MB
mysql               5.7       a70d36bc331a   2 months ago         449MB
tomcat              9.0       040bdb29ab37   2 months ago         649MB
tomcat              latest    040bdb29ab37   2 months ago         649MB
nginx               latest    f6d0b4767a6c   2 months ago         133MB
centos              latest    300e315adb2f   3 months ago         209MB

```

重新push，发现push的时候，也是分层上传的。

![image-20210326223943567](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326223943567.png)

![image-20210326225704027](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326225704027.png)

> 发布镜像到阿里云容器服务

1、https://cr.console.aliyun.com/cn-shanghai/instance/namespaces 。创建命名空间

![image-20210326225903128](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326225903128.png)

2、创建镜像仓库

![image-20210326230000967](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326230000967.png)

3、根据文档进行操作

![image-20210326230040669](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210326230040669.png)

#### 5.7 流程总结

![img](https://kuangstudy.oss-cn-beijing.aliyuncs.com/bbs/2021/01/25/kuangstudyc864dc47-06fd-4e46-9e58-cc98dea19472.png)

### 6、Docker网络

#### 6.1 理解Docker0

![image-20210327094938667](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327094938667.png)

docker是如何处理容器网络访问的？

![image-20210327095203318](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327095203318.png)

```shell
[root@ ~]#: docker run -d -P --name tomcat01 tomcat

# 查看容器的内部地址，eth0@if97地址的docker分配的
[root@ ~]#: docker exec -it tomcat01 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
96: eth0@if97: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

# 在本机是可以ping通的
[root@ ~]#: ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.111 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.060 ms
64 bytes from 172.17.0.2: icmp_seq=3 ttl=64 time=0.055 ms
^C
--- 172.17.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 1999ms
rtt min/avg/max/mdev = 0.055/0.075/0.111/0.026 ms

```

> 原理

1.我们每启动一个docker容器，docker就会给docker容器分配一个ip，只要安装了docker容器，就会有一个网卡docker0桥接模式，使用的技术是**veth-pair技术**。

再次测试ip addr

![image-20210327100231733](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327100231733.png)

2.再启动一个tomcat，发现又多了**一对网卡**。

```shell
[root@ ~]#: docker run -d -P --name tomcat02 tomcat
28cc9b1ece2496f764cb5043bdcc34ae8c7b696a48c744de55c8526b3bfb4cdf
[root@ ~]#: docker exec -it tomcat02 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
98: eth0@if99: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

![image-20210327100415297](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327100415297.png)

veth-pair：顾名思义，veth-pair 就是一对的虚拟设备接口，和 tap/tun 设备不同的是，它都是成对出现的。一端连着协议栈，一端彼此相连着。

正因为有这个特性，它常常充当着一个桥梁，连接着各种虚拟网络设备，典型的例子像“两个 namespace 之间的连接”，“Bridge、OVS 之间的连接”，“Docker 容器之间的连接” 等等，以此构建出非常复杂的虚拟网络结构，比如 OpenStack Neutron。

具体可查看：https://www.cnblogs.com/bakari/p/10613710.html

```shell
# tomcat02可以ping统通tomcat01，说明容器和容器之间是可以相互ping通的。
[root@ ~]#: docker exec -it tomcat02 ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.095 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.069 ms
64 bytes from 172.17.0.2: icmp_seq=3 ttl=64 time=0.064 ms
```

![image-20210327102414051](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327102414051.png)

结论：tomcat01和tomcat02是共用的一个路由器docker0。所有的容器在不指定网络的情况下，都是docker0路由，docker会给容器分配一个默认的可用ip。

> 小结

![image-20210327103003104](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327103003104.png)

docker使用的是linux的桥接，宿主机中是一个docker容器的网桥docker0。

Docker中的所有网络接口都是虚拟的，虚拟的转发效率更高。只要容器删除，对应的那对网桥也会被删除。

#### 6.2 --link

> 思考一个场景，我们编写了一个微服务，database URL=ip:，项目不重启，数据库ip换了，可以实现通过名字来访问容器吗？

```shell
[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND             CREATED          STATUS          PORTS                     NAMES
28cc9b1ece24   tomcat    "catalina.sh run"   41 minutes ago   Up 41 minutes   0.0.0.0:49156->8080/tcp   tomcat02
7ecc18123788   tomcat    "catalina.sh run"   51 minutes ago   Up 51 minutes   0.0.0.0:49155->8080/tcp   tomcat01

# 尝试使用容器名来ping，发现ping不通
[root@ ~]#: docker exec -it tomcat02 ping tomcat01
ping: tomcat01: Name or service not known
```

这里可以使用`--link`参数解决这个问题

```shell
[root@ ~]#: docker run -d -P --name tomcat03 --link tomcat02 tomcat
788c3dcb238eb5a2a52d4bec962ef0a783066e6be9aea43e4f9cf48f5a53c38e

[root@ ~]#: docker ps
CONTAINER ID   IMAGE     COMMAND             CREATED          STATUS          PORTS                     NAMES
788c3dcb238e   tomcat    "catalina.sh run"   3 seconds ago    Up 2 seconds    0.0.0.0:49157->8080/tcp   tomcat03
28cc9b1ece24   tomcat    "catalina.sh run"   44 minutes ago   Up 44 minutes   0.0.0.0:49156->8080/tcp   tomcat02
7ecc18123788   tomcat    "catalina.sh run"   54 minutes ago   Up 54 minutes   0.0.0.0:49155->8080/tcp   tomcat01

# 通过容器名，tomcat03可以ping通tomcat02
[root@ ~]#: docker exec -it tomcat03 ping tomcat02
PING tomcat02 (172.17.0.3) 56(84) bytes of data.
64 bytes from tomcat02 (172.17.0.3): icmp_seq=1 ttl=64 time=0.093 ms
64 bytes from tomcat02 (172.17.0.3): icmp_seq=2 ttl=64 time=0.065 ms

# 反向是无法ping通的
[root@ ~]#: docker exec -it tomcat02 ping tomcat03
ping: tomcat03: Name or service not known
```

> 探究出现上面这种现象的原因

![image-20210327105036689](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327105036689.png)

```shell
# 查看该网卡的信息
[root@ ~]#: docker network inspect 843b0497d70e
```

![image-20210327105328399](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327105328399.png)

![image-20210327105434271](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327105434271.png)

```shell
# 查看tomcat03的元数据信息
[root@ ~]#: docker inspect 788c3dcb238e
```

![image-20210327105637705](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327105637705.png)

可以看到，tomcat03和tomcat02做了绑定，使用同样的命令查看tomcat02的元数据信息，并没有这一项，所以这就是为啥tomcat03通过容器名能ping通tomcat02，而tomcat02却不能通过容器名ping通tomcat03。

也可以通过查看tomcat03的`hosts`文件进行验证。

```shell
[root@ ~]#: docker exec -it tomcat03 cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.3      tomcat02 28cc9b1ece24
172.17.0.4      788c3dcb238e


[root@ ~]#: docker exec -it tomcat02 cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.3      28cc9b1ece24
```

所以--link参数，本质上就是在容器的`host`文件里增加了ip映射。

**在实际开发中，不建议使用--link的方法，使用自定义网络。**

#### 6.3 自定义网络

> 查看所有网络

![image-20210327110701381](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327110701381.png)

网络模式：

- bridge：桥接模式
- none：不配置网络
- host：和宿主机共享网络
- container：容器网络连通（用的少，局限性较大）

```shell
# 之前启动tomcat01的时候使用的是下面的命令，其实默认加了--net参数
# 下面的命令等价于docker run -d -P --name --net bridge tomcat01 tomcat
# bridge就是docker0网络的name
[root@ ~]#: docker run -d -P --name tomcat01 tomcat
```

我们可以创建一个自己的网络

```shell
# docker network create --help
# -d  网络模式
# --subnet  子网地址192.168.0.0/16
# --gateway  网关
[root@ ~]#: docker network create -d bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet
f2ab8b7fc3789841e0af9d4766a792c90da5ca4ace54d82396da4605d692198f

[root@ ~]#: docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
843b0497d70e   bridge    bridge    local
535d144c49fa   host      host      local
f2ab8b7fc378   mynet     bridge    local
fbf14c00c75e   none      null      local
```

![image-20210327111934318](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327111934318.png)

这里我们就搭建好了一个自己的网络，在启动容器的时候，就可以指定我们自己创建的网络了。

```shell
[root@ ~]#: docker run -d -P --name tomcat-net01 --net mynet tomcat
dc22821ddfd3dff3da6fce2a31dcc7a750c4c71204bc1279f99dc637ecf2d1ab

[root@ ~]#: docker run -d -P --name tomcat-net02 --net mynet tomcat
9f0e545c6442f0f04bbf7cba980c9d4c2971844fc04e7fd7e6775c78790018b2

# 查看自己创建的网络的信息
[root@ ~]#: docker network inspect f2ab8b7fc378
[
    {
        "Name": "mynet",
        "Id": "f2ab8b7fc3789841e0af9d4766a792c90da5ca4ace54d82396da4605d692198f",
        "Created": "2021-03-27T11:17:02.455837658+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "192.168.0.0/16",
                    "Gateway": "192.168.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "9f0e545c6442f0f04bbf7cba980c9d4c2971844fc04e7fd7e6775c78790018b2": {
                "Name": "tomcat-net02",
                "EndpointID": "dec261463bf388a900ba53fe37d602e09b3e2087125a81dc4d7a13c42a135731",
                "MacAddress": "02:42:c0:a8:00:03",
                "IPv4Address": "192.168.0.3/16",
                "IPv6Address": ""
            },
            "dc22821ddfd3dff3da6fce2a31dcc7a750c4c71204bc1279f99dc637ecf2d1ab": {
                "Name": "tomcat-net01",
                "EndpointID": "c4dd60f3ad80416f9f4a9284af7b79014ff0405480caed952822fbdedfd7704a",
                "MacAddress": "02:42:c0:a8:00:02",
                "IPv4Address": "192.168.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```

![image-20210327112252486](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327112252486.png)

这时候测试tomcat-net01去ping tomcat-net02

```shell
# 使用ip地址ping
[root@ ~]#: docker exec -it tomcat-net01 ping 192.168.0.3
PING 192.168.0.3 (192.168.0.3) 56(84) bytes of data.
64 bytes from 192.168.0.3: icmp_seq=1 ttl=64 time=0.096 ms
64 bytes from 192.168.0.3: icmp_seq=2 ttl=64 time=0.068 ms
64 bytes from 192.168.0.3: icmp_seq=3 ttl=64 time=0.064 ms

# 使用容器名ping也能成功，并没有使用--link
[root@ ~]#: docker exec -it tomcat-net01 ping tomcat-net02
PING tomcat-net02 (192.168.0.3) 56(84) bytes of data.
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=1 ttl=64 time=0.048 ms
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=2 ttl=64 time=0.065 ms
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=3 ttl=64 time=0.067 ms

```

自定义的网络，docker都已经维护好了对应的关系，推荐使用这种方式。

好处：

redis - 不同的集群使用不同的网络，保证集群是安全和健康的。

mysql - 不同的集群使用不同的网络，保证集群是安全和健康的。

#### 6.4 网络互通

![image-20210327131338657](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327131338657.png)

tomcat-01和tomcat-02两个容器使用的docker0网络，tomcat-net-01和tomcat-net-02使用的是我们自己创建的网络mynet，是不能互相ping通的。

![image-20210327131530168](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327131530168.png)

![image-20210327131624248](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327131624248.png)

```shell
# 将tomcat02容器连接到mynet网络
[root@ ~]#: docker network connect mynet tomcat02

# 查看网络的数据信息，发现将tomcat02容器放到了mynet网络下
# 这样tomcat02容器就有了两个ip地址，跟阿里云服务器一样，一个公网ip一个私网ip
[root@ ~]#: docker network inspect mynet
```

![image-20210327131952819](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327131952819.png)

```shell
[root@ ~]#: docker exec -it tomcat02 ping tomcat-net02
PING tomcat-net02 (192.168.0.3) 56(84) bytes of data.
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=1 ttl=64 time=0.071 ms
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=2 ttl=64 time=0.066 ms
64 bytes from tomcat-net02.mynet (192.168.0.3): icmp_seq=3 ttl=64 time=0.064 ms

[root@ ~]#: docker exec -it tomcat-net01 ping tomcat02
PING tomcat02 (192.168.0.4) 56(84) bytes of data.
64 bytes from tomcat02.mynet (192.168.0.4): icmp_seq=1 ttl=64 time=0.069 ms
64 bytes from tomcat02.mynet (192.168.0.4): icmp_seq=2 ttl=64 time=0.065 ms
64 bytes from tomcat02.mynet (192.168.0.4): icmp_seq=3 ttl=64 time=0.073 ms

[root@ ~]#: docker exec -it tomcat-net01 ping tomcat01
ping: tomcat01: Name or service not known
```

结论：如果要跨网络操作， 就需要使用`docker network connect`进行连通。

#### 6.5 实战

> 部署redis集群

![image-20210327134349847](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327134349847.png)

```shell
# 创建网卡
[root@ ~]#: docker network create redis --subnet 172.38.0.0/16

# 通过脚本创建6个redis配置
for port in $(seq 1 6); \
do \
mkdir -p /mydata/redis/node-${port}/conf
touch /mydata/redis/node-${port}/conf/redis.conf
cat << EOF >/mydata/redis/node-${port}/conf/redis.conf
port 6379
bind 0.0.0.0
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 172.38.0.1${port}
cluster-announce-port 6379
cluster-announce-bus-port 16379
appendonly yes
EOF
done
```

![image-20210327135317216](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327135317216.png)

```shell
# 启动6个redis容器
docker run -p 637${port}:6379 -p 1637${port}:16379 --name redis-${port} \
-v /mydata/redis/node-${port}/data:/data \
-v /mydata/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.1${port} redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6371:6379 -p 16371:16379 --name redis-1 \
-v /mydata/redis/node-1/data:/data \
-v /mydata/redis/node-1/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.11 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6372:6379 -p 16372:16379 --name redis-2 \
-v /mydata/redis/node-2/data:/data \
-v /mydata/redis/node-2/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.12 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6373:6379 -p 16373:16379 --name redis-3 \
-v /mydata/redis/node-3/data:/data \
-v /mydata/redis/node-3/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.13 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6374:6379 -p 16374:16379 --name redis-4 \
-v /mydata/redis/node-4/data:/data \
-v /mydata/redis/node-4/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.14 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6375:6379 -p 16375:16379 --name redis-5 \
-v /mydata/redis/node-5/data:/data \
-v /mydata/redis/node-5/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.15 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 

docker run -p 6376:6379 -p 16376:16379 --name redis-6 \
-v /mydata/redis/node-6/data:/data \
-v /mydata/redis/node-6/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.16 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 
```

![image-20210327140250853](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327140250853.png)

```shell
[root@ conf]#: docker exec -it redis-1 /bin/sh
/data # ls
appendonly.aof  nodes.conf

# 创建集群
/data # redis-cli --cluster create 172.38.0.11:6379 172.38.0.12:6379 172.38.0.13:6379 172.38.0.14:6379 172.38.0.15:6379 172.38.0.16:6379 --cluster-repli
cas 1
>>> Performing hash slots allocation on 6 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
Adding replica 172.38.0.15:6379 to 172.38.0.11:6379
Adding replica 172.38.0.16:6379 to 172.38.0.12:6379
Adding replica 172.38.0.14:6379 to 172.38.0.13:6379
M: 58f5576ad95b4ce8899c7203913961090b564b13 172.38.0.11:6379
   slots:[0-5460] (5461 slots) master
M: 6150b073a47c900cbb0862ac2ad85e7c21ef9085 172.38.0.12:6379
   slots:[5461-10922] (5462 slots) master
M: 95b3faeea63f1048dd84ebb70d5133c545191611 172.38.0.13:6379
   slots:[10923-16383] (5461 slots) master
S: de5787bb26632451d2badfcfcaa123e97e16f20b 172.38.0.14:6379
   replicates 95b3faeea63f1048dd84ebb70d5133c545191611
S: 47e608432908a4a97dd42ac42c56b22473f060c0 172.38.0.15:6379
   replicates 58f5576ad95b4ce8899c7203913961090b564b13
S: c1475019d9c7b7723843a1d0d8c8210aa67488d4 172.38.0.16:6379
   replicates 6150b073a47c900cbb0862ac2ad85e7c21ef9085
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
.
>>> Performing Cluster Check (using node 172.38.0.11:6379)
M: 58f5576ad95b4ce8899c7203913961090b564b13 172.38.0.11:6379
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
S: de5787bb26632451d2badfcfcaa123e97e16f20b 172.38.0.14:6379
   slots: (0 slots) slave
   replicates 95b3faeea63f1048dd84ebb70d5133c545191611
S: c1475019d9c7b7723843a1d0d8c8210aa67488d4 172.38.0.16:6379
   slots: (0 slots) slave
   replicates 6150b073a47c900cbb0862ac2ad85e7c21ef9085
S: 47e608432908a4a97dd42ac42c56b22473f060c0 172.38.0.15:6379
   slots: (0 slots) slave
   replicates 58f5576ad95b4ce8899c7203913961090b564b13
M: 6150b073a47c900cbb0862ac2ad85e7c21ef9085 172.38.0.12:6379
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
M: 95b3faeea63f1048dd84ebb70d5133c545191611 172.38.0.13:6379
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

可以看到，创建了三个主节点172.38.0.11:6379、172.38.0.12:6379、72.38.0.13:6379，三个从节点172.38.0.14:6379、172.38.0.15:6379、172.38.0.16:6379

```shell
# 连接redis客户端，要加上-c参数表示集群，不然就是单机模式
/data # redis-cli -c

127.0.0.1:6379> cluster info

127.0.0.1:6379> cluster nodes


```

![image-20210327141733205](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327141733205.png)

```shell
# 设置一个值，存在172.38.0.13上面，也就是redis-3，从节点172.38.0.14应该也会有这个值
127.0.0.1:6379> set a b
-> Redirected to slot [15495] located at 172.38.0.13:6379
OK

# 把redis-3容器停掉，主节点挂掉
[root@ ~]#: docker stop redis-3
redis-3

# get a还有值，并且是从172.38.0.14获取到的
172.38.0.12:6379> get a
-> Redirected to slot [15495] located at 172.38.0.14:6379
"b"
```

![image-20210327142621243](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327142621243.png)

可以发现，redis-3（172.38.0.13）挂掉后，从节点172.38.0.14上升为主节点。

> SpringBoot项目打包Docker镜像

1、构建SpringBoot项目。

2、打包应用（maven package）

3、编写Dockerfile

4、构建镜像

5、发布运行

```shell
# Dockerfile文件
FROM java:8
COPY *.jar /app.jar
CMD ["--server.port = 8080"]
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

-------------

## 二、进阶篇

### 1、Docker Compose

#### 1.1 简介

启动单个容器一般是Dockerfile、build、run三部曲，需要手动操作，单个容器还好，实际一般微服务有上百个，并且相互之间还有依赖关系，如果要手动操作，那麻烦并且容器出错。可以使用Docker Compose来轻松高效的管理容器。

> 官方介绍

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see [the list of features](https://docs.docker.com/compose/#features).

Compose works in all environments: production, staging, development, testing, as well as CI workflows. You can learn more about each case in [Common Use Cases](https://docs.docker.com/compose/#common-use-cases).

Using Compose is basically a three-step process:

1. Define your app’s environment with a `Dockerfile` so it can be reproduced anywhere.
2. Define the services that make up your app in `docker-compose.yml` so they can be run together in an isolated environment.
3. Run `docker compose up` and the [Docker compose command](https://docs.docker.com/compose/cli-command/) starts and runs your entire app. You can alternatively run `docker-compose up` using the docker-compose binary.

**作用：批量容器编排。**

Docker Compose是Docker的开源项目，使用前需要进行安装。https://docs.docker.com/compose/install/

docker-compose.yml文件的格式如下

```yaml
version: "3.9"  # optional since v1.27.0
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    links:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
```

#### 1.2 安装

**（1）下载**

```shell
# 下载很慢
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 用这个更快
curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.5/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
```

![image-20210327193349227](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327193349227.png)

**（2）授权**

```shell
# docker-compose可执行权限
sudo chmod +x /usr/local/bin/docker-compose

[root@ bin]#: docker-compose version
docker-compose version 1.25.5, build 8a1c60f6
docker-py version: 4.1.0
CPython version: 3.7.5
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

#### 1.3 体验

官方文档：https://docs.docker.com/compose/gettingstarted/   

（1）app.py页面，相当于一个应用。

（2）Dockerfile打包为镜像。

（3）docker-compose.yml文件（定义整个服务需要的环境，web、redis等）。

（4）启动compose项目（docker compose up）-d参数表示后台启动

运行`docker compose up`命令后的流程

（1）创建一个网络`composetest_default` with the default driver

（2）执行docker-compose.yml文件。

（3）启动服务composetest_redis_1和composetest_web_1，均在`composetest_default` 网络下面。

**停止compose：**

- docker-compose down（需要在docker-compose.yml文件所在目录下执行）
- ctrl + c

> docker-compose.yml文件编写规则

官方文档：https://docs.docker.com/compose/compose-file/

![image-20210327202637983](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210327202637983.png)

```yaml
# 3层

version: ''  # 版本
service:  # 服务
	服务1: web
		# 服务配置
		images
		build
		netowrk
		......
	服务2: redis
		......
# 其他配置 网络/卷，全局规则
volumes:
networks:
configs:
```

#### 1.4 使用compose部署wordpress

参考文档：https://docs.docker.com/compose/wordpress/

#### 1.5 实战

> 使用docker compose部署SpringBoot项目

（1）新建一个SpringBoot项目

![image-20210328095004152](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328095004152.png)

```properties
server.port=8080
spring.redis.host=redis
```

（2）编写Dockerfile文件构建镜像

```dockerfile
FROM java:8

COPY *.jar /app.jar

CMD ["--server.port=8080"]

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
```

（3）编写docker-compose.yml编排项目

```yml
version: '3.8'
services:
  myapp:
    build: .
    image: myapp
    depends_on:
      - redis
    ports:
    - "8080:8080"
  redis:
    image: "library/redis:alpine"
```

（4）在服务器上docker-compose up启动项目

首先对项目进行`maven package`，然后把需要的文件放到服务器上

![image-20210328102030289](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328102030289.png)

执行`docker-compose up`命令构建镜像

![image-20210328103210124](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328103210124.png)

如果重新打包后上传服务器，`docker-compose up --build`重新构建，启动成功

![image-20210328104857804](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328104857804.png)

![image-20210328104943347](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328104943347.png)

测试成功

![image-20210328135953571](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328135953571.png)

发现好多为none的镜像，应该是每次`docker-compose up --build`重新构建就会产生一个，批量删除使用`docker images|grep none|awk '{print $3}'|xargs docker rmi`命令，先删除容器再删除镜像。

![image-20210328140156205](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328140156205.png)

### 2、Docker Swarm

官方文档：https://docs.docker.com/engine/swarm/

#### 2.1 购买服务器

要搭建集群，必须要有服务器，去阿里云租几台，按量使用的。

![image-20210328214545037](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328214545037.png)

#### 2.2 四台服务器安装Docker环境

按照基础篇1.3和1.4小节进行安装即可。

#### 2.3 Swarm工作模式

![image-20210328210844850](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328210844850.png)

#### 2.4 搭建集群

新机器网络

![image-20210328215024847](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215024847.png)

对于服务器1

![image-20210328215149995](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215149995.png)

![image-20210328215223944](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215223944.png)

`ip addr`查看服务器的ip地址

![image-20210328215506864](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215506864.png)

初始化节点`docker swarm init`

![image-20210328215704062](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215704062.png)

如果要让一个worker节点加入这个swarm，使用上面的命令1，如果要让一个manager节点加入这个swarm，则使用命令2。

```shell
# 获取令牌
docker swarm join-token manager
docker swarm join-token worker
```

对于服务器2，使用`docker swarm join`命令加入swarm成为worker节点。

![image-20210328215954298](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328215954298.png)

可以看到，swarm里已经有两个节点了。

![image-20210328220056947](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328220056947.png)

同理，把服务器3加入作为worker节点，服务器4加入作为manager节点。

![image-20210328220405470](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328220405470.png)

大概流程如下：

（1）init生成主节点。

（2）加入（成为worker或者manager）

#### 2.5 Raft协议

上面已经搭建双主双从的集群（即两个主节点，两个从节点），假设一个节点挂了，其他节点是否可用？

Raft协议：保证大多数节点存活才可以用。

只要主节点数量 > 1，就可以正常使用，所以主节点至少大于3台，不然没有意义。

假设主节点为manager1和manager2，从节点为worker1和worker2。

（1）将manager1节点所在的机器停止，在双主的情况下，另一个主节点也不能用。

（2）如果让worker1节点离开swarm，则状态变为down。

![image-20210328211814390](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328211814390.png)

（3）命令都只能在manager节点使用，worker只是用来工作的。

![image-20210328211932642](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328211932642.png)

（4）让worker1节点变为manager节点，那么停止manager1节点所在的机器，集群还可以正常使用，因为此时还有两个manager节点。

#### 2.6 实战

弹性！扩缩容！集群！

告别 `docker run`。

`docker-compose up` 属于单机启动一个项目。

集群：swarm，`docker service`。

容器 => 服务 => 副本。容器相当于一个服务。

redis服务 => 10个副本。（同时开启10个redis容器）

接下来体验一下：创建服务、动态扩展服务、动态更新服务。

![image-20210328221235970](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328221235970.png)

灰度发布：金丝雀发布。

在服务器1上使用`docker service`启动一个nginx

```shell
docker service create -p 8888:80 --name my-nginx nginx
```

![image-20210328221629059](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328221629059.png)

```shell
docker run  # 容器启动，不能扩缩容器
docker service # 可以进行扩缩容、滚动更新、灰度发布
```

查看服务`docker server ps`

![image-20210328221838807](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328221838807.png)

**虽然是在服务器1上启动了nginx，但使用docker ps命令发现，该服务不一定存在服务器1上，可能是存在其他节点上。**

如果需要进行扩容

```shell
docker service update --help
    ···
    --replicas uint                      Number of tasks
    ···

# 启动3个nginx
docker service update --replicas 3 my-nginx
```

![image-20210328222338545](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328222338545.png)

3个nginx会随机运行在4个服务器中。

使用浏览器访问，可以出现nginx欢迎页面。对于没有运行nginx服务的那台服务器，依然可以访问到nginx。

**对于一个服务，集群中任意的节点都可以访问。服务可以有多个副本动态扩缩容实现高可用。**

同样也可以使用`docker service scale`命令进行扩缩容。

```shell
docker service scale my-nginx=5
```

移除服务

```shell
docker service rm my-nginx
```

#### 2.7 概念总结

>  **Swarm**

集群的管理和编号，docker可以初始化一个swarm集群，其他节点可以加入成为管理者或者工作者。

> **Node**

就是一个docker节点，多个节点就组成了一个网络集群。

> **Service**

任务，可以在管理节点或者工作节点运行。用户访问

![image-20210328224445675](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328224445675.png)

> **Task**

容器内的命令。

![image-20210328224412655](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328224412655.png)

![image-20210328224532204](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328224532204.png)

> 服务副本与全局任务

![image-20210328224633472](C:\Users\lxp\AppData\Roaming\Typora\typora-user-images\image-20210328224633472.png)

调整service以什么方式运行

```shell
--mode string  
Service mode (replicated, global, replicated-job, or global-job) (default "replicated")

docker service create --mode replicated --name mytomcat tomcat:7   # 默认的
docker service create --mode global --name haha alpine ping baidu.com

# 场景？日志收集
每一个节点有自己的日志收集器，过滤，再把所有日志传给日志中心。
```

