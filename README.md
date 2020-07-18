# BlogWebapp-practice
基于廖雪峰老师2016年的Python3教程实战部分，从零搭建个人博客网站。没有使用成熟的Flask, Django等Python Web开发框架，代码包含：
* 数据库构建
* Web框架构建
* ORM构建
* MVC构建
* API构建
* 前端页面CSS/HTML构建
* JS, DOM操作
* 服务器部署

由于廖雪峰老师的教程发布的时间较早，他的网站和相应github中提供的参考代码有相当一部分已经不符合最新的语法，尤其是异步框架syncio，MySQL的新语法等。感谢教程的评论区里某位同学提供的大大的网站 让我成功熬到了最后关头，成功运行。网页的主要代码都很新，但是在部署部分，依然因为MacOS和Windows的区别，以及对于Linux部署的不熟悉，踩了很多坑。
(https://aodabo.tech/blog/001546714438970511a8089adc94c909312e2554aa4eabd000)

这里提供我成功运行的版本，本代码开发环境 **Windows10 Python3.8.2  MySQL 8.0.19**。部署于AWS申请的免费一年的**Ubuntu 18.04** 默认安装的**Python 3.6.9**

supervisor、Nginx的配置文件我直接在服务器上用vim编辑的，因此没有放上来：
* supervisor部分我使用的是前面提到的网站上的相应代码
* Nginx部分则是使用廖雪峰老师的配置，因为aodabo的配置文件包含域名解析和SSL证书相关内容，我也是第一次玩AWS，它的证书审核我等待了好几天，而域名解析又只需要在AWS的控制台中设置即可。

综上，请配合廖雪峰老师Python教程及凹大卜网站相关教程食用！


