---
date: 2014-10-14
layout: post
title: "Design Pattern (4)"
description: "bridge, command, chain of responsibility, mediator, flyweight, interpreter, visitor"
category: program
tags: ["design pattern", "python"]
---

### 大话设计模式的读书笔记（四）
  * [读书笔记（一）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-0/)
  * [读书笔记（二）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-1/)
  * [读书笔记（三）](http://snorlaxzxz.com/program/2014/10/11/design-pattern-2/)

### Bridge, Command, Chain Of Responsibility, Mediator, Flyweight, Interpreter, Visitor

#### 桥接模式
  * 桥接模式的定义为「将抽象不分与实现部分分离，使之可以独立变化」
  * 简单来说就比如python 把语言核心逻辑抽象出PVM具体实现根据是当前什么平台再分别处理、使用也使用的是抽象接口
  由实现者abstraction获得抽象的implementor并具体实现

  ```python
  	from abc import ABCMeta, abstractmethod
	class Implementor(object):
	    __metaclass__ = ABCMeta
	    
	    @abstractmethod
	    def operation(self):
	        pass


	class Abstraction(object):
	    def operation(self):
	        if self.implementor:
	            self.implementor.operation()
	        
	class ConcreteImplementorA(Implementor):
	    def operation(self):
	        print "implementor A"


	class ConcreteAbstraction(Abstraction):
	    def operation(self):
	        super(Abstraction, self).operation()


	if __name__ == '__main__':
	    ab = ConcreteAbstraction()
	    ab.implementor = ConcreteImplementorA()
	    ab.operation()
  ```

#### 命令模式
  * 命令模式是把一个请求进行多一道转移、通过一个统一的invoker进行一起的操作
  * 例如ios中dispatch_async等操作或者任意的线程池都是这个思路、任何request只管我来托管、具体怎么操作由我自己来决定这个模式也是非常常见的

	```python
	from abc import ABCMeta, abstractmethod

	class Command(object):
		__metaclass__ = ABCMeta

		def __init__(self, receiver):
			self.receiver = receiver

		@abstractmethod
		def execute(self):
			pass


	class ConcreteCommand(Command):
		def execute(self):
			self.receiver.action()


	class Receiver(object):
		def action(self):
			print "do sth"


	class Invoker(object):
		def set_command(self, command):
			self.command = command

		def execute_command(self):
			self.command.execute()


	if __name__ == '__main__':
		r = Receiver()
		c = ConcreteCommand(r)
		i = Invoker()
		i.set_command(c)
		i.execute_command()

	```

#### 职责链模式
  * 职责链模式的核心我理解的是把担负责任的对象抽象出公共、并对每个节点不关心其周边节点、只关心与他需要传递的节点核心好处就是避免了客户端上需要对整个职责具体模块的掌握、就像上班只需要关注上级领导即可
  * 具体来说还是拿ios来说、比如触碰下屏幕、他并不知道你点击的到底是哪儿个button、他一层层先给他的直接交互UIWindow然后再由他传递他的第一层view等等直到找到该负责的那个button为止。或者说就像一个request进服务器他并不知道他是给具体的业务是谁、他先去找nginx、然后nginx再去分发给相关的、再进到具体的某个业务层逻辑一样道理

	```python
	from abc import ABCMeta, abstractmethod

	class Handler(object):
		__metaclass = ABCMeta
		def set_successor(successor):
			self.successor = successor

		@abstractmethod
		def handle_request(request):
			pass


	class ConcreateHandler(Handler):
		def handle_request(request):
			if request > 0:
				print "deal it"
			else:
				if self.successor:
					self.successor.handle_request(request)


	if __name__ == '__main__':
		h = ConcreateHandler()
		h.set_successor(None)
		h.handle_request(1)

	```

#### 中介者模式
  * 其实这东西感觉是不是办法的办法。。虽然说初衷的确能够理解。举个例子就是有10个人、每个人和另外9个人都有一种接触方式、那么一共就有45种规则。并且每个人里都需要记录9种规则。于是就抽象出一个规则列表、里面记录了45种规则、所有的具体问题全去找中介者。也就是多对多的关系。
  * 不过我理解这种脏活也是在所难免的、比如一个UI层的渲染再怎么拆分开总有需要合并起来的地方、而上层拆的越开越清晰、倒霉的肯定是下层的强大逻辑。

	```python
	from abc import ABCMeta, abstractmethod
	class Mediator(object):
		__metaclass__ = ABCMeta

		@abstractmethod
		def send(self, message, colleague):
			pass


	class Colleague(object):
		def __init__(self, mediator):
			self.mediator = mediator


	class ConcreteMediator(Mediator):
		def set_colleague1(self, colleague):
			self.colleague1 = colleague

		def set_colleague2(self, colleague):
			self.colleague2 = colleague

		def send(self, message, colleague):
			if colleague == self.colleague1:
				self.colleague2.notify()
			else:
				self.colleague1.notify()


	class ConcreteColleague1(Colleague):
		def send(self, message):
			self.mediator.send(message, self)

		def notify(self):
			print "c1 dosth"

	class ConcreteColleague2(Colleague):
		def send(self, message):
			self.mediator.send(message, self)

		def notify(self):
			print "c2 dosth" 


	if __name__ == '__main__':
		m = ConcreteMediator()
		c1 = ConcreteColleague1(m)
		c2= ConcreteColleague2(m)
		m.set_colleague1(c1)
		m.set_colleague2(c2)
		c1.send("hi1")
		c2.send("hi2")

	```

#### 享元模式
  * 定义为「运用共享技术有效地支持大量细粒度的对象」核心的话就是抽出公共、独立出私有的。我太菜大概只能理解到除了省内存这一点而已。。

	```python
	from abc import ABCMeta, abstractmethod

	class Flyweight(object):
		def operation(self, extrinsicstate):
			pass


	class ConcreteFlyweight(Flyweight):
		def operation(self, extrinsicstate):
			print "do{0}".format(extrinsicstate)


	class UnSharedCOncreteFlyweight(Flyweight):
		def operation(self, extrinsicstate):
			print "unshared{0}".format(extrinsicstate)


	class FlyweightFactory(object):
		def __init__(self):
			self.flyweights = {}


		def get_flyweight(self, key):
			if key not in self.flyweights:
				self.flyweights[key] = ConcreteFlyweight()
			return self.flyweights[key]


	if __name__ == '__main__':
		f = FlyweightFactory()
		x1 = f.get_flyweight("x")
		x2 = f.get_flyweight("y")
		ux3 = UnSharedCOncreteFlyweight()

		x1.operation(1)
		x2.operation(2)
		ux3.operation(3)

	```

### 解释器模式
  * 大概我觉得我最喜欢这个了Orz……自己定义一套语法去解释一套东西而不去用各种复杂的OO的东西大概是我最喜欢的了……
  * 我又来qb vfl(Visual Format Language)了……同样是在ios里面把复杂的constraints抽象成一套自己定义的语言真是舒服级了。。。

	```python
	from abc import ABCMeta, abstractmethod

	class AbstractExpression(object):
		__metaclass__ = ABCMeta

		def __init__(self, context):
			self.context = context

		@abstractmethod
		def interpret(self, context):
			pass


	class TerminalExpression(AbstractExpression):
		def interpret(self, message):
			print "interpret {0} in {1}".format(message, self.context)


	class Context(object):
		pass


	if __name__ == '__main__':
		c = Context()
		t = TerminalExpression(c)
		t.interpret("dosth")
	```

#### 访问者模式
  * 我理解的访问者模式是把不同人在不同状态做的事情、2个数据model给解耦了。把状态全都丢进了一个公共处理的objectStructure、然后针对每个不同的访问者然后做出相应的处理
  * 访问者的有点是因为抽象出公共的处理部分了、所以再他的基础上添加新的行为非常方便，就多一种element而已、但是如果在数据结构层次的修改的话就蛋疼了。

	```python
	from abc import ABCMeta, abstractmethod

	class Visitor(object):
		__metaclass__ = ABCMeta

		@abstractmethod
		def visit_concrete_element_a(self, concrete_element_a):
			pass

		@abstractmethod
		def visit_concrete_element_b(self, concrete_element_b):
			pass


	class ConcreteVisitor1(Visitor):
		def visit_concrete_element_a(self, concrete_element_a):
			print '{0} was visited by {1}'.format(concrete_element_a, self)

		def visit_concrete_element_b(self, concrete_element_b):
			print '{0} was visited by {1}'.format(concrete_element_b, self)


	class Element(object):
		__metaclass__ = ABCMeta

		@abstractmethod
		def accept(self, visitor):
			pass


	class ConcreteElementA(Element):
		def accept(self, visitor):
			visitor.visit_concrete_element_a(self)

		def operation_a(self):
			print "do sth a"


	class ConcreteElementB(Element):
		def accept(self, visitor):
			visitor.visit_concrete_element_b(self)

		def operation_a(self):
			print "do sth b"


	class ObjectStructure(object):
		def __init__(self):
			self.elements = []

		def attach(self, element):
			self.elements.append(element)

		def detach(self, element):
			self.elements.remove(element)

		def accept(self, visitor):
			for e in self.elements:
				e.accept(visitor)


	if __name__ == '__main__':
		o = ObjectStructure()
		o.attach(ConcreteElementA())
		o.attach(ConcreteElementB())

		v1 = ConcreteVisitor1()

		o.accept(v1)

	```

### 后记
  * 用了4天读完了这本书、虽然说感觉书里面有些例子还是举的太过生硬、但总体来说还是帮助结构化的梳理了之前编程中碰到过的大量例子、两者结合起来才能理解的比较深刻。
  * 我理解学设计模式是学的解耦思想、核心透过几个原则来自己写代码、而不是为了OO而OO的生搬硬套。闭上眼睛想想之前自己的代码到底什么地方设计不合理等等也是可以回味不少的。
  * 这次里面所有的例子我都是用python实现的、其实用python这种活的脚本语言本来就不大适合严谨的设计模式、嘛不过总体来说也是一样的。
