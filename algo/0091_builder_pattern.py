# coding: utf-8
""" 
@author: lipeng
@file: 0091_builder_pattern.py 
@time: 2019/12/20
"""
from abc import ABCMeta, abstractmethod
import unittest

"""
建造者模式

意图：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不通的表示

适用性
    1.当创建复杂对象的算法应该独立于该对象的组成部分以及他们的装配方式时
    2.当构造过程必须允许被构造的对象有不同的表示时
参与者
    Builder:为创建一个Product对象的各个部件指定抽象接口
    ConcreteBuilder:实现Builder的接口以构建和装配该产品的各个组件
                    定义并明确它所创建的表示
                    提供一个检索产品的接口
    Director:构造一个使用Builder接口的对象
    Product：表示被构造的复杂对象。ConcreteBuilder创建该产品的内部表示并定义它的装配过程
            包含定义组成部件的类，包括将这些部件装配成最终的产品的接口
协作：客户创建Director对象，并用它所想要的Builder对象进行配置
     一旦产品部件被生成，导向器就会通知生成器
     生成器处理导向器的请求，并将部件加到该产品中
     客户从生成器中检索产品
效果：它使你可以改变一个产品的内部表示
     他将构造代码和表示代码分开
     它使你可对构造过程进行更精细的控制
"""


class Computer:
    def __init__(self):
        self.cpu = ""
        self.hard_disk = ""
        self.main_board = ""
        self.memory = ""


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def create_cpu(self, cpu: str):
        pass

    @abstractmethod
    def create_hard_disk(self, hard_risk: str):
        pass

    @abstractmethod
    def create_main_board(self, main_board: str):
        pass

    @abstractmethod
    def create_memory(self, memory: str):
        pass

    @abstractmethod
    def create_computer(self) -> Computer:
        pass


class AssembleBuilder(Builder):

    def __init__(self):
        self.computer = Computer()

    def create_cpu(self, cpu: str):
        self.computer.cpu = cpu

    def create_hard_disk(self, hard_risk: str):
        self.computer.hard_disk = hard_risk

    def create_main_board(self, main_board: str):
        self.computer.main_board = main_board

    def create_memory(self, memory: str):
        self.computer.memory = memory

    def create_computer(self) -> Computer:
        return self.computer


class Director:

    def __init__(self, builder: Builder):
        self.builder = builder

    def create_computer(self, cpu: str, hard_disk: str, main_board: str, memory: str):
        self.builder.create_cpu(cpu)
        self.builder.create_hard_disk(hard_disk)
        self.builder.create_main_board(main_board)
        self.builder.create_memory(memory)
        return self.builder.create_computer()


builder: Builder = AssembleBuilder()
directory: Director = Director(builder)
computer: Computer = directory.create_computer("Intel 酷睿i9 7900X", "三星M9T 2TB （HN-M201RAD）",
                                               "技嘉AORUS Z270X-Gaming 7", "科赋Cras II 红灯 16GB DDR4 3000")
computer: Computer = computer
print(computer.memory)
print(computer.cpu)