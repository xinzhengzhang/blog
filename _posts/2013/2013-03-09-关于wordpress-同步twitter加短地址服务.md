---
layout: post
title: 关于wordpress 同步twitter加短地址服务
categories:
- program
tags: []
published: true
comments: true
---
<p>1.首先安装依赖http://wordpress.org/extend/plugins/social/<br />
2.再安装上 https://wordpress.org/extend/plugins/twitter-tools/</p>

<p>这样就其实已经可以在发布的时候同步到twitter上了、但是有一个问题那就是url是全长度输出的、在限制长度的twitter下这是个非常大的问题<br />
所以我修改了下源码用了sina的短地址服务（大sina把google api给墙掉了残年……<br />
-----------------------------------------------------------------------------------------------------------<br />
具体操作如下<br />
1.首先从wordpress的根目录开始寻址到/wp-content/plugins/social/views/wp-admin/post/broadcast/options.php （我们需要修改文件就在这<br />
2.找到第70行 其实我们从这里就可以看出$account['content']里就是我们发出的文本段（鉴于本人太懒不高兴往上找了所以就直接在这段做处理<br />
3.先用正则式剔出我们blog的url 然后对他进行shorten再替换回去

```

url_short,$account['content']);
    echo esc_textarea($tar);
	echo "; 
	echo esc_textarea($tar); 
?>>
</p></pre></p>

<p>然后跑起来就ok了<br />
修改完后的文件附上:<a href="http://snorlax-wordpress.stor.sinaapp.com/uploads/2013/03/options.php_.zip">options.php</a></p>

```
