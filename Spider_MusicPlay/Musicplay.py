#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 20:51
#@Author : dele
#@File : Musicplay.py
#@Software: PyCharm


# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
#
# win = QWidget()
#
# win.resize(400,150)
#
# win.setWindowTitle('Lemon—-Play')
# win.show()
#
# sys.exit(app.exec_())



from PyQt5 import QtWidgets,QtGui,QtCore

from PyQt5.QtMultimedia import  QMediaContent,QMediaPlayer

import qtawesome as qta

class Music(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,200)
        self.setWindowTitle("Music_Play")
        self.init_ui()
        self.custom_style()
        self.playing = False

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        #self.timer.timeout.connect(self.check_status)


# 界面设置

    def custom_style(self):
        self.setStyleSheet('''
            #main_widget{
                border-radius:5px;
            }
            #play_btn,#pervious_btn,#next_btn:hover{
                background:gray;
                border-radius:5px;
                cursor:pointer;
            }
        ''')
        self.close_btn.setStyleSheet('''
            QPushButton{
                background:#F76677;
                border-radius:5px;
            }
            QPushButton:hover{
                background:#red;
            }''')
        self.status_label.setStyleSheet('''
            QLabel{
                background:#F7D674;
                border-radius:5px;
                }
        ''')

    # 初始化界面
    def init_ui(self):
        # 窗口布局
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        # 控件布局 网格布局
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        # 标签
        self.title_lable = QtWidgets.QLabel("乐者，音之所由生")
        # 关闭按钮
        self.close_btn = QtWidgets.QPushButton("")
        self.close_btn.setFixedSize(15,15)
        # 音乐状态
        self.status_label =QtWidgets.QLabel("")
        self.status_label.setFixedSize(15,15)
        # 图标
        play_icon = qta.icon("fa.play-circle",)
        self.play_btn = QtWidgets.QPushButton(play_icon,"")
        self.play_btn.setIconSize(QtCore.QSize(80,80))
        self.play_btn.setFixedSize(82,82)
        self.play_btn.setObjectName("play_btn")
        # 下一个
        next_icon = qta.icon("fa.play-circle-o")
        self.next_btn = QtWidgets.QPushButton(next_icon,"")
        self.next_btn.setIconSize(QtCore.QSize(80,80))
        self.next_btn.setFixedSize(82,82)
        self.next_btn.setObjectName("next_btn")
        #进度条
        self.process_bar = QtWidgets.QProgressBar()
        self.process_value = 0
        self.process_bar.setValue(self.process_value)
        self.process_bar.setFixedHeight(5)
        self.process_bar.setTextVisible(False)


        # 布局
        self.main_layout.addWidget(self.close_btn,0,0,1,1)
        self.main_layout.addWidget(self.title_lable,0,1,1,1)
        self.main_layout.addWidget(self.status_label,1,0,1,1)
        self.main_layout.addWidget(self.play_btn,1,1,1,1)
        self.main_layout.addWidget(self.next_btn,1,2,1,1)
        self.main_layout.addWidget(self.process_bar,2,0,1,3)

        self.setCentralWidget(self.main_widget)

import sys
app = QtWidgets.QApplication(sys.argv)
gui = Music()
gui.show()
sys.exit(app.exec_())




