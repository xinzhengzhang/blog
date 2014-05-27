---
layout: post
title: 最大公共上升子序列(lcs) python实现
categories:
- program
tags: []
published: true
comments: true
---
<p>mit 算法导论公开课 15集<br />
http://v.163.com/movie/2010/12/L/4/M6UTT5U0I_M6V2U1HL4.html</p>

<p>实现了求出所有的lcs</p>

```
import copy
import sys
#stringa="abcbdab"
#stringb="bdcaba"

stringa=sys.argv[1]
stringb=sys.argv[2]
lena=len(stringa)
lenb=len(stringb)

mapl=[[0 for _ in xrange(lena+1)] for _ in xrange(lenb+1)]
path=[]
for i in xrange(1,lenb+1):
	for j in xrange(1,lena+1):
		if stringa[j-1]==stringb[i-1]:
			mapl[i][j]=mapl[i-1][j-1]+1
			path.append((i,j))
		else:
			mapl[i][j]=max(mapl[i-1][j],mapl[i][j-1])
#for i in mapl:
#	print i
#print path
if len(path)==0:
	print "no lcs"
else:
	backdatestack=[[(lenb,lena),[]]]
	while len(backdatestack)!=0:
		top=backdatestack.pop()
		ansstack=top[1]
		lcs=mapl[top[0][0]][top[0][1]]
		i=top[0][0]
		j=top[0][1]
		while lcs!=0:
			try:
				ind=path.index((i,j))
				ansstack.append(stringb[i-1])
				i-=1
				j-=1
				lcs-=1
			except ValueError:
				if mapl[i-1][j]>>mapl[i][j-1]:<br />
					i-=1<br />
				elif mapl[i-1][j]<mapl[i][j-1]:<br />
					j-=1<br />
				else:<br />
					backdatestack.append([(i-1,j),copy.copy(ansstack)])<br />
					j-=1<br />
		while len(ansstack)!=0:<br />
			print ansstack.pop(),<br />
		print </p>

<p></p>

```
