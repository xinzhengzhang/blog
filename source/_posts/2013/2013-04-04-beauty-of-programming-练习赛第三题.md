---
date: 2013-04-04
layout: post
title: beauty of programming 练习赛第三题
categories:
- program
tags: []
published: true
comments: true
---
<p>先看题</p>

<p><h4>题目列表 > 踩方格</h4>
</p>

<p><div class="coding-problem">		<br />
	<p>时间限制: 1000ms    内存限制: 1024MB</p>
    <p /><h3>描述</h3><p>有一个方格矩阵，矩阵边界在无穷远处。我们做如下假设：<br />a.    每走一步时，只能从当前方格移动一格，走到某个相邻的方格上；<br />b.    走过的格子立即塌陷无法再走第二次；<br />c.    只能向北、东、西三个方向走；<br />请问：如果允许在方格矩阵上走n步，共有多少种不同的方案。2种走法只要有一步不一样，即被认为是不同的方案。</p><h3>输入</h3><p>允许在方格上行走的步数n</p><h3>输出</h3><p>计算出的方案数量</p><p><br /></p>对于小数据1 &lt;= n &lt;= 20; 对于大数据1 &lt;= n &lt;= 100.<p><br /></p></div></p>
	<dl class="content">
		<dt>样例输入</dt>
		<dd>
```
2
		样例输出
		7


这个题目我觉得最大的阴谋就是对于小数据1
我了个fuck了给了个那么小规模的数据还给那么高的分值正常人理所当然的就肯定认为这是个指数级的运算了啊！然后我就想到了三叉树去暴力啊、可是再怎么暴力这个指数摆在那就算是100也很恐怖了、各种挂……纠结了好久好久写了好几种都挂
最后静下心来把他当数学做……然后草稿纸写写……尼玛5分钟就算出来了……
其实思想非常非常简单 往北的节点就是能叉出3条路、其中分别是继续叉2的2条以及继续叉3的一条、往两侧的每次只能叉出两条路、分别是2 和3 具体路径的结构问你了么？去暴力做等于就是浪费这些路径的信息啊小时候怎么做数学题的……要那么多条件吃屎啊……数学规律就是这么简单……然后还不会写么？……！你妹的别说100了来个平方这复杂度都闭着眼睛来的啊……

#include
int main(){
    int a=0;
    int b=1;
    int count＝0;
    int i=0;
    int temp;
    scanf("%d",&count);
    for (i=0; i
没了！没了！写完了！……………………突然有种回归最质朴的感觉真好……
>

```
