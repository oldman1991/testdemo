# coding=utf-8
# create by oldman at 2018/6/12
"""
面向对象的实现
"""
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelituy')


class LineItem(object):
    """
    :param
    """

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):
    """
    上下文
    """

    def __init__(self, customer, cart, promotion):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        """

        :return:
        """
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        """

        :return:
        """
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total : {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    """
    :param
    """

    @abstractmethod
    def discount(self, order):
        """
        返回折扣金额(正值)
        :param order:
        :return:
        """


class FidelityPromo(Promotion):
    """为积分为1000或以上的顾客提供5%z折扣"""

    def discount(self, order):
        """

        :param order:
        :return:
        """
        return order.total() * .05 if order.customer.idelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """
    单个商品为20个或以上时提供10%折扣
    :param
    """

    def discount(self, order):
        """

        :param order:
        :return:
        """
        discount = 0
        for item in order.cat:
            if item.quantity >= 20:
                discount += item.total() * .1

        return discount


class LargOrderPromo(Promotion):
    """
    订单中的不同商品达到10个或以上时提供7%折扣
    """

    def discount(self, order):
        """

        :param order:
        :return:
        """
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07


"""
>>> joe = Customer('John', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banner', 4, .5),
...         LineItem('apple', 10, 1.5)
...         LineItem('watermellon', 5, 1.5)]
>>> Order(joe, cart, FidelityPromo())

"""

"""
Order类和函数实现的折扣策略
"""


class Order(object):
    """
    上下文
    """

    def __init__(self, customer, cart, promotion):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        """

        :return:
        """
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        """

        :return:
        """
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total : {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(self, order):
    """
    为积分为1000或以上的顾客提供5%z折扣
    :param order:
    :return:
    """
    return order.total() * .05 if order.customer.idelity >= 1000 else 0


def bulk_item_promo(self, order):
    """
    单个商品为20个或以上时提供10%折扣
    :param order:
    :return:
    """
    discount = 0
    for item in order.cat:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


def large_order_promo(order):
    """
    订单中的不同商品达到10个或以上时提供7%折扣
    :param order:
    :return:
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07

"""

>>> joe = Customer('John', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banner', 4, .5),
...         LineItem('apple', 10, 1.5)
...         LineItem('watermellon', 5, 1.5)]
>>> Order(joe, cart, fidelity_promo)

"""