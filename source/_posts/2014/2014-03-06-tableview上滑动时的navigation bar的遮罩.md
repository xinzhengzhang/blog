---
date: 2014-03-06
layout: post
title: "tableview上滑动时的navigation bar的遮罩"
description: ""
category: program
tags: []
---

这个需求本来并不复杂、烦人的几乎这端遮罩代码要复用到每个tablview所在的场景、非常的不合适、直到看到了前辈写的一段hack到暴的代码才深知道所在的差距……
他大致的思路就是给scrollview拓展了一个category、利用ios的运行时的特性、在他load的时候直接把他的setContenOffset给替换掉成了自己的函数、用他来控制公共的navigationbar
代码如下

```objective-c
@interface UIScrollView (ContentOffset)

+ (void)load; //复写掉load方法

@end

@implementation UIScrollView (ContentOffset)

+ (void)load
{
    method_exchangeImplementations(class_getInstanceMethod(self, @selector(setContentOffset:)), class_getInstanceMethod(self, @selector(swizzled_setContentOffset:)));//替换原生的与自己重写的
}

- (void)swizzled_setContentOffset:(CGPoint)point
{
    [self swizzled_setContentOffset:point];//由于此时已经被交换了所以调用自己相当于是在调原生的setContOffset

    ZDDeckViewManager *deck = [ZDDeckViewManager sharedInstance_ks];//单例拿到大家一起控制的navigationbar
    /*这里就可以在滑动状态上对bar做任何事情了*/
}

@end
```
