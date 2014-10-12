---
layout: post
title: "Design Pattern (1)"
description: "simple factory, strategy, decorator, factory, proxy, prototype, template"
category: program
tags: ["design pattern", "python"]
---
{% include JB/setup %}

### 大话设计模式的读书笔记（一）
### Simple Factory, Strategy, Decorator, Factory, Proxy, Prototype, Template
#### 简单工厂模式
  * 其实工厂平常也用的非常多了、核心就是抽出公共外部接口、然后按照需求子类、然后由统一工厂返回。好处也很明显就是解耦、隔绝上层知道自己不需要知道的东西。
  * 用`python`实现了一端最简单的例子

  ```python
  class Operation:
      def __init__(self, a=0, b=0):
          self.number_a = a
          self.number_a = b
      # 抽象出公共的计算
      def getresult(self):
          assert False, "base method must be implement"


  class Add(Operation):
      def getresult(self):
          return self.number_a + self.number_b


  class Minus(Operation):
      def getresult(self):
          return self.number_a - self.number_b


  class Factory:
      @staticmethod
      def create_operation(operate):
          if operate == "+":
              return Add()
          elif operate == "-":
              return Minus()


  if __name__ == '__main__':
      op = Factory.create_operation("+")
      op.number_a = 1
      op.number_b = 5
      print op.getresult()
```
#### 策略模式
  * 我理解的策略模式其实就是给操作对象多wrap了一层context的东西、由他来抽象一堆方法进行管理。核心也是解耦把这部分脏东西控制在自己手上避免影响到上层
  * 其实类似`NSManagedObjectContext`这就是封装了真实数据底层的一些方法、让用户避免开这样噁心的东西、具体不同的数据媒介的相关操作让他自己处理即可。
  * 同样一个简单的例子、抽象出cash这个类、他的具体打折策略去由context去维护、整个这个打折这个事件全托管给context、类似一个中间人的角色

  ```python
  class CashSuper(object):
      def get_result(self):
          assert False, "abstract method must be implement"


  class CashNormal(CashSuper):
      def get_result(self):
          return self.origin * 0.9


  class CashRebate(CashSuper):
      def get_result(self):
          return self.origin - 300


  class CashContext:
      cash_super = None

      def __init__(self, type_str, money):
          if type_str == 0:
              self.cash_super = CashNormal()
          else:
              self.cash_super = CashRebate()
          self.cash_super.origin = money

      def get_result(self):
          return self.cash_super.get_result()


  if __name__ == '__main__':
      cc = CashContext(0, 900)
      print cc.get_result() 

  ```
#### 装饰模式
  * 装饰模式核心就是装饰不要去污染原来的东西、遵循开放封闭原则。例如一个人穿衣服、隔离出穿衣服这个事情。
  * 先写一端照书上的装饰模式的结构图写的代码
  
  ```python
  class Person(object):
      def __init__(self, name = None):
        self.name = name

      def show(self):
        print self.name


  class Finery(Person):
      person = None

      def decorate(self, person):
          self.person = person

      def show(self):
          self.person.show()



  class TShirt(Finery):
      def show(self):
          print "wear tshirt"
          super(TShirt, self).show()


  class Shoe(Finery):
      def show(self):
          print "wear shoe"
          super(Shoe, self).show()


  if __name__ == '__main__':
      p = Person("zx")
      ts = TShirt()
      sh = Shoe()

      ts.decorate(p)
      sh.decorate(ts)
      sh.show()
  ```

  * 感觉这样装饰模式虽然结构清楚、但是写起来感觉很难受、继承来继承去也麻烦、用了另外种装饰方法感觉明了简介更多

  ```python
  def wear_shoe(f):
      def wrapper(*args):
          print "wear shoe"
          f(*args)
      return wrapper


  def wear_tshirt(f):
      def wrapper(*args):
          print "wear Tshirt"
          f(*args)
      return wrapper


  class Person(object):
      def __init__(self, name):
          self.name = name

      def show(self):
          print self.name


  if __name__ == '__main__':
      p = Person("zx")
      f = wear_tshirt(wear_shoe(Person.show))
      f(p)
  ```
#### 工厂模式
  * 工厂其实主要就是工厂的抽象以及实体的抽象2部分、把实体的选择都抽象在工厂里、然后统一由工厂返回

  ```python
  from abc import ABCMeta, abstractmethod

  class AbstractFactory(object):
      __metaclass__ = ABCMeta

      @abstractmethod
      def createFactory(self):
          assert False, "abstract method must be implement"


  class Instance1(object):
      def __init__(self):
          print "instance1 alloc"

  class Factory1(AbstractFactory):
      def createFactory(self):
          return Instance1()


  class Instance2(object):
      def __init__(self):
          print "instance2 alloc"


  class Factory2(AbstractFactory):
      def createFactory(self):
          return Instance2()


  if __name__ == '__main__':
      instance = Factory1().createFactory()


  ```
#### 代理模式
  * 其实代理模式平常用的非常多、我所认为的核心是有两点
    * 隔离开他所需要操作的对象、使用户使用这个对象的方法大大减少保证正确
    * 类似一个callback的感觉在调真实对象时有个地方给你写需要做的别的事情
  * 比如html加载图片时碰到真的图片时都是弄个假的框框再去真的download图片大致套用了写模式

  ```python
  class ImageNetwork(object):
      def request(self):
          assert False, "abstract method must be implement"


  class ImageRequestProxy(ImageNetwork):
      def __init__(self):
          super(ImageRequestProxy, self).__init__()
          self.image_request = ImageRequestNetwork()

      def request(self):
          print "render ui"
          self.image_request.request()


  class ImageRequestNetwork(ImageNetwork):
      def request(self):
          print "download image"


  if __name__ == '__main__':
      p = ImageRequestProxy()
      p.request()

  ```
#### 原型模式
  * 一个词核心就是拷贝实现一个深拷贝就可以了
  * 比如js就是个非常经典的原型
  * 例子就不写了 Orz

#### 模版模式
  * 模版的话核心也是提出公共部分、在可变的部分抽象出公共接口给具体的实现去实现……各种web框架模版也是用烂了的……

  ```python
  class Template(object):
      def dosth(self):
          print "dosth"
          self.needsth()
      def needsth(self):
          assert False, "abstract method must be implement"


  class Detail(Template):
      def needsth(self):
          print "food"
  if __name__ == '__main__':
      Detail().dosth()
  ```