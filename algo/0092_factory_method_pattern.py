# coding: utf-8
""" 
@author: lipeng
@file: 0092_factory_method_pattern.py 
@time: 2019/12/20
"""
from abc import ABCMeta, abstractmethod

"""
工厂方法：(对象创建型模式)

意图：定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到子类

适用性:当一个类不知道它所必须创建的对象的类的时候
      当一个类希望由他的子类来指定它所创建的对象的时候
      当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理这一信息局部化的时候

参与者：Product:定义工厂方法所创建的对象的接口
       ConcreteProduct:实现Product接口
       Creator：声明工厂方法，该方法返回一个Product类型的对象。Creator也可以定义个工厂方法的缺省实现，
                它返回一个缺省的ConcreteProduct对象
       ConcreteCreator:冲定义工厂方法以返回一个ConcreteProduct对象
协作：Creator依赖于它的子类来定义工厂方法，所以它返回一个适当的ConcreteProduct实例

效果：为子类提供挂钩
     连接平行的类层次
"""


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def manufacture(self):
        pass


class IProduct(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass


class ProductA(IProduct):
    def show(self):
        print("生产出了产品A")


class ProductB(IProduct):
    def show(self):
        print("生产出了产品B")


class FactoryA(IFactory):
    def manufacture(self):
        return ProductA()


class FactoryB(IFactory):
    def manufacture(self):
        return ProductB()


# if __name__ == "__main__":
#     factory: IFactory = FactoryA()
#     product: IProduct = factory.manufacture()
#     product.show()
#
#     factory2: IFactory = FactoryB()
#     product2: IProduct = factory2.manufacture()
#     product2.show()
"""
或者更高级一些的实现
"""


class IProduct(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass


class ProductA(IProduct):
    def show(self):
        print("生产出了产品A")


class ProductB(IProduct):
    def show(self):
        print("生产出了产品B")


class Factory:
    def __init__(self, product_type):
        self.product_type = product_type

    def manufacture(self):
        if self.product_type == 1:
            return ProductA()
        if self.product_type == 2:
            return ProductB()


if __name__ == "__main__":
    factory: IFactory = Factory(1)
    product_a: IProduct = factory.manufacture()
    product_a.show()
    factoryb: IFactory = Factory(2)
    product_b: IProduct = factoryb.manufacture()
    product_b.show()
