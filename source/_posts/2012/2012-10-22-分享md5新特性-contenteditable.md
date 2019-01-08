---
date: 2012-10-22
layout: post
title: 分享html5新特性 contenteditable
categories:
- program
tags: []
published: true
comments: true
---
<p>最近做个项目碰到一个很纠结的问题，富文本编辑。什么脑筋都动了，抓js句柄，手动解析标签属性，然后转成ios的font等等，想都不用想这种愚蠢又耗时的行为是不可能解决问题的。直到大stackoverflow救了我<br />
原帖如下<br />
http://stackoverflow.com/questions/8012245/using-ios-5-rich-text-editor<br />
用到的最重要的新特性 就是 contenteditable<br />
具体demo 如下<br />
http://html5demos.com/contenteditable</p>

<p>简单来说就是加个section 设置个 contenteditable，就那么简单！<br />
比如

```



 hi 我来作试验的
  首先是段落
  &nbsp; &nbsp; 然后是缩进  

 然后多换行  
 然后大段文字ahdjasd  

jaieowajkncnxmbfhawija
 hiiii

 &nbsp; &nbsp; test over





----------------------------------我是分割线-------------------------

 hi 我来作试验的
  首先是段落
  &nbsp; &nbsp; 然后是缩进  

 然后多换行  
 然后大段文字ahdjasd  

jaieowajkncnxmbfhawija
 hiiii

 &nbsp; &nbsp; test over


仅仅只要把需要编辑的部分加个section设置个 contenteditable＝true，所有的富文本编辑问题就这么搞定了……
>

```
