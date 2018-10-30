#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/10/26
import unittest


class BinarySearch(unittest.TestCase):
    def binary_search(self, list, num):
        # print list
        first = 0
        top = len(list)
        # print first , top

        while first < top :
         mid = (first + top) / 2
         if num == list[mid]:
           return mid
         if num < list[mid]:
           top = mid
         else:
           first = mid
        else:
            return None

    def test_search(self):
        print self.binary_search([1, 3, 5, 7, 9], 7)
