#encoding=utf-8
#用QTwebkit解析web页面（html+js）
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

for index in range(1,10):
  url =  'http://lvyou.baidu.com/yiheyuan/youji/#%d'%index
  print url
  r = Render(url)
  html = r.frame.toHtml()
  #print html.toUtf8()
  #降低访问频率
  time.sleep(random.randint(1,10))

  # 将执行后的代码写入文件中
  f = open(u'颐和园测试.txt','a')
  f.write(html.toUtf8())
  f.close()