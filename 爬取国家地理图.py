
"""
要实现的功能：
从中国国家地理网上解析网页源码，循环获取图片的资源，并下载到本地
这是自己写的**************
"""
# 一.获取图片资源
# 二.保存在本地
# 原版程序出现的问题是：判断的第一步是是否有文件夹而不是有文件
# 可以组合
# r ：只读
# r+ : 读写
# w ： 新建（会对原有文件进行覆盖）
# a ： 追加
# b ： 二进制文件
"""
同时添加或者减少缩进的快捷方式：
tab+shift或者
shift+tab
"""
import os
import requests
from bs4 import BeautifulSoup
import re  # 用正则表达式来解析网页的img标签下的src资源或者用美丽汤
# 测试用网页：http://www.dili360.com/gallery/cate/1.htm
x = input("1.风光 2.人文 3.航拍 4.水下 5.建筑 6.动物 7.植物 8.星空 9.黑白 10.专题 \r\n请输入需要爬取的页数:")  # \r\n换行符
res = requests.get("http://www.dili360.com/gallery/cate/"+x+".htm")  # 获取网页源码
texts = res.text
bf = BeautifulSoup(texts)
s = bf.find_all("img")
name = bf.find_all("a", href="/gallery/cate/"+x+".htm")  # 标签
count = len(name)
for Name in range(count):
    kk = name[Name].string
    if kk is not None:
        wenJianMing=""
        wenJianMing = kk
"""
<img alt="春天的密码" src="http://img0.dili360.com/ga/M02/02/18/wKgBzFQ2x9eAbZn8AATCSQolols997.jpg@!rw5"/>
"""
listCount = len(s)
root = "G://pycharm//爬虫专用文件夹//"+wenJianMing+"//"
num = 1
for i in range(listCount):
    if not os.path.exists(root):
        os.mkdir(root)
    path = root + '%d'%num + ".jpg"  # int类型转换成str型,要加上.jpg才可以识别文件类型
    src = s[i].get("src")  # 相当于正则表达式的方法获取src资源
    l = len(src)
    sr = src[0:l-5]  # 删减后缀，变成jpg
    if sr[-3:] == "jpg":  # 判断是否是.jpg后缀的文件
        num += 1
        # url = "http://img0.dili360.com/ga/M02/02/18/wKgBzFQ2x9eAbZn8AATCSQolols997.jpg"
        print('{}{}{}{}'.format(num, " ", ":", sr))
        re = requests.get(sr)
        with open(path, "wb") as f:
            f.write(re.content)
            f.close()
            print(wenJianMing+"图片保存成功")

