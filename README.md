# spider-baidulvyou
百度旅游网页上游记标题的链接是动态生成的，这一点与大众点评有所不同；
1.利用pyqt-qtwebkit出现了无法连续抓取的问题，原因不明（不稳定？）
  尝试随机的useragent、睡眠随机秒数都没有效果
2.第二个方案，利用spynner，它是对pyqt的qtwebkit的封装（其实质还是webkit进行处理）
  程序在运行过程中，会产生AttributeError: 'Browser' object has no attribute 'manager'，这个错误可以忽略，对结果的完整性没有影响；
3.get_url文件用于从得到的html文件中提取url,并将其写入文件中；
