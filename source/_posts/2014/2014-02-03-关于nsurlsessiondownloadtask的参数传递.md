---
date: 2014-02-03
layout: post
title: 关于NSURLSessionDownloadTask的参数传递
categories:
- program
tags: []
published: true
comments: true
---
<p>ios7开放了一组新的api其中一个最吸引人的也应该就是开放了后台下载的接口。当然凭ios一贯的作风肯定是把接口封的简单的要死然后用着噁心的要死……反正我是绝对被噁心到了、最近要解决的一个问题就是把downloadtask和实体关联上的问题。当然最简单的就是传参数了，然后我可以很负责的告诉你……尼玛你assign task的时候和从call back拿的时候不是一个实体！！！wtf……所以什么用runtime给他加点奇怪的东西什么都别想了……<br />
-------------------------------------------万恶的分割线-----------------------------------------------<br />
然后就说下解决办法吧……其实想想是会吐血的，仔细看看他的.h里面终于发现了还有这个一个东西……至少他是不会变的……<br />
所以我们既然找到了有不变的东西那么就终于可以有解决办法了……直接把要传的东西转成json靠这个东西传简直轻松又愉快……</p>

```objective-c
/*
 * The taskDescription property is available for the developer to
 * provide a descriptive label for the task.
 */
@property (copy) NSString *taskDescription;
```
