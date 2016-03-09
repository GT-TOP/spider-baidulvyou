#coding=utf-8
import sys
import re
import requests
reload(sys)
sys.setdefaultencoding('utf8')

def get_nexturl(html):
    arg = re.search('href="/notes/(.*?)" data-itemnum="(.*?)">下一页</a>',html.content,re.S)  #此处html应加上content，否则出现typeerror
    if arg:
        nexturl =  'http://lvyou.baidu.com/notes/'+ arg.group(1) + '-' + arg.group(2)
        return nexturl
    else:
        return None

#存放每一篇游记的首页地址
fin = open(u'故宫.txt','r')
#得到所有游记的html文件
fout = open(u'故宫源代码.html','w')
urllist = fin.readlines()
fin.close()
#游记数目
print len(urllist)

for url in urllist:  #对每一个游记首页链接
    html = requests.get(url)
    fout.write(html.content)
    url = get_nexturl(html)
    while url != None:
        html = requests.get(url)
        fout.write(html.content)
        url = get_nexturl(html)

fout.close()
