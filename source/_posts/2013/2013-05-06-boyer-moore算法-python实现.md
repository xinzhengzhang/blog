---
date: 2013-05-06
layout: post
title: Boyer-Moore算法 python实现
categories:
- program
tags: []
published: true
comments: true
---
<p>看了<a href="http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html?utm_source=feedly">字符串匹配的Boyer-Moore算法</a>后觉得很有用就写一个实现了一下

```

def badcharrule(ori,sear):
	if len(ori)!=len(sear):
		print "error"
	else:
		le=len(ori)
		badindex=-1
		lastindex=-1
		for i in xrange(le-1,0,-1):
			if ori[i]==sear[i]:
				pass
			else:
				badindex=i
				break
		if badindex==-1:
			pass
		else:
			for i in xrange(0,le):
				if sear[i]==ori[badindex]:
					lastindex=i
					break
				else:
					pass
		return badindex-lastindex
def goodpostfixrule(ori,sear):
	if len(ori)!=len(sear):
		print "error"
	else:
		le=len(ori)
		postfix=0
		for i in xrange(le-1,0,-1):
			if ori[i]==sear[i]:
				postfix+=1
			else:
				break
		if postfix==0:
			return -1
		else:
			postfixstring=sear[-postfix:]
			restori=sear[:-postfix]
			if restori.find(postfixstring)==-1:
				restori=postfixstring[:-1]+restori
				if restori.find(postfixstring)==-1:
					return -1
				else:
					return len(sear)-restori.find(postfixstring)-1
			else:
				return len(sear)-restori.find(postfixstring)-len(postfixstring)

def movestep(ori,sear):
	gu=badcharrule(ori,sear)
	if gu==0:
		return 0
	else:
		return max(gu,goodpostfixrule(ori,sear))

oristring="here is a simple example"
searchstring="example"

index=0
while index+len(searchstring)
	move=movestep(oristring[index:index+len(searchstring)],searchstring)
	if move==0:
		print "find it index=%s" %index
		index+=len(searchstring)
	else:
		index+=move
print "search over"

>

```
