---
date: 2012-11-02
layout: post
title: os x safari代理配置
categories:
- program
tags: []
published: true
comments: true
---
<p>首先先问候一下方校长，自从google被封了一批ip后墙翻的我简直痛不欲生一会么证书伪造一会么500……<br />
大chrome崩溃的频率也tm越来越高，想来想去既然是os x那就索性用safari装x到到底-_-#</p>

<p>个么safari上默认的设代理就是全局翻（上weibo什么的怎么办啊不卡死啊……<br />
那就也写个简单点的代理就好了么（其实如果用chrome的switchysharp直接导出他的配置文件就好了
<a href="http://snorlax-wordpress.stor.sinaapp.com/uploads/2012/11/6FC51D93-7ED1-46FA-A632-14B720CAE1EE.jpg"><img src="http://snorlax-wordpress.stor.sinaapp.com/uploads/2012/11/6FC51D93-7ED1-46FA-A632-14B720CAE1EE-300x163.jpg" alt="" title="6FC51D93-7ED1-46FA-A632-14B720CAE1EE" width="300" height="163" class="alignnone size-medium wp-image-82" /></a></p>

<p>那么没有的怎么搞呢，自己写一个也很简单的<br />
浏览器是会通过这个FindProxyForURL来选择具体是否选择实用代理<br />
那么最简单的一个代理就是</p>

<p>
```

function FindProxyForURL(url, host)
{
    if(dnsDomainIs(host, "twitter.com")
    {
        return 'PROXY 127.0.0.1:8087'
    }
    return 'DIRECT';
}



那么稍微再加个正则匹配的就变成这样了


function FindProxyForURL(url, host)
{
    if (shExpMatch(url, "*://*.twitter*")) return 'PROXY 127.0.0.1:8087';
    if (shExpMatch(url, "*://*.google*")) return 'PROXY 127.0.0.1:8087';
    return 'DIRECT';
}


个么最后写完这个脚本丢在哪儿呢
在 system perference->>network->advanced->proxy->auto proxy  configuration把自己刚写的那pac(后缀什么的都无所谓的)给导进去就可以了</p>

<p>enjoy</p>

```
