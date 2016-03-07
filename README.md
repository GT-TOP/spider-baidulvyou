# spider-baidulvyou
百度旅游网页上游记标题的链接是动态生成的，这一点与大众点评有所不同；
1.利用pyqt-qtwebkit出现了无法连续抓取的问题，原因不明（不稳定？）
  尝试随机的useragent、睡眠随机秒数都没有效果
2.第二个方案，利用spynner，它是对pyqt的qtwebkit的封装（其实质还是webkit进行处理）
