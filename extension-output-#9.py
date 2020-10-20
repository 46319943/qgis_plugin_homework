# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SoftwareInstall\QGIS\apps\qgis-ltr\python\plugins\ly\LY_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LYDialogBase(object):
    def setupUi(self, LYDialogBase):
        LYDialogBase.setObjectName("LYDialogBase")
        LYDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(LYDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.pushButton = QtWidgets.QPushButton(LYDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.layerComboBox = QtWidgets.QComboBox(LYDialogBase)
        self.layerComboBox.setGeometry(QtCore.QRect(50, 30, 291, 22))
        self.layerComboBox.setObjectName("layerComboBox")

        self.retranslateUi(LYDialogBase)
        self.button_box.accepted.connect(LYDialogBase.accept)
        self.button_box.rejected.connect(LYDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(LYDialogBase)

    def retranslateUi(self, LYDialogBase):
        _translate = QtCore.QCoreApplication.translate
        LYDialogBase.setWindowTitle(_translate("LYDialogBase", "LY"))
        self.pushButton.setText(_translate("LYDialogBase", "PushButton"))

