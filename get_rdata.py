#-*-coding: utf-8 -*-
#观察发现除了文字以外，其余内容全部都在< >标签中
#图片的链接前有data-src
#采用sub多次逐步清理
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

fin = open(u'八达岭长城游记实体.txt','r')
fout = open(u'八达岭长城真实数据.txt','w')
strs = fin.read()
#将含有图片链接的标签做一些特殊标记，将<...>改为$...>   更正：选用$无法进行第三步清理，改为/  
#原因是$在python正则表达式中有特殊含义，而/加上某些字母也有特殊含义，这次实验中没有影响
strs = re.sub('<img class="notes-photo-img"','/img class="notes-photo-img"',strs)
#将没有特殊标记过的<...>标签删掉
strs = re.sub('<.*?>','',strs)   #添加re.S后，部分<...>里的内容没有替换
#最后清理得到链接
strs = re.sub('/img.*?data-src="','',strs)
strs = re.sub('".*?/>','',strs)

for str in strs:
    fout.write(str)    #read()读取文件的方式是将整个文件看作是一个大的字符串，不用多加\n，与readline有区别

fin.close()
fout.close()

