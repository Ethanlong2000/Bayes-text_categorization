# This is a sample Python script.
import os
import jieba
import random
from collections import Counter
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# txts=[]
# position= "D:\workspace\Bayes\中文停用词库.txt"
# with open(position, "r",encoding='utf-8') as f:  # 打开文件
#     data = f.read()  # 读取文件
#     txts.append(data)
# txts = ','.join(txts)
# word_list = list(jieba.cut(txts))
# set(word_list)
# print(word_list)



# def shuffel(lst):
#     l = len(lst)
#
#     if l <= 1:
#         return lst
#     i = 0
#     while l > 1:
#         p = int(random.random() * l)
#         lst[i], lst[i + p] = lst[i + p], lst[i]
#         i += 1
#         l -= 1
#     return lst
#
#
# print(shuffel([1, 2, 2, 3, 3, 4, 5, 10]))
# a=[1,1,1,1,1,1, 2, 2, 2,2,2,3, 3, 4, 5, 10]
# P=Counter(a)
# # for i in range(1,4):
# #    print(P.get(i))
# if 10 in P.keys():
#    print(P.keys())
# accuracy=1
# FOLD_NUM=0
# precision=4
# recall=5
# print("第" ,FOLD_NUM + 1, "折验证的结果为:" , '\n'
#               "准确率为：" ,accuracy , '\n'
#          "精准率为：" , precision , '\n'
#              "召回率为：" , recall , '\n'
#
#       )