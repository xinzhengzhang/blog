---
date: 2013-03-07
layout: post
title: 关于ios下的goagent使用
categories:
- program
tags: []
published: true
comments: true
---
<p>国际惯例先问候下方滨兴你这狗娘养的<br />
-----------------------------------------------------------------------------------<br />
首先说下我的server的版本是2.1.3<br />
ios下的goagent各种教程到处都是、可是只可惜共军太狡猾、gfw现在是越来越牛逼<br />
反正我搜着的各种帖子要么是那种二到家的就装装装下去就成功了、要么就是中间某个步骤被干掉了<br />

正常人都肯定会看官方的文档、可惜没那么简单……<del datetime="2013-03-07T06:08:41+00:00">https://code.google.com/p/goagent/wiki/GoAgent_IOS</del>
这上面的版本由于过于古老让我吃尽苦头<br />
好了废话到此位置<br />
-----------------------------------------------------------------------------------<br />
由于官方那个是把python包直接内嵌在里面的所以第一步装python<br />
为了一下操作方便点可以安装下open ssh以及aptbackup(用了这个就可以直接用apt-get了<br />
1.这个可以直接在178的源里搜索安装python2.7<br />
2.在big boss源中安装adv-cmds（是下一步的依赖<br />
3.接下去就是goagent了 <https://code.google.com/p/goagent/downloads/detail?name=goagent-local-1.7.deb&can=2&q=>(debian包安装可以采取dpkg -i 或者就索性丢到</var/root/Media/Cydia/AutoInstall> 重启下<br />
4.安装方便的工具栏 有两种选择 第一是先装sbsetting依赖（有一串东西）然后装178源里的goagent-toggle 第二就是用之前的goagent-ios 在里面的/Applications/goagent-ios.app/goagent-local/proxy.py做一个映射到/var/mobile/goagent-local/proxy.py（前者是在sbsetting中进行开关、后者是在通知栏最下放有个按键进行开关）<br />
5.配置goagent中的appid、以及更改为google_hk(若用google_cn请把hosts中的域名更改为响应的ip地址、isp不提供解析)配置当前网络下的pac 地址在<file://localhost/stash/Applications/MobileSafari.app/8087.pac> 在当前wifi里的http proxy中填写<br />
以上你已经在http情况下翻过去了<br />
6.现在要安装ca、这个正常看起来简单暴的事情、由于你现在根本在没翻的前提下变的异常困难不过你可以发现goagent-local里其实已经有了很多ca了、把</var/mobile/goagent-local/certs/apis.google.com.crt> 拷贝出来（如果本机可以翻墙可以直接把<https://goagent.googlecode.com/files/CA.crt>下载下来用并跳到8） 然后如果自己有python环境就用传说中两行的web服务器把ca给共享出去

```

import SimpleHTTPServer
SimpleHTTPServer.test()

7.在safari访问这个然后下一步安装、到这就可以轻易的safari访问 <https://goagent.googlecode.com/files/CA.crt> 装他的ca了

8.你自由了:-)

ps.以上的server的环境是在2.1.3的基础上server我放了个压缩包server



```
