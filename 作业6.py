# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:25:15 2018
练习6
1.每一行显示4个商品然后打印分割线，只要第一个36个商品
2.列出36个商品3
3.获取所有的商品价格并给商品排序，从高到低排序
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示
@author: samsung
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)


def skirt():
    for p in range(0,36):
         print('商品'+str(p+1))
         print('商品名称:'+str(data['mods']['itemlist']['data']['auctions'][p]['title']))
         print('商品价格:'+str(data['mods']['itemlist']['data']['auctions'][p]['view_price']))
         print('商品产地:'+str(data['mods']['itemlist']['data']['auctions'][p]['item_loc']))
         print('店铺:'+str(data['mods']['itemlist']['data']['auctions'][p]['nick']))
         if((p+1)%4==0):
              print('#'*40)
skirt()



ls=[]
def price():
    for i in range(0,36):                                                                                                               
      p=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
      print('')
      ls.append(p)
    return ls
price()
a=sorted(ls)
print('商品价格排序为：')
b=list(reversed(a))
print(b)  



ls1=[]
for t in range(0,36):       
    m=str(data['mods']['itemlist']['data']['auctions'][t]['view_sales'])
    x=int(m[0:-3])
    ls1.append(x)
y=sorted(ls1)
s=list(reversed(y))
print('商品销量从高到低为：'+str(s))



print('包邮的商品为：')
def F(i):   
    print('第'+format(i+1)+'个商品')
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])              
    print('-'*10)
for i in range(0,36):   
    if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0:   
      F(i)

    
    