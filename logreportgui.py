# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guir.ui'
# Created by: PyQt5 UI code generator 5.13.2
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(326, 155)
        self.buttonBox = QtWidgets.QWidget(MainWindow)
        self.buttonBox.setGeometry(QtCore.QRect(10, 110, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 70, 81, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(160, 40, 141, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 291, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LogBook Report"))
        self.label.setText(_translate("Dialog", "Ім\'я файлу"))
        self.label_2.setText(_translate("Dialog", "Період підрахунку"))
        self.label_3.setText(_translate("Dialog", "Підрахунок річного підсумку Total flight-time"))
