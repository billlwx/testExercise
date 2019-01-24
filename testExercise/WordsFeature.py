#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/1/24

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# 任一个英文的纯文本文件，统计其中的单词出现的个数。任一个英文的纯文本文件，统计其中的单词出现的个数。
vectorizer = CountVectorizer()
text_path = r"pages.txt"  #utf-8 without BOM
with open(text_path, 'r') as f:
    s = f.readlines()
    X = vectorizer.fit_transform(s)
words = vectorizer.get_feature_names()
counts = np.sum(X.toarray(), 0).tolist()
results = sorted(zip(words, counts), key=lambda x:x[1], reverse=True)
for word, count in results: # print results
    print word, count