#coding=utf-8
#先大后小原则，先抓取<div class="content">标签中的内容
#然后从中提取文字内容以及图像链接
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

fin = open(u'八达岭长城源代码.html','r')
fout = open(u'八达岭长城游记实体.txt','w')
content = fin.read()
bigarea = re.findall('<div class="content">(.*?)</div>',content,re.S)
for item in bigarea:
    print item
    fout.write(item)
print len(bigarea)
fin.close()
fout.close()
