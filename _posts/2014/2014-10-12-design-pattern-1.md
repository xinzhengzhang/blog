---
layout: post
title: "Design Pattern (2)"
description: "facade, builder, observer, abstract factory"
category: program
tags: ["design pattern", "python"]
---
{% include JB/setup %}

### 大话设计模式的读书笔记（二）
  * [读书笔记（一）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-0/)
  
### Facade, Builder, Observer, Abstract Factory

#### 外观模式
  * 外观模式大概不就是个封装……说好听点他的定义是「为系统中一组接口提供一个一致的界面」核心就是把业务层的复杂逻辑全部抽出来给另外一个替死鬼来干ˊ_>ˋ
  * 代码也不想写了、举个例子比如老师管理收作业要去不会去盯每个学生、会选个班长把脏活都丢给他来做……自己只要简单的去和班长交流就好了

#### 建造者模式
  * 建造者模式我理解核心有一点是强制把一些必须实现的东西抽象到上层通过虚方法强制必须实现。这样可以极大的有效的防止使用的时候漏掉了某一个步骤
  * 另外一个是他有一个叫导演的概念、整个建造的方法整段逻辑托管给了这个导演而不会暴露给最上层去担忧这个事情

  ```python
  class Product(object):
      def __init__(self):
          self.parts = []
      def add(self, part):
          self.parts.append(part)
      def show(self):
          for i in self.parts:
              print i

  from abc import ABCMeta, abstractmethod
  class Builder(object):
      __metaclass__ = ABCMeta

      @abstractmethod
      def build_part_a(self):
          pass

      @abstractmethod
      def build_part_b(self):
          pass

      @abstractmethod
      def get_result(self):
          pass
      
  class ConcreteBuilder1(Builder):
      def __init__(self):
          self.product = Product()

      def build_part_a(self):
          self.product.add("partA")

      def build_part_b(self):
          self.product.add("partB")

      def get_result(self):
          return self.product


  class Director(object):
      @staticmethod
      def construct(builder):
          builder.build_part_a()
          builder.build_part_b()


  if __name__ == '__main__':
      b = ConcreteBuilder1()
      Director.construct(b)
      p = b.get_result()
      p.show()

  ```

#### 观察者模式
  * 我想这个东西熟悉ios的人一定不会陌生、ios中kvo的使用简直是不能再棒、那为什么客户端超级适用这个模式我想大家也应该想到了是因为客户端因为是个超级重交互的东西、例如UI层的重新render每次都需要前段手动进行这么一下简直是不能忍的
  * 观察者模式核心的话我认为是一种定义了一个一对N的关系、并且一去和N中的一个进行交互、一旦触发同时去触发剩下另外的N－1个。例如ios的UIVIew会去observe他的rect、一旦这一个rect进行变化、他会自己去触发绑定的一坨逻辑例如render等等
  * 写了一个很简单的UI的模拟 rect就简单变成kvo一个int了

  ```python
  from abc import ABCMeta, abstractmethod
  class ISth(object):
      __metaclass__ = ABCMeta
      @abstractmethod
      def notify(self):
          pass


  class View(ISth):
      def __init__(self):
          self.handler = [self.render]
          self._rect = 0
     
      @property
      def rect(self):
          return self._rect

      @rect.setter
      def rect(self, value):
          self._rect = value
          self.notify()

      def notify(self):
          for i in self.handler:
              i()

      def render(self):
          print "i am render"


  if __name__ == '__main__':
      v = View()
      v.rect = 5

  ```
#### 抽象工厂模式
  * 好吧……抽象工厂模式其实就是工厂的再一步进化……核心就是本来子类到底是什么是交给具体适用场景去决定的、而抽象工厂把这部分也给抽走了
  * 说具体点两者的差别的话就是类似多个route的东西、由他来决定到底把工厂route到哪儿个子类去，然后表示用一坨switch case太丑陋了，然后用了反射来处理、我就大致写下python的反射好了= =具体的工厂大同小异了

  ```python
  module = __import__(__name__)
  class_ = getattr(module, "xxx")
  ```