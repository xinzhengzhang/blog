---
layout: post
title: "Design Pattern (3)"
description: "state, adapter, memento, composite, singleton"
category: program
tags: ["design pattern", "python"]
---

### 大话设计模式的读书笔记（三）
  * [读书笔记（一）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-0/)
  * [读书笔记（二）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-1/)
  * [读书笔记（四）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-3/)


### State, Adapter, Memento, Composite, Singleton

#### 状态模式
  * 理解状态核心就是让一个封闭的东西自己决定自己该干嘛、而如何让他自己决定就是给他自己一个状态
  * 例如button一个按钮他就有多种状态、而他的行为都是被按上去、由他自己来决定自己要做什么

  ```python
  from abc import ABCMeta, abstractmethod
  class State(object):
      __metaclass__ = ABCMeta
      @abstractmethod
      def dosth(self):
          pass


  class Pressed(State):
      def dosth(self, button):
          print "do sth 1"
          button.state = Normal()


  class Normal(State):
      def dosth(self, button):
          print "do sth 2"
          button.state = Pressed()


  class Button(object):
      def __init__(self):
          self.state = Normal()

      def press(self):
          self.state.dosth(self)


  if __name__ == '__main__':
      b = Button()
      b.press()
      b.press()

  ```

#### 适配器模式
  * adapter的核心是把一些接口不兼容的一些类可以被统一的一起工作
  * 例如在客户端一个page需要展示的格式不止一种、比如他有两个tab通过切换实现两套数据、而具体他们的实现其实并不可以保证接口一定统一这个时候就可以使用adapter
  * 最好的例子就是android的adapter、adapter就起了桥接AdapterView与里面具体data的作用，可以一个Adapter这样的类兼容很多展示工作
  * 同理ios中对一个比较复杂的viewController可以参考android中的adapter模式把里面的多种情况抽离开来在最上层再统一的塞进去、例如拆开tableView等的delegate dataSource进去

#### 备忘录模式
  * 具体定义为不破坏封装性的前提下，不活一个对象的内部状态并可以随时恢复
  * 这个也是用烂了的东西……比如在各种canvas绘图时对各种变量设置的save restore
  * 例如`CGContextSaveGState`和`CGContextRestoreGState`这一对api
  * 书上的正经的写法是这样的反正我个人认为是极大的不喜欢……感觉纯粹是为了OO而OO的产物

  ```python
  class Memento(object):
      def __init__(self, state):
          self.state = state 


  class Originator(object):
      def __init__(self):
          self.state = 1

      def create_memento(self):
          return Memento(self.state)

      def restoreMemento(self, memento):
          self.state = memento.state


  class Caretaker(object):
      def __init__(self):
          self.memento = None


  if __name__ == '__main__':
      o = Originator()
      c = Caretaker()
      c.memento = o.create_memento()
      o.state = 2
      o.restoreMemento(c.memento)

  ```

#### 组合模式
  * 理解的核心就是这就是颗树、然后对上层调用者来说他只关心他、并不关心他下面的节点、比如他不关心他控制的是一个节点还是一棵树
  * 又拿ios做例子了……比如`UIView`你你根本不用去关系到底这个view只有一层还是有一坨subview……
  * 有一点需要比较注意的就是非常有可能因为这棵树的结构是一样的导致很多相应的节点实现起来会很难受因为很多别的节点的方法自己并没有的。在这里书上其实主要选择两种方法、具体用哪儿种其实我还是倾向透明的好、毕竟调空也没什么问题啦……
    * 透明方式 暴露出这些节点方法、具有一致的行为接口、空着去实现
    * 安全方式 不去实现这些方法、在上层调用的时候需要做相应的判断

#### 迭代器模式
  * 迭代器模式提供了一种方法顺序访问一个聚合对象的各个元素、且不暴露内部
  * 就像python一个list根本其实不需要在意list中每一个到底是什么东西只需要知道我可以一个个的取就够了
  * 这个模式已经甚至进化成语言特性了

#### 单例模式
  * 也是比较用烂的、我其实理解单例就是那些需要类似写面向过程的代码、没办法的通路= =
  * 单例的定义就是保证一个类仅只能又一个实例
  * 写一个python的单例

  ```python
  def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
      if class_ not in instances:
          instances[class_] = class_(*args, **kwargs)
      return instances[class_]
    return getinstance

  @singleton
  class MyClass(BaseClass):
    pass
  ```