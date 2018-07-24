# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:43:06 2018
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

#data字典-》mods字典-》itemlist字典-》data字典-》（中括号内是列表）0uctions列表-》0 index 字典-》title变量
title=data['mods']['itemlist']['data']['auctions'[0]['title']
#data字典-》mods字典-》itemlist字典-》data字典-》（中括号内是列表）0uctions列表-》0 index 字典-》view price
price=data['mods']['itemlist']['data']['auctions'[0]['view_price']

