---
layout: post
title: "Begin With Swift"
description: ""
category: program
tags: ["swift", "objective-c", ]
---
{% include JB/setup %}

### OC Swift混编

* [大家好我是传送门= =](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/BuildingCocoaApps/index.html)
* 其实官方文档里写的各种东西也非常清楚的、我就用简单的描述下

* swift
  	* 如果需要引入同样的swift代码、只需要直接用就可以了！！！ (总之我也不知道工程索引文件什么的ide悄悄藏在什么地方了……
  	* 如果需要引入oc代码、首先需要生成一个`ProductName-Bridging-Header.h`的头文件(倒入随便一个oc文件就自动生成了)
    然后只需要把所有需要用到的oc头文件在这个header import进去，你的swift代码就可以随意这些类了！！(黑科技就是auto complete的时候怎么把oc的头文件自动转成swift的头文件的！！完全不知道ide偷偷的去哪儿生成了这些中间代码Orz……
* objective-c
	  * 如果需要引入oc代码= =原来怎么搞现在怎么搞= =怎么说都感觉是废话= =
    * 如果需要引入swift代码、首先在setting中打开`Defines Module`为YES、然后在需要使用的那个oc的 .m文件中引入 `#import "ProductModuleName-Swift.h"` 文档里的用`<>`引的应该是别的framework的依次类推、其中ProductModuleName可以在setting中设置
    **这个文件不需要自己新建**ide在一个很奇怪的角落里建好了……
* 混编完全无痛吧_(:з”∠)_

### swift 语法特点 (粗略)
* [The Swift Programming Language (以下略为书)](https://itunes.apple.com/book/swift-programming-language/id881256329?mt=11&ign-mpt=uo%3D4)
* 类型推断、参数约束描述等等 见如下

    ```
    func anyCommonElements <T, U where T: Sequence, U: Sequence, T.GeneratorType.Element: Equatable, T.GeneratorType.Element == U.GeneratorType.Element> (lhs: T, rhs: U) -> Bool {
      for lhsItem in lhs {
          for rhsItem in rhs {
              if lhsItem == rhsItem {
                  return true
              }
          }
      }
      return false
    }
    anyCommonElements([1, 2, 3], [3])
    ```

* optional
  * 在swift加入了两个语法糖一样性质的! 和 ? 分别是拆包 装包
  * 可以用在一些判空的地方例如
  ```
  //任意一个为空就中止不会走下去了、类似oc中的对nil perferselector不会crash一样
  john.residence?.address?.buildingIdentifier() {}
  ```
  * 包的感觉类似这样的感觉 例如函数中定义的是String 而你的 var a: String? 传入String要保证非空就必须一次解包操作如果这个时候值为空就crash

      ```
      enum Optional<T> {
        Some(T)
        None
      }
      ```

* 闭包、oc的block折腾够了么……好吧这回终于有简单明了爽快的闭包了Orz
  * 一般定义

    ```
    {
      (arg1: Type, arg2: Type) -> returnType in
      closure content
    }
    ```
  * sort Array

    ```
    var l: Array = [3, 4, 6, 1, 2]
    sort(l, {
      (i1: Int, i2: Int) -> Bool in
      return i1 > i2
      })
    //嫌烦里面的type可以被推断出来所以可以省略
    sort(l, {i1, i2 in return i1 > i2})
    //还可以更短= =
    sort(l, { $0 > $1})
    //还他妈可以更短！= =
    sort(l, >)
    ```

  * 注意一些循环引用的这些东西
    * unowned 弱引用非空对象(不init 编译器还报错
    * weak 弱引用可空的wrap过的对象就是那些加?的
  * 详情可见书245页

* setter getter willSet didSet
  * 类似c#的大大简化工作量……java那种seter getter去死吧混蛋！

* 碉堡的switch case……妈妈再也不用担心我一排if了= = 见书179页
* 还有各种符号重载、特别是`[]`也是非常的方便！(不过有一大堆关键字Orz 见书619页

* 更多
   * 还有各种各样的特性从脚本语言过来的话应该都是非常熟悉的比如返回个`tuple`什么的啦字典`keyvalue遍历`啦`for _ in 1..5`这种写法啦、oc的一些类似category那样的写法同样也由extension保留了下来
   * 一言以蔽之、swift的语法特性简直就是叼炸天、完全不觉得这个是Apple出的toy language、嗯就是这样啦！
   * redcarpet快支持swift吧……没语法高亮好不爽！

### 感想
* 2014wwdc苹果新发表的语言嘛、不知道为什么就是特别的热= =难道跟名字有关么(听说swift贴吧都被占领了23333
* 实际体验了下完全不知道苹果用什么黑科技bridge oc 和 swift的，除了代码提示几乎没有之外几乎两个语言完全自然连接的
* 粗粗把[The Swift Programming Language](https://itunes.apple.com/book/swift-programming-language/id881256329?mt=11&ign-mpt=uo%3D4)、有种特别熟悉的感觉……互联网上讨论也特别多、有厨有黑、包括各种媒体什么的也插一脚很多人都说像python，我倒是不怎么觉得，倒是各种语言的影子都可以看到一些而且东西特别多……不过脑补都知道完全用起来的话肯定很爽
* xcode6的bug特别多……
  * background 他是边写代码就一边在跑的所以比如 `system(rm -rf ~/)`这种命令> <
  * 群里看到的一句话干崩xcode…… `var b = 1; println("a", b)`
  * 小tips
    * 开始纯粹练语法的话比较那个background比较核心……还不如用cli模式进去打了试东西目录在</Applications/Xcode6-Beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/>
    可以 `PATH=$PATH:/Applications/Xcode6-Beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/` 然后命令行swift进cli试验(这样就算挂了也不会xcode无限重启> <

***
