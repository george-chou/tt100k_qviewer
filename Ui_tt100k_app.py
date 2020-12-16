# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\downloads\telecom_interns\tt100k_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ShowImg
import Widget_img_in
import Widget_img_out

class Ui_MainWindow(object):

    def __init__(self):
        self.showimg = ShowImg.ShowImg()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = Widget_img_in.Widget_img_in(self.showimg, self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 70, 371, 271))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = Widget_img_out.Widget_img_out(self.showimg, self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(500, 70, 371, 271))
        self.widget_2.setAutoFillBackground(True)
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 180, 51, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 370, 821, 91))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.widget.upd)
        self.pushButton.clicked.connect(self.widget_2.clear)
        self.pushButton_2.clicked.connect(self.widget_2.upd)
        self.widget.loaded.connect(self.updStatusbar)
        self.widget_2.loaded.connect(self.updStatusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Random"))
        self.pushButton_2.setText(_translate("MainWindow", ">>"))

    # def releaseBtn(self, enable):
    #     self.pushButton_2.setEnabled(enable)

    def updStatusbar(self, msg):
        dvline = '\n'
        for i in range(98):
            dvline = '-' + dvline
        self.textBrowser.append(dvline + msg)
        self.pushButton_2.setEnabled(True)


