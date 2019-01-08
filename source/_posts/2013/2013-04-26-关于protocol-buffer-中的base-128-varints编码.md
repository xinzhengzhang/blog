---
date: 2013-04-26
layout: post
title: 关于protocol-buffer-中的base-128-varints编码
categories:
- program
---
### 工作
1. host在github上
2. 安装jekyll bootstrap~~简称jb~~
3. 导出wordpress评论以及内容
4. 处理wordpress的内容转化为markdown
5. 注意事项

#### [host在github上](https://pages.github.com/)
1. 新建一个username.github.io的repo
2. [绑定域名](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages)

#### [安装~~jb~~](http://jekyllbootstrap.com/)
1. 安装jekyll
2. clone代码 并看一下sample的样例以及api

***

#### 导出wordpress评论以及内容
* 导出评论
  * 由于github page采用的是纯静态的、评论这种那么麻烦的东西索性还是交给第三方好啦= =在github上我使用的是[disqus](http://disqus.com/)，他也同时提供从wordpress导出的功能
    * 创建 disqus账号 <disqus.com/admin/create>
    * 添加自己的site并安装wp插件 <http://wordpress.org/plugins/disqus-comment-system/>
    * 等待disques后台进程帮你抓完会通知你的
* 导出内容
  * 导出content 使用wordpress的导出工具导出xml即可

#### 转换内容
* 导出mark down
  * ~~jekyll 有一个jekyll-import 的工具、不过中文支持的巨差无比~~
  * 使用一个改进过对中文支持的版本 <https://gist.github.com/chitsaou/1394128>
  * 导出的xml命名 (wordpress.xml) 如下命令会把为你生成一拖post 以及wordpress中的page
  ```ruby
  ruby -r "./wordpressdotcom.rb" -e "Jekyll::WordpressDotCom.process"
  ```
  * 如果在wordpress中没有使用什么插件类似**codebox**这样的到这一步就导入成功了
  * 如果使用了一些奇怪的语法在html用插件解出来的格式就一塌糊涂了，比如我的所有的代码都是用codebox的……
  写了一段简单的脚本来处理html，基本思路都是文本解析到codebox的开始标签pre然后替换掉
  ```python
  __author__ = 'zhangxinzheng'
# -*- coding: utf-8 -*-
import sys
import re
import os
def f(filename):
    if filename.find("html") == -1:
        return
    targetName = filename.replace("html","md")
    fd = open(filename, "r+")
    str = ''.join(fd.readlines())
    while str.find("<pre") != -1:
        tempString="\n```\n"
        isContent = False
        startIndex = str.find("<pre")
        endIndex = len(str)
        realEnd = startIndex
        leftCount = 1
        rightCount = 0
        for j in xrange(startIndex, endIndex):
            if str[j] == '<':
                isContent = False
                leftCount +=1
            if isContent:
                tempString+=str[j]
            if str[j] == '>':
                isContent = True
                rightCount +=1
                realEnd = j
            if leftCount == rightCount:
                break
        str+="\n```\n"
        str=str.replace(str[startIndex:realEnd], tempString)
    fd.close()

    fd = open(targetName, "w+")
    fd.write(str)
    fd.close()
    os.remove(filename)

if __name__ == "__main__":
    for i in sys.argv:
        f(i)
  ```
