#-*-coding: utf-8 -*-
#之前将该文件命名为spynner.py导致出错，与spynner库冲突
#该程序可以抓取到JS文件执行后的HTML
import spynner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

for index in range(1,60):
    #创建一个浏览器对象
    browser = spynner.Browser()
    #打开浏览器，并隐藏
    browser.hide()
    url = 'http://lvyou.baidu.com/yiheyuan/youji/#%d'%index
    print url
    #browser 类中有一个类方法load，可以用webkit加载你想加载的页面信息
    #load(是你想要加载的网址的字符串形式)
    browser.load(url)
    #browser 类中有一个成员是html，是页面进过处理后的源码的字符串
    #将其转码为UTF-8编码
    #print browser.html.encode("utf-8")

    #你也可以将它写到文件中，用浏览器打开。
    open(u"颐和园完整.html", 'a+').write(browser.html.encode("utf-8"))

    #关闭该浏览器
    browser.close()


