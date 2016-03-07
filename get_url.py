#-*-coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

total = 0
fin = open(u'香山.html','r')
fout = open(u'香山.txt','w')
htmllist = fin.readlines()
for line in htmllist:
    urls = re.findall('target="_blank" href="http:(.*?)title=',line,re.S)
    for url in urls:
        url = 'http:' + url
        fout.write(url+'\n') #write函数不会自动写入一个换行符
        print url
    total += len(urls)   #统计url总数以便于验证结果正确性
print total
fin.close()
fout.close()
