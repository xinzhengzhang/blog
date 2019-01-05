---
layout: post
title: "wordpress迁移github page"
description: ""
category: program
tags: ["wordpress", "github"]
---

### 工作
1. host在github上
2. 安装jekyll bootstrap ~~简称jb~~
3. 导出wordpress评论以及内容
4. 处理wordpress的内容转化为markdown
5. 注意事项

#### host在github上
1. https://pages.github.com/
2. 新建一个username.github.io的repo
3. [绑定域名](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages)

#### 安装 jb
1. http://jekyllbootstrap.com/
2. 安装jekyll
3. clone代码 并看一下sample的样例以及api

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

#### 注意事项
1. 中文路径在github上跑起来没问题，但是本地调试时会报错

  ```ruby
    % LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8" be jekyll build --trace
    Configuration file: /Users/albertogg/Documents/beyondalbert.github.com/_config.yml
                Source: /Users/albertogg/Documents/beyondalbert.github.com
           Destination: /Users/albertogg/Documents/beyondalbert.github.com/_site
          Generating...
    /Users/albertogg/Documents/Github/jekyll/lib/jekyll.rb:121:in `gsub!': invalid byte sequence in US-ASCII (ArgumentError)
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll.rb:121:in `sanitized_path'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/post.rb:276:in `destination'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/cleaner.rb:43:in `block in new_files'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:420:in `block (2 levels) in each_site_file'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:419:in `each'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:419:in `block in each_site_file'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:418:in `each'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:418:in `each_site_file'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/cleaner.rb:43:in `new_files'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/cleaner.rb:24:in `obsolete_files'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/cleaner.rb:15:in `cleanup!'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:255:in `cleanup'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/site.rb:44:in `process'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/command.rb:43:in `process_site'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/commands/build.rb:46:in `build'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/commands/build.rb:30:in `process'
        from /Users/albertogg/Documents/Github/jekyll/lib/jekyll/commands/build.rb:17:in `block (2 levels) in init_with_program'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary/command.rb:220:in `call'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary/command.rb:220:in `block in execute'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary/command.rb:220:in `each'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary/command.rb:220:in `execute'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary/program.rb:35:in `go'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/gems/mercenary-0.3.3/lib/mercenary.rb:22:in `program'
        from /Users/albertogg/Documents/Github/jekyll/bin/jekyll:18:in `<top (required)>'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/bin/jekyll:23:in `load'
        from /Users/albertogg/.rbenv/versions/2.1.2/lib/ruby/gems/2.1.0/bin/jekyll:23:in `<main>'
    ```
  * 详见这个<https://github.com/jekyll/jekyll/issues/2379> 修改了报错那行为
  ```ruby
    clean_path.force_encoding('UTF-8').gsub!(/\A\w\:\//, '/')
  ```
2. 使用里面的代码高亮很不爽可以参见gfm使用他的语法并在config中调整配置
  ```
    markdown: redcarpet
    redcarpet:
      extensions: ["no_intra_emphasis", "fenced_code_blocks", "autolink", "strikethrough", "superscript"]
  ```
3. 代码高亮开启了pygments后的css也需要自己配置来写
  * 可以参加<https://github.com/richleland/pygments-css>
