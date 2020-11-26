# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'umeng.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox, QWidget, QLabel, QMainWindow, QApplication, QHBoxLayout, \
    QLineEdit

import myjson
from getqrcode import search
from mainwindow import Ui_wechatqrcode
from proxy import startmimt, openproxy, closeproxy
from umengapi import getqrimglist

class Ui_umeng(object):
    def setupUi(self, umeng):
        umeng.setObjectName("umeng")
        umeng.resize(1200, 801)
        umeng.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(umeng)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 600))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 5, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(800, 500))
        self.scrollArea.setMaximumSize(QtCore.QSize(800, 1300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 680))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 2, 1, 1)
        umeng.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(umeng)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        umeng.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(umeng)
        self.statusbar.setObjectName("statusbar")
        umeng.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(umeng)
        self.cnbt()
        self.initdata()
        QtCore.QMetaObject.connectSlotsByName(umeng)

    def retranslateUi(self, umeng):
        _translate = QtCore.QCoreApplication.translate
        umeng.setWindowTitle(_translate("umeng", "微信二维码获取"))
        self.pushButton.setToolTip(_translate("umeng", "输入公众号链接点击获取"))
        self.pushButton.setText(_translate("umeng", "一键获取"))
        self.label_2.setText(_translate("umeng", "抓取服务状态："))
        self.label.setText(_translate("umeng", "代理状态："))
        self.textBrowser.setHtml(_translate("umeng",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">使用方法：</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.首次使用需要先安装证书，下载地址http://mitm.it，密码为空，安装到目录根证书发布者</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.打开二维码所在页面，目前支持跟谁学的二维码获取，复制链接粘贴到页面，点击获取即可</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.在线地址会缓存在本地，每次点击选择列表会自动刷新图片</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.双击列表内容可以删除无效资源，每个号频繁后换号获取其他链接即可</p></body></html>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.复制目录下data.json文件到其他电脑可以共用已经获取到的图片地址"
                                            ))
        self.menu.setTitle(_translate("umeng", "菜单"))
        self.menu.addAction(_translate("f_1", "公众号文章内二维码抓取"))

    def cnbt(self):
        self.pushButton.clicked.connect(self.addtolist)
        self.listWidget.itemClicked.connect(self.chooseitem)
        self.listWidget.itemClicked.connect(self.savechange)
        self.listWidget.itemSelectionChanged.connect(self.savechange)
        self.listWidget.itemDoubleClicked.connect(self.doubleck)
        self.lineEdit.returnPressed.connect(self.addtolist)
        self.menu.triggered.connect(self.openchild)

    def initdata(self):  ## 程序初始化自动打开代理
        self.data = myjson.read('./data.json')
        self.mylist = list(self.data.keys())
        startmimt(self)
        openproxy(self)
        self.renderlist(self.mylist)

    def savechange(self):
        print("字段保存")
        for index,i in enumerate(self.mylist):
            title=globals()['Qline_' + str(index)].text()
            self.data[i] = {"title": title, "pic": self.data[i]['pic']}
            myjson.write('./data.json', self.data)


    def renderlist(self,rdlist):
        for index,i in enumerate(rdlist):
            text = self.data[i]['title']
            globals()['Qline_' + str(index)] =QLineEdit(text)
            globals()['Qline_' + str(index)].editingFinished.connect(self.savechange)
            item = QListWidgetItem(i)
            item.setSizeHint(QSize(50,50))
            layout_right_down = QHBoxLayout()  # 右下的横向布局
            layout_right_down.addWidget(globals()['Qline_' + str(index)])
            wg= QWidget()
            wg.setLayout(layout_right_down)
            self.listWidget.addItem(item)  # 创建本地缓存  载入时加载本地缓存！
            self.listWidget.setItemWidget(item, wg)


    def addtolist(self):  ## 添加到列表自动获取图片
        # closeproxy(self)
        text = self.lineEdit.text()
        if text not in self.mylist and text != "":
            self.data[text] ={"title":"未命名","pic":[]}
            self.mylist = list(self.data.keys())
            self.renderlist(self.mylist)
            myjson.write('./data.json', self.data)
        self.cacheimg()

    def chooseitem(self):
        critem = self.listWidget.currentItem().text()
        newlist = self.data[critem]['pic']
        self.getcode(newlist)

    def doubleck(self):
        critem = self.listWidget.currentItem()
        reply = QMessageBox.question(self.centralwidget, '删除', '确认删除吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.listWidget.takeItem(self.listWidget.currentRow())
            del self.data[critem.text()]
            myjson.write('./data.json', self.data)

    def cacheimg(self):
        text = self.lineEdit.text()
        if text != "":
            newlist = getqrimglist(text, self.centralwidget)
            self.getcode(newlist)
        # if self.listWidget.currentItem():
        #     newlist = getqrimglist(self.listWidget.currentItem().text(),self.centralwidget)
        #     self.getcode(newlist)

    def getcode(self, list):
        self.filewidget = QWidget()
        self.filewidget.setMinimumSize(350, 3000)
        row = len(list) / 3
        positions = [(i, j) for i in range(3) for j in range(round(row))]  # 规定每行每列多少数据  第一个是行 第二个是列
        for position, picurl in zip(positions, list):  # 在for里面新建qlabel 这样每个label才会是独立的
            myimg = QLabel(self.filewidget)
            myimg.setScaledContents(True)
            res = requests.get(picurl)
            print(position, picurl)
            img = QImage.fromData(res.content)
            myimg.setPixmap(QPixmap.fromImage(img))
            myimg.setFixedSize(200, 200)
            myimg.move(250 * position[0], 250 * position[1])
        self.scrollArea.setWidget(self.filewidget)

    def openchild(self, action):
        print("zi", action)
        self.childwindow = QMainWindow()
        ui = Ui_wechatqrcode()
        ui.setupUi(self.childwindow)
        self.childwindow.show()
        print(558888)