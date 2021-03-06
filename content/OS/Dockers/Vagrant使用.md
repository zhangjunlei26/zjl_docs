Title: Vagrant 使用
Date:  2015-04-16
:category: Docker

Vagrant 使用
============================

## 1. Vagrant功能

     Vagrant usesOracle’s VirtualBox to build configurable, lightweight, and portable virtual machines dynamically..

      【Vagrant 使用Oracle VM VirtualBox 动态创建和配置轻量级的，可重现的，便携的虚拟机环境。】

## 2. Vagrant下载

      http://downloads.vagrantup.com/tags/v1.0.5

## 3. Vagrant安装:

### 3.1. 下载并安装Oracle VM VirtualBox

例如在Windows环境下，需要安装VirtualBox-4.2.0-80737-Win.exe

	https://www.virtualbox.org/wiki/Downloads

### 3.2. 下载并安装最新版本的Vagrant

http://downloads.vagrantup.com/

[注]在 Windows and Mac OS X,vagrant 命令应该自动添加到环境变量PATH. 但是在其他操作系统下, 你必须手动添加/opt/vagrant/bin 到环境变量PATH。

## 4. Vagrant命令

Vagrant安装完成之后，我们就可以从命令行通过vagrant命令来进行操作。vagrant 常用命令如下：

       vagrant box add <name> <url>
       vagrant box list
       vagrant box remove <name>
       vagrant box repackage <name> 
       vagrant init [box-name] [box-url]
       vagrant up [vm-name] [--[no-]provision] [-h]
       vagrant destroy [vm-name]
       vagrant suspend [vm-name]
       vagrant reload [vm-name]
       vagrant resume [vm-name]
       vagrant halt [vm-name]
       vagrant status [vm-name]
       vagrant package [vm-name] [--base name] [--output name.box][--include one,two,three] [--vagrantfile file]
       vagrant provision [vm-name]
       vagrant ssh [vm-name] [-c command] [-- extra ssh args]
       vagrant ssh-config [vm-name] [--host name]

## 5. Vagrantfile

任何Vagrant工程下都有一个Vagrantfile, 就像makefile一样，Vagrantfile用来配置vagrant的行为所创建虚拟机的信息，下面是一个基本的Vagrantfile：      

       Vagrant::Config.run do |config|
           # Setup the box
           config.vm.box = "my_box"
       end

## 6. 创建第一个Vagrant虚拟环境以及工程

### 6.1 创建Vagrantfile

创建工程目录， 并且执行vagrant init命令，该命令会产生最初的 Vagrantfile

$ mkdir vagrant_guide
$ cd vagrant_guide
$ vagrant init

### 6.2 添加一个Base Box:

Vagrant不是从头开始创建虚拟机，而是导入一个虚机的base image，在这个基础上进行构建。这些image就叫做Box。Vagrant 支持从本地文件系统或者HTTP URL来添加boxes：

    $vagrant box add basehttp://files.vagrantup.com/lucid32.box
    $vagrant box add base D:\lucid32.box

    

### 6.3 配置

配置Project使用这个Box: 修改Vagrantfile为如下内容：

     Vagrant::Config.run do |config|
        config.vm.box = "base"
     end

### 6.4 启动虚拟机

    $vagrant up

    

### 6.5 停掉虚拟机

    $vagrant destroy

### 6.6 SSH配置

     Vagrant 提供了对虚拟机的SSH连接，只需要执行一个命令：

    $vagrant ssh

    在Windows环境下可以使用PUTTY，配置下面的信息来连接虚拟机：

     hostname: localhost

     port:             2222

     Connection Type: SSH

     User Name:   vagrant

     Password:     vagrant

    

### 6.7 访问刚才创建的Project.

     Vagrant 通过VirtualBox的shared folder来连接你的application和虚拟机， 默认的shared folder的卫士是/vagrant， 所以想要查看刚才创建的项目，只需要执行：

     vagrant@lucid32:~$ ls /vagrant
     index.html  Vagrantfile

### 6.8 Provisioning：

  通常情况下Box只做最基本的设置，而不是一次到位的设置好所有的环境。Vagrant通常使用chef或者Puppet来做进一步的环境搭建。  
  
  回到刚才创建的index.html，我们需要安装Apache。我们下面用Puppet来完成这一设置。
  
  1. 在项目的根目录下创建文件夹manifests，然后在该文件家中创建Puppet的配置文件default.pp，该文件内容如下：     

	    #Basic Puppet Apache manifest
    	class apache {
	      exec { 'apt-get update':
	        command => '/usr/bin/apt-get update'
    	  }

	      package { "apache2":
    	    ensure => present,
	      }

    	  service { "apache2":
        	ensure => running,
	        require => Package["apache2"],
    	  }
	    }
    	include apache

   2. 在Vagrantfile里添加对Puppet provisioning的支持： 
   
   
		Vagrant::Config.rundo|config|
		config.vm.box="base"
		# Enable the Puppet provisioner
		config.vm.provision:puppet
		end

### 6.9 运行Project

 为了使puppet的配置生效，如果不重启虚机，则需要执行vagrant reload命令。

         $ vagrant reload 

 因为没有配置port forwarding，所以你还不能从本地浏览器查看Project的输出。只能SSH到虚拟机上查看127.0.0.1的输出：

       

### 6.10 进行端口映射

修改Vagrantfile， 添加本地端口和虚机端口的映射关系， 然后执行vagrant reload, 然后你就可以通过本地浏览器来访问：http://localhost:4567.  


	   Vagrant::Config.run do |config|
    	    # Forward guest port 80 to host port 4567
        	config.vm.forward_port 80, 4567
	   end 

## 7. 打包 Packaging

###  7.1 创建一个新的文件Vagrantfile.pkg，内容如下：     

     Vagrant::Config.run do |config|
                # Forward apache
                config.vm.forward_port 80, 8080
     end

### 7.2 打包Project       

       $ vagrant package --vagrantfile Vagrantfile.pkg

## 8. 完成
 
打包完成后，在工程根目录下就会生成package.box，别人就可以使用这个Box了：

    $ vagrant box add my_box /path/to/the/package.box
    $ vagrant init my_box
    $ vagrant up

