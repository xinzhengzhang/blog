---
layout: post
title: 关于protocol buffer 中的Base 128 Varints编码
categories:
- program
tags: []
published: true
comments: true
---
首先大致讲下protocol buffer 是大google用来改变世界的……（不过要干掉xml json什么的我感觉再过二十年吧……好像解析的速度也没有那么的重要<br />
其实具体的google的文档讲了很清楚了
<https://developers.google.com/protocol-buffers/docs/encoding#simple>
然后就是这个奇怪的新的编码、大致的好处我看下来感觉就是类似utf8那样可长可短根据数的大小来决定编码长度这样的
然后拿他官方例子来讲
比如300 来对他encode
首先先把他转成二进制、然后进行补0 补整字节的倍数也就8的倍数
然后进行逆序 最后对每个字节的8位进行填充、也就是每个字节的最高byte如果为1就是把后面那个字节的8位拿过来一起算、反正就是自己算
然后是decode 也就是一个反序 先根据每个字节的最高位拆开成独立的小块 然后以字节为单位进行反序 再然后去0把他十进制读出思想就是这样但是有点疑惑这个倒序的意义我是一直没有明白= =  

好吧最后把代码贴出

```python
def encodebase128(ori):
	t=str(bin(int(ori))[2:])
	tmp=7
	while len(t)>>tmp:
		tmp*=2
	t='0'*(tmp-len(t))+t
	ll=t[-7:]
	for i in xrange(1,tmp/7):
		ll+=t[-(i+1)*7:-i*7]
	ans=""
	for i in xrange(0,tmp/7):
		ans+='0'
		ans+=ll[i*7:(i+1)*7]
	if tmp/7>1:
		ans='1'+ans[1:]
	return ans
def decodebase128(dealed):
	if len(dealed)%8!=0:
		print 'illegal'
	tt=dealed[-7:]
	for i in xrange(len(dealed)/8-1,0,-1):
		tt+=dealed[(i-1)*8+1:(i)*8]
	return int('0b'+tt,2) 
import sys
t= encodebase128(sys.argv[1])
print t
print dealstring(t)
```
