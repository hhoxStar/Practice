# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:44:33 2018
练习题8：
保存淘宝数据（小组项目）
1.每个组员爬取某个URL100页数据  每个组员爬取的不同的城市
2.保存淘宝商品信息（同练习6）并且保存为csv格式
3。每组组长合并各组员的数据
@author: samsung
"""

try:
    def p(n):
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E8%B4%B5%E5%B7%9E&ajax=true'
        import urllib.request as r#导入联网工具包，名为为r
        page=n*44
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E5%90%89%E6%9E%97&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'
        data=r.urlopen(url.format(page)).read().decode('utf-8','ignore')

        import json#将字符串转换为字典
        data=json.loads(data)
        a=json.dumps(data)
        f=open('tmp.txt','a',encoding='utf-8')
        f.write(a+'\n')
        f.close()
    for n in range(0,100):
        p(n)
        print(n)
except Exception as err:
    print('错误')


f=open('tmp.txt',encoding='utf-8')  #write
ls=f.readlines()  #将文本读取成列表
f.close()
def show(s):
    import json
    l=json.loads(ls[s])
    a=l['mods']['itemlist']['data']['auctions']
    def p(x):
        b=a[x]['title']
        c=a[x]['item_loc']
        d=a[x]['view_price']
        e=open('skirt.csv','a',encoding='gbk')
        e.write('第'+str(x+1)+'件'+'商品名称'+b+'发货地址'+c+'商品价格'+d)
        e.close()
    if s==0:
        for i in range(0,36):
            p(i)
    else:
        for i in range(0,44):
            p(i)
for i in range(0,100):
    show(i)
    e=open('skirt.csv','a',encoding='gbk')
    e.write('\n')
    e.close()
    
    
    
    

    
f=open('skirt.txt',encoding='utf_8')  #write
ls=f.readlines()  #将文本读取成列表
f.close()
def p(s):
    def skirt(q):
        import json
        data=json.loads(ls[s])
        a=data['mods']['itemlist']['data']['auctions'][q]['title']
        b=data['mods']['itemlist']['data']['auctions'][q]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][q]['item_loc']
        d=data['mods']['itemlist']['data']['auctions'][q]['nick']
        e=open('skirt.csv','a',encoding='utf_8')
        e.write('第'+str(q+1)+'件'+'商品名称'+a+'商品价格'+b+'商品产地'+c+'店铺'+d)
        e.close()
        for i in range(0,44):
            skirt(i)
for i in range(0,100):
    p(i)
    e=open('skirt.csv','a',encoding='utf_8')
    e.write('\n')
    e.close()       
    
    
    
    
    