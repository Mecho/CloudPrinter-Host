

# 云上印记自助打印机（施工中）

使用本项目构建一个属于自己的自助收费打印机

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/Mecho/CloudPrinter-Host/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">简单配置的自助打印机</h3>
  <p align="center">
    使用本项目配置属于你的可收费的云自助打印机
    <br />
    <a href="https://github.com/Mecho/CloudPrinter-Host"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mecho/CloudPrinter-Host">查看Demo</a>
    ·
    <a href="https://github.com/Mecho/CloudPrinter-Host/issues">报告Bug</a>
    ·
    <a href="https://github.com/Mecho/CloudPrinter-Host/issues">提出新特性</a>
  </p>
</p>


 本项目面向所有喜欢动手想要自己配置一套可以赚钱的自助打印机的同学
 (代码勿喷 闲来无事搞的 原本不准备这么运营)
## 目录

- [上手指南](#上手指南)
  - [部署前的准备](#部署前的准备)
  - [部署步骤](#部署步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

本章我们将讲解第一次如何进行部署

###### 部署前的准备

1. 一台性能还凑活的主机（小主机工控机尤佳或者自己电脑也不是不行）
   1. Windows系统（啥版本其实都行 LTSB尤佳）
   2. Python3环境
2. 一台打印效果你觉得还不错的打印机（做生意咱用好的哦~）
3. 一个二维码扫描模块（淘宝有卖不贵）
4. 企业小程序账号（用于收费，没有也可以，联系作者直接用作者部署好的）
5. 云服务器（用于存储任务列表，没有也可以，联系作者直接用作者部署好的）
6. 腾讯云COS（用于存储用户上传的文件，没有也可以，联系作者直接用作者部署好的）
7. 一个善于思考的脑袋瓜子（瓜子🌻好吃）

###### **部署步骤**

1. 部署用户端小程序、云服务器及腾讯云COS（联系作者QQ：1554655360 备注：自助打印机 我会耐心帮助你的哦~）
2. 下载或克隆本仓库
```sh
git clone https://github.com/Mecho/CloudPrinter-Host.git
```
3. 安装Python依赖包（如果在真实环境发现还是缺少包自己搜搜都能安装好）
```sh
pip install requests   //用于访问任务分发服务器获取打印任务
pip install pypiwin32  //用于调用打印机
pip install pyserial   //用于串口调用扫描器
pip install Pillow     //用于对图像打印时对图像进行调整
pip install wmi        //用于获取主机序列号与后端服务器鉴权
pip install PyQt5      //用于窗体展示打印状态
```
4. 打开config.txt 将第一个1改为自己主机ID（第一步的时候我会告诉你如何填写）
5. 打开printer.py 找到173行修改扫描器的串口参数
6. 运行！





### 文件目录说明
eg:

```
文件树
├── LICENSE.txt //GPL3.0开源协议
├── README.md   //指南
├── config.txt  //简单配置文件
├── database.db //任务存储数据库
└── printer.py  //源程序
```





### 开发的架构 

请阅读[ARCHITECTURE.md](https://github.com/Mecho/CloudPrinter-Host/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

暂无

### 使用到的框架

- [xxxxxxx](https://getbootstrap.com)
- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

xxx@xxxx

知乎:xxxx  &ensp; qq:xxxxxx    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/Mecho/CloudPrinter-Host/blob/master/LICENSE.txt)

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:Mecho/CloudPrinter-Host
[contributors-shield]: https://img.shields.io/github/contributors/Mecho/CloudPrinter-Host.svg?style=flat-square
[contributors-url]: https://github.com/Mecho/CloudPrinter-Host/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Mecho/CloudPrinter-Host.svg?style=flat-square
[forks-url]: https://github.com/Mecho/CloudPrinter-Host/network/members
[stars-shield]: https://img.shields.io/github/stars/Mecho/CloudPrinter-Host.svg?style=flat-square
[stars-url]: https://github.com/Mecho/CloudPrinter-Host/stargazers
[issues-shield]: https://img.shields.io/github/issues/Mecho/CloudPrinter-Host.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/Mecho/CloudPrinter-Host.svg
[license-shield]: https://img.shields.io/github/license/Mecho/CloudPrinter-Host.svg?style=flat-square
[license-url]: https://github.com/Mecho/CloudPrinter-Host/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian




