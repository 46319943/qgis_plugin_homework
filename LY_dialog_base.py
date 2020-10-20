# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SoftwareInstall\QGIS\apps\qgis-ltr\python\plugins\ly\LY_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LYDialogBase(object):
    def setupUi(self, LYDialogBase):
        LYDialogBase.setObjectName("LYDialogBase")
        LYDialogBase.resize(400, 446)
        self.button_box = QtWidgets.QDialogButtonBox(LYDialogBase)
        self.button_box.setGeometry(QtCore.QRect(40, 410, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.cannyPushButton = QtWidgets.QPushButton(LYDialogBase)
        self.cannyPushButton.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.cannyPushButton.setObjectName("cannyPushButton")
        self.rasterLayerComboBox = QtWidgets.QComboBox(LYDialogBase)
        self.rasterLayerComboBox.setGeometry(QtCore.QRect(90, 30, 291, 22))
        self.rasterLayerComboBox.setObjectName("rasterLayerComboBox")
        self.classifyPushButton = QtWidgets.QPushButton(LYDialogBase)
        self.classifyPushButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.classifyPushButton.setObjectName("classifyPushButton")
        self.label = QtWidgets.QLabel(LYDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.label.setObjectName("label")
        self.vectorLayerComboBox = QtWidgets.QComboBox(LYDialogBase)
        self.vectorLayerComboBox.setGeometry(QtCore.QRect(90, 60, 291, 22))
        self.vectorLayerComboBox.setObjectName("vectorLayerComboBox")
        self.label_2 = QtWidgets.QLabel(LYDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LYDialogBase)
        self.label_3.setGeometry(QtCore.QRect(170, 130, 51, 21))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(LYDialogBase)
        self.spinBox.setGeometry(QtCore.QRect(270, 130, 42, 22))
        self.spinBox.setMinimum(2)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(LYDialogBase)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.lowThresholdSpinBox = QtWidgets.QSpinBox(LYDialogBase)
        self.lowThresholdSpinBox.setGeometry(QtCore.QRect(120, 100, 42, 22))
        self.lowThresholdSpinBox.setMinimum(0)
        self.lowThresholdSpinBox.setMaximum(1000)
        self.lowThresholdSpinBox.setProperty("value", 100)
        self.lowThresholdSpinBox.setObjectName("lowThresholdSpinBox")
        self.label_5 = QtWidgets.QLabel(LYDialogBase)
        self.label_5.setGeometry(QtCore.QRect(170, 100, 91, 21))
        self.label_5.setObjectName("label_5")
        self.highThresholdSpinBox_2 = QtWidgets.QSpinBox(LYDialogBase)
        self.highThresholdSpinBox_2.setGeometry(QtCore.QRect(270, 100, 42, 22))
        self.highThresholdSpinBox_2.setMinimum(0)
        self.highThresholdSpinBox_2.setMaximum(1000)
        self.highThresholdSpinBox_2.setProperty("value", 200)
        self.highThresholdSpinBox_2.setObjectName("highThresholdSpinBox_2")
        self.label_6 = QtWidgets.QLabel(LYDialogBase)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_6.setObjectName("label_6")
        self.spinBox_2 = QtWidgets.QSpinBox(LYDialogBase)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 130, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setProperty("value", 3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.textEdit = QtWidgets.QTextEdit(LYDialogBase)
        self.textEdit.setGeometry(QtCore.QRect(20, 210, 361, 191))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(LYDialogBase)
        self.button_box.accepted.connect(LYDialogBase.accept)
        self.button_box.rejected.connect(LYDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(LYDialogBase)

    def retranslateUi(self, LYDialogBase):
        _translate = QtCore.QCoreApplication.translate
        LYDialogBase.setWindowTitle(_translate("LYDialogBase", "LY"))
        self.cannyPushButton.setText(_translate("LYDialogBase", "图像辅助"))
        self.classifyPushButton.setText(_translate("LYDialogBase", "图形分类"))
        self.label.setText(_translate("LYDialogBase", "栅格图层"))
        self.label_2.setText(_translate("LYDialogBase", "矢量图层"))
        self.label_3.setText(_translate("LYDialogBase", "聚类数量"))
        self.label_4.setText(_translate("LYDialogBase", "Canny滞后低阈值"))
        self.label_5.setText(_translate("LYDialogBase", "Canny滞后高阈值"))
        self.label_6.setText(_translate("LYDialogBase", "Sobel算子大小"))
        self.textEdit.setHtml(_translate("LYDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">图像辅助</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">通过Canny算子检测栅格图像边缘，帮助矢量化边界的识别</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">图形分类</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">计算矢量图形对应栅格图像的多通道平均值，使用层次聚类对矢量图形进行非监督聚类</span></p></body></html>"))

