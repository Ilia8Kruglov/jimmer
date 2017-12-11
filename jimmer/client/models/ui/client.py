# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(200, 0))
        MainWindow.setMaximumSize(QtCore.QSize(200, 16777215))
        MainWindow.setTabletTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/chat1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lnContact = QtWidgets.QLineEdit(self.centralwidget)
        self.lnContact.setEnabled(False)
        self.lnContact.setMinimumSize(QtCore.QSize(198, 0))
        self.lnContact.setMaximumSize(QtCore.QSize(198, 16777215))
        self.lnContact.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lnContact.setFrame(False)
        self.lnContact.setObjectName("lnContact")
        self.verticalLayout.addWidget(self.lnContact)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setMinimumSize(QtCore.QSize(24, 24))
        self.btnAdd.setMaximumSize(QtCore.QSize(24, 24))
        self.btnAdd.setText("")
        iconAddContact = QtGui.QIcon()
        iconAddContact.addPixmap(QtGui.QPixmap(":/images/icons/plus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(iconAddContact)
        self.btnAdd.setAutoDefault(True)
        self.btnAdd.setDefault(True)
        self.btnAdd.setFlat(True)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setEnabled(False)
        self.btnDel.setMinimumSize(QtCore.QSize(24, 24))
        self.btnDel.setMaximumSize(QtCore.QSize(24, 24))
        self.btnDel.setText("")
        iconDelContact = QtGui.QIcon()
        iconDelContact.addPixmap(QtGui.QPixmap(":/images/icons/minus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDel.setIcon(iconDelContact)
        self.btnDel.setIconSize(QtCore.QSize(16, 16))
        self.btnDel.setAutoRepeatDelay(299)
        self.btnDel.setAutoDefault(False)
        self.btnDel.setDefault(False)
        self.btnDel.setFlat(True)
        self.btnDel.setObjectName("btnDel")
        self.horizontalLayout.addWidget(self.btnDel)
        self.btnChat = QtWidgets.QPushButton(self.centralwidget)
        self.btnChat.setEnabled(False)
        self.btnChat.setMaximumSize(QtCore.QSize(40, 40))
        self.btnChat.setFlat(True)
        self.btnChat.setObjectName("btnChat")
        self.horizontalLayout.addWidget(self.btnChat)
        self.btnGetContacts = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetContacts.setEnabled(False)
        self.btnGetContacts.setMinimumSize(QtCore.QSize(60, 0))
        self.btnGetContacts.setMaximumSize(QtCore.QSize(80, 20))
        self.btnGetContacts.setFlat(True)
        self.btnGetContacts.setObjectName("btnGetContacts")
        self.horizontalLayout.addWidget(self.btnGetContacts)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lstContacts = QtWidgets.QListWidget(self.centralwidget)
        self.lstContacts.setEnabled(True)
        self.lstContacts.setMinimumSize(QtCore.QSize(198, 0))
        self.lstContacts.setMaximumSize(QtCore.QSize(198, 16777215))
        self.lstContacts.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lstContacts.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstContacts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lstContacts.setObjectName("lstContacts")
        self.verticalLayout.addWidget(self.lstContacts)
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setMinimumSize(QtCore.QSize(160, 0))
        self.btnConnect.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnConnect.setAutoDefault(False)
        self.btnConnect.setDefault(False)
        self.btnConnect.setFlat(True)
        self.btnConnect.setObjectName("btnConnect")
        self.verticalLayout.addWidget(self.btnConnect, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusMessage = QtWidgets.QStatusBar(MainWindow)
        self.statusMessage.setMaximumSize(QtCore.QSize(16777215, 16))
        self.statusMessage.setSizeIncrement(QtCore.QSize(0, 16))
        self.statusMessage.setObjectName("statusMessage")
        MainWindow.setStatusBar(self.statusMessage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnConnect, self.lnContact)
        MainWindow.setTabOrder(self.lnContact, self.btnAdd)
        MainWindow.setTabOrder(self.btnAdd, self.lstContacts)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "jimmer"))
        self.btnChat.setText(_translate("MainWindow", "Join"))
        self.btnGetContacts.setText(_translate("MainWindow", "Get contacts"))
        self.btnConnect.setText(_translate("MainWindow", "Disconnected. Click to connect"))

import client.resources_rc
