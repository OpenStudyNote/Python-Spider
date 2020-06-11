#-*- codeing = utf-8 -*-
#@Time : 2020/5/13 20:20
#@Author : dele
#@File : music.py
#@Software: PyCharm

# 功能实现
# 搜索 https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=lemon
# 歌曲ID https://y.qq.com/n/yqq/song/000akynZ2Rbro5.html
# 解析 http://www.douqq.com/qqmusic/qqapi.php

import requests
from urllib.request import urlretrieve
import jsonpath
import json
import re

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# 界面设计
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 380, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 190, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.download_mp3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QQ Music Download"))
        self.pushButton.setText(_translate("MainWindow", "download"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Please enter a song name"))

    def download_mp3(self):
        # 搜索链接
        keyword =self.lineEdit.text()
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=65868335786339164&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={}&g_tk_new_20200303=498689185&g_tk=498689185&loginUin=1057527027&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(keyword)
        resp = requests.get(url)  # 获取url内容
        # print(resp.text) # 打印网页源代码
        html_doc = resp.json()
        mids = jsonpath.jsonpath(html_doc, "$..mid")
        print(mids)
        # 接口
        # headers 请求头 模拟浏览器登录
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh,zh-CN;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '65',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.douqq.com',
            'Origin': 'http://www.douqq.com',
            'Referer': 'http://www.douqq.com/qqmusic/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36129 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        link = 'http://www.douqq.com/qqmusic/qqapi.php'
        data = {'mid': 'https://y.qq.com/n/yqq/song/{}.html'.format(mids[0])}
        req = requests.post(url=link, data=data, headers=headers).text
        # print(req)

        req = json.loads(req)
        req = req.replace('\/', '/')  # 正则表达式，替换url下载链接
        # print(req)

        # 正则表达式
        res = re.compile('"m4a":"(.*?)",')
        rs = re.findall(res, req)
        # print(rs)
        mp3 = rs[0]  # 取列表第一个元素
        urlretrieve(mp3, keyword + '.mp3')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())
