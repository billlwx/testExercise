#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/3/25
import random

# 冒泡排序 效率低
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

date =list(range(10000))
random.shuffle(date)
bubble_sort(date)
print date