# spider-baidulvyou
百度旅游网页上游记标题的链接是动态生成的，这一点与大众点评有所不同；
1.利用pyqt-qtwebkit出现了无法连续抓取的问题，原因不明（不稳定？）
  尝试随机的useragent、睡眠随机秒数都没有效果
2.第二个方案，利用spynner，它是对pyqt的qtwebkit的封装（其实质还是webkit进行处理）
  程序在运行过程中，会产生AttributeError: 'Browser' object has no attribute 'manager'，这个错误可以忽略，对结果的完整性没有影响；
3.get_url文件用于从得到的html文件中提取url,并将其写入文件中；
4.get_html文件用于根据之前提取的每篇游记的首页地址来获得游记的全部html内容，主要解决翻页问题；
  由于没有考虑优化，所以程序的效率不高，在颐和园这种比较大的景点上，程序需要半个小时；
5.get_content文件用于从上一步得到的html文件中初步去除冗余，只保留content标签里的内容（观察网页源代码发现需要的内容包含在这些标签里）
（a.大部分游记的内容都在若干个 textarea 标签中，而其中有用的内容在<div class="content">....</div>中
  b.存在少数老版本的游记，内容直接在<div class="content">....</div>中）
6.get_rdata文件得到最终需要的游记文字加图片链接，并且按照游记原有的顺序排列

至此，数据准备工作完成。
