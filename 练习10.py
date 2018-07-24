# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:05:34 2018
请求的URL
http://www.gaokaopai.com/university-ajaxGetMajor.html
请求的数据
id=3319&type=2&city=34&state=1
学校编号   理科2        城市        正常
作业10
1.获取2300所学校的编号
2.获取31所城市的编号
3.获取142000数据 31/10，每个组有3个城市数据 后面组装
4.将142600数据使用spark统计

河南湖北湖南
@author: Administrator
"""





ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
    
'北京大学 北京http://www.gaokaopai.com/daxue-jianjie-477.html'.split('-jianjie-')[1].split('.')[0]


import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

f=open('湖北学校.txt','a',encoding='utf-8')
for schoolid in schoolls[0:2300]:
    for kemu in [1,2]:
        req=r.Request(url,data='id={}&type={}city=42&state=1'.format(schoolid,kemu).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()

        



import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
d=open('school_id.txt')
school=d.readlines()
citys=[41,42,43]
d.close()
f=open('河南湖北湖南.txt','a',encoding='utf-8')
for sid in school:
    for city in citys:
        for ls in [1,2]:
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(sid,ls,city).encode(),headers=headers)
            data=r.urlopen(req).read().decode('utf-8','ignore')
            import json
            data=json.loads(data)
            a=json.dumps(data)
            f.write(a)
            print(school)
f.close()





import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
citys=[41,42,43]
f=open('河南河北湖南.txt','a',encoding='utf-8')
for schoolid in schoolls[0:2300]:
    for city in citys:
        for kemu in [1,2]:
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolid,kemu,city).encode(),headers=headers)
            f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()


##1.2300所学校的编号
file=open('all_school.txt',encoding='utf-8').readlines()
print('2300所学校的编号：\n')
for i in range(len(file)):
    print(file[i].split('-jianjie-')[1].split('.')[0])


##2.31所城市的编号
file2=open('XML高考派城市.txt',encoding='gbk').readlines()
print('31所城市的编号：\n')
for k in range(1,32):
    print(file2[k].split('<li data-val=')[1].split('data-id=')[0]+file2[k].split('claimCity')[1].split(',')[1].split(')')[0])


