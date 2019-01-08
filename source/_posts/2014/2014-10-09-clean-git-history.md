---
date: 2014-10-09
layout: post
title: "Clean Git History"
description: ""
category: program
tags: ["git"]
---

### 背景
* 不当心在git里塞进了几个大的静态文件……导致整个git repo大的无法忍于是开始清理
  * 核心的东西是使用`filter-branch` (好像这玩意是用来的原始意图不是这个= = [我是传送门](https://help.github.com/articles/remove-sensitive-data/) 
  * 查找大文件部分主要参照[这篇blog](http://naleid.com/blog/2012/01/17/finding-and-purging-big-files-from-git-history)

### 具体的操作三步
* 从git历史里找出大文件
  * 对所有文件的sha进行输出 `git rev-list --objects --all | sort -k 2 | uniq > allsha.txt`
  * 排序得到所有打文件列表 

  ```
  git gc && git verify-pack -v .git/objects/pack/pack-*.idx | egrep "^\w+ blob\W+[0-9]+ [0-9]+ [0-9]+$" \
  | sort -k 3 -n -r \
  > bigobjects.txt
  ```
  * 映射sha值得到所有大文件的path列表

  ```
    for SHA in `cut -f 1 -d\  < bigobjects.txt`; do
      echo $(grep $SHA bigobjects.txt) $(grep $SHA allsha.txt) | \
      awk '{print $1,$3,$7}' >> bigtosmall.txt
    done;
  ```
* 用filter-branch修改掉历史记录
  * 其中的Rakefile 就是在上一步中找寻出来的大文件 这里支持通配符的:)

  ```
  git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch Rakefile' \
  --prune-empty --tag-name-filter cat -- --al
  ```
  * push回主干
    `git push origin master --force`
* 用gc清理
  * `rm -rf .git/refs/original/`
  * `git reflog expire --expire=now --all`
  * `git gc --prune=now`
  * `git gc --aggressive --prune=now`

#### 这次成果成功把.git 从130M成功清理成5M哦耶！