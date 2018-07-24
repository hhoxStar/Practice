# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:38:41 2018
练习11:可视化展示
1.获取学校名
2.获取学校招生人数
3.在Echarts展示

@author: samsung
"""
ls=open('湖北学校.txt',encoding='gbk').readlines()
schoolls=[]
numls=[]
f1=open('学校名称.txt','a',encoding='utf-8')
f2=open('学校招生人数.txt','a',encoding='utf-8')
for line in ls:
    schoolls.append(line.split(',')[0][1:])
    numls.append((line.split(',')[1][0:-2]))
f1.write(str(schoolls))
f2.write(str(numls))
f1.close()
f2.close()

