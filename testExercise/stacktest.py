#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/10/22
import unittest

from mytest.Stack import Stack

stackA = Stack()
stackB = Stack()

class mytest(unittest.TestCase):

    def enQueue(self,element):
        stackA.push(element)

    def deQueue(self):
        if stackB.is_empty():
            if stackA.is_empty():
                return None
            else:
                self.transfer()
        return stackB.pop(stackB.peek())

    def transfer(self):
        while not stackA.is_empty():
            stackB.push(stackA.pop(stackA.peek()))

    def test_stack(self):

        self.enQueue(1)
        self.enQueue(2)
        self.enQueue(3)
        print stackA.show(),stackB.show()
        self.deQueue()
        print stackA.show(), stackB.show()
        self.deQueue()
        print stackA.show(), stackB.show()
        self.enQueue(4)
        print stackA.show(), stackB.show()
        self.deQueue()
        print stackA.show(), stackB.show()