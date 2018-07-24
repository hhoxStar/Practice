# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:44:47 2018
练习7：
1使用多选其一，完成天气的提醒，淘宝客户端
2.一定要多次使用for循环 偶尔使用while 循环 在淘宝客户端中
3.使用到break 或者continue

@author: samsung
"""
##多选其一：
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def day(a,b):
    print(str(a)+'日')
    print('温度:'+str(data['list'][b]['main']['temp']))
    print('天气情况:'+str(data['list'][b]['weather'][0]['description']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('晴朗出门耍')
    if a=='Rain':
        print('有雨带上伞')
    if a=='Clouds':
        print('今日多云哦')
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)



###淘宝客户端
url=''
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def sale():
   for i in range(0,36):
       print(str(data['mods']['itemlist']['data']['auctions'][i]['title']))
       print(str(data['mods']['itemlist']['data']['auctions'][i]['view_price']))
       print(str(data['mods']['itemlist']['data']['auctions'][i]['view_sales']))
         
       y=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
       x=int(y[0:-3])
      
       if x>1000:
           print('销售火爆，爆款商品')
       elif x<=500:
           print('销量不错，小众爱好')
       elif x<=100:
           print('销量低迷，谨慎选购')
       while i==40:
           continue
       if i==35:
           break 
       if (i+1)%4==0:
           print('****'*10)
           
sale()   

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def z(b):
    print('商品名称'+str(a[b-1]['title'])+'商品价格'+str(a[b-1]['view_price']))
 
    
    



 
def y(a):
    for i in range(1,4):
        z(a*4-i)
        c='_'*6
        print(c)
for i in range(9):
    print(y(i))
    if i==4:
        break  
    else:
        continue
for i in range(9):
    if i==4:
         print(y(i))
    else:
        continue
for i in range(9):
    if i>4:
        print(y(i))
    else:
        continue
for i in range(0,9):
    if i<4:
        print(i)
    else:
        print(y(i))
        continue
    
   
        
    
        


    