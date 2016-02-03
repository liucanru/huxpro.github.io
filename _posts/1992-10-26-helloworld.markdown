---
layout:     post
title:      "博客·在路上"
subtitle:   " \"Hello World. Blog on the road.\""
date:       2015-10-4 22:10:17
author:     "Lcr"
header-img: "img/post-bg-2015.jpg"
tags:
    - 生活
---

> “Not only on the road but also on the path.”  -- Jack Kerouac


## 前言

为什么要写博客？

*记录
听到的会有印象，看到的会忆起，而只有写下来才能真正记得，并能时常回顾。于我而言，习得的知识，实践的经验，思考的感悟，自我的认识，这些成长收获的点滴，都只是脑海里的过客，如果不搭一个舒适安稳的窝加以挽留，他们片刻之后便会离去，只能留下丁点的痕迹，其余的便都流失消散了。

升华
生活在一个信息爆炸的时代，的不断输出给我带来恐惧

分享

有了想法，便一直在找一个文字的居所。

## 正文

首先想到在新浪，网易等网站开通个人博客，好处是简单方便，但是觉得这些提供个人博客服务的网站UI都太丑，而且还常常有大量的广告和无关链接等干扰信息，非常影响读者的阅读体验。于是萌生了搭建一个个人博客网站的想法。

于是开始搜索搭建个人网站的方法。找了一些网上的教程，作为一个技术小白，看完以后还是感觉有些云里雾里，让人无从下手。后来终于找到一个足够轻松优雅的解决方案：[GitHub Pages](https://pages.github.com/) + [Jekyll](http://jekyllrb.com/)快速搭建个人博客网站，具备了满足我所需要的一切优点：

* 不需要web的相关知识，Markdown轻松优雅
* 不需要自已申请域名以及服务器资源，GiHub Pages 提供了所需的一切
* 搭建简单，没有复杂的配置，只需专心于文字创作

<p id = "build"></p>

---

###下面详细说一下整个博客网站的搭建过程。

背景介绍

首先介绍一下GitHub是什么

> GitHub is a web-based Git repository hosting service. It offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features.
[GitHub-wiki](https://en.wikipedia.org/wiki/GitHub)

[Git](https://en.wikipedia.org/wiki/Git)是一个分布式的版本控制系统，版本控制是一个软件工程中的概念。一个项目如果由多人合作开发，那么就需要有一套程序来协调各个人的工作。版本控制意味着记录项目的每一次更新变动的详情，同步最新项目版本，避免不同人对同一文件修改的冲突，从而实现多人高效协作开发。

就好像一篇文章一个人写的话从头写到尾就可以了，但多人一起写的话，每个人就必须知道当前文章被其他人编辑成什么样了，每个人都从最新的版本往下写。如果一篇文章分多个段落(模块)的话，还要避免多个人同时编辑同一个段落(模块)，以避免冲突。

了解了Git以后，GitHub就是在Git的基础上提供了Web界面和具有图形化界面的桌面软件，方便进行更新项目最新版本，提交更新，处理冲突，撤销更改返回到历史版本等操作，此外GitHub网站还提供项目托管展示等其他相关服务。

（如果看了GitHub的介绍感觉比较深涩难懂，那就忽略好了，反正跟后面的博客网站的搭建没有多大关系，只需要知道伟大的GitHub网站给我们提供了强大的[GitHub Pages](https://pages.github.com/) + [Jekyll](http://jekyllrb.com/)就好了。）

介绍完GitHub，我们再来看看GitHub Pages的介绍

> [GitHub Pages](https://github.com/blog/272-github-pages) allow you to publish web content to a github.com subdomain named after your username. With Pages, publishing web content becomes as easy as pushing to your GitHub repository.


GiHub Pages可以让你发布Web内容到GiHub.com上，并且能够以你的GitHub网站上注册的用户用户名作为子域名的一部分来访问。有了GitHub Pages提供的服务器和域名资源，接下来还要用到Jekyll：

> We thought it would be nice to give you an easy way to assemble more complex sites. That’s why we pipe every Pages-bound repo/branch through [Jekyll](https://github.com/jekyll/jekyll), my very own blog-aware static site generator that was purpose built specifically for this task. With Jekyll, you have access to layouts, includes, filters, syntax highlighting, Textile and Markdown, and intelligent handling of blog entries. All you have to do is follow the Jekyll conventions and we’ll handle the transformation. For an example of a Jekyll site that works on Pages, check out my tpw blog repo.
[GitHub Pages](https://github.com/blog/272-github-pages)

GitHub Pages项目Jekyll是GitHub支持的一个开源项目，提供了一个轻松的方式搭建一个复杂的网站。

搭建步骤

1. 在[GitHub](https://github.com/)网站注册一个账号，账号的用户名会作为之后网站域名的一部分。
2. 进入[Jekyll-GitHub](https://github.com/jekyll/jekyll)，点击｀fork｀
3. 进入个人页面，找到
	

## 后记

回顾这个博客的诞生，纯粹是出于个人兴趣。

如果你恰好逛到了这里，希望你也能喜欢这个博客主题。

—— Lcr 后记于 2015.10
