## 安装k8s



### 添加软件源


#### NO_PUBKEY


#### depend on
	执行apt update



### 修改HOST
`vim /etc/hosts`
注释掉
`127.0.0.1 computer_name`
添加
`192.168.9.103  master`
`192.168.9.104  node1`

### 安装kubeadm
安装kubeadm时会自动安装kubectl、kubelet。


### 列出需要的镜像

### 使用国内源下载这些镜像

###　使用tag命令打标

### 配置 master

### 添加网络配置

`kubectl apply `





##  安装 NVIDIA 驱动

### 寻找合适的版本

根据自己的GPU型号，到英伟达网站寻找合适的版本。



### 安装



### 问题

#### 重复登录

#### 进不去图形界面





















