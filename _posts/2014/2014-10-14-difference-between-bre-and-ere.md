---
layout: post
title: "正则表达式——BRE与ERE区别"
description: ""
category: program
tags: ["re", "shell"]
---
{% include JB/setup %}

### 本文主要说明了正则的两个标准 BRE 以及 ERE的具体区别
  * BRE - Basic Regular Syntax ， ERE - Extended Regular Syntax 顾名思义ere是对bre的拓展。
  * 但是两种语法也都必须要记因为很多Unix程序用的并没有统一。

          | BRE | ERE
  --------| ----| ---
  grep    | √   |
  sed     | √   |
  ed      | √   |
  vi      | √   |
  more    | √   |
  egrep   |     | √
  awk     |     | √
  lex     |     | √

### 公共meta部分
  * `\` 
  	* 用来关闭后续字符意义例如 `\'  \"` 
  	* 在BRE中特别有打开字符意义的意思例如 `\(...\)` `\{...\}`
  * `.`
  	* 用来匹配单个字符
  * `*`
  	* 匹配0-n个字符
  * `^`
  	* 锚点、行首起始处
  	* 在BRE中必须需要在表达式开头才有效
  		* `echo abc | grep ".*^a"` ×
  		* `echo abc | egrep ".*^a"` √
  * `$`
  	* 锚点、行尾结尾处
  	* 同上在BRE中必须要在结尾处才有效
  * `[...]`
  	* `[^...]` 取...的反
  	* `[x-y]` 匹配 x-y 之间的  例如 x=1 y=9 or x=a y=z
  	* `[express]` 匹配express的字符集  例如 express=[:alnum:] [[:alnum:]] 匹配数字字符

  		类别 | 意义
  		----| ---
  		[:alnum:]|数字
  		[:alpha:]|字母
  		[:blank:]|space or tab
  		[:cntrl:]|控制字符
  		[:digit:]|数字
  		[:graph:]|除了空格字符
  		[:lower:]|小写字母
  		[:print:]|可显示的字符
  		[:puncat:]|标点
  		[:space:]|空白
  		[:upper:]|大写字母
  		[:xdigit:]|16进制数字
  * `\n`
  	* 在BRE中为重复\(...\)的第n个表达式且当时位置匹配的结果于他所代表的那个结果相同
  		* `echo axa | grep "\([ab]\)x\1"` √
  		* `echo axb | grep "\([ab]\)x\1"` ×

  	* 在ERE中为重复()的第n个表达式
  		* `echo axa | egrep "([ab])x\1"` √
  		* `echo axb | egrep "([ab])x\1"` ×

### BRE meta部分
  * `\{n,m\}`
  	* 匹配前面单个字符的次数区间为n-m次 
  		* `\{n\}` 重现n次
  		* `\{n,\}` 至少出现n次
  * `\(...\)`
  	* 匹配...子模式的 可以通过上述的`\n`来引用

### ERE meta部分
  * `{n,m}`
  	* 同BRE匹配单个字符n-m次
  * `+`
  	* 匹配一个或n个
  * `?`
  	* 匹配0个或1个
  * `|`
  	* 匹配 | 前后的表达式
  * `(...)`
  	* 同BRE中的`\(...\)`

### BRE 优先级 >
  * `[...]` 方括号中的具体转义
  * `\metacharacter` 转义的meta字符
  * `[]` 方括号表达式
  * `\(...\)...\n` 子表达式后向引用
  * `\{...\}` * 单置字符重现
  * `...` 连续字符
  * `^ $` 锚点

### ERE 优先级 >
  * `[...]` 方括号中的具体转义
  * `\metacharacter` 转义的meta字符
  * `[]` 方括号表达式
  * `(...)...\n` 子表达式后向引用
  * `+ ? * {}` 单置字符重现
  * `...` 连续字符
  * `^ $` 锚点
  * `|` 选择
