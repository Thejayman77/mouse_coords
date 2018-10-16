# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coords.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(420, 300))
        Form.setMaximumSize(QtCore.QSize(420, 300))
        Form.setStyleSheet("color: white;\n"
"background-color: black;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.y_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.y_label.setFont(font)
        self.y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.y_label.setObjectName("y_label")
        self.gridLayout.addWidget(self.y_label, 1, 1, 1, 1)
        self.x_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.x_label.setFont(font)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")
        self.gridLayout.addWidget(self.x_label, 1, 0, 1, 1)
        self.y_coord = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_coord.sizePolicy().hasHeightForWidth())
        self.y_coord.setSizePolicy(sizePolicy)
        self.y_coord.setMinimumSize(QtCore.QSize(0, 130))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.y_coord.setFont(font)
        self.y_coord.setStyleSheet("background-color: rgb(1,10,30);\n"
"border: 4px solid white;\n"
"border-radius: 25px;\n"
"color: yellow;")
        self.y_coord.setText("")
        self.y_coord.setAlignment(QtCore.Qt.AlignCenter)
        self.y_coord.setObjectName("y_coord")
        self.gridLayout.addWidget(self.y_coord, 2, 1, 1, 1)
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setStyleSheet("border-bottom: 2px solid yellow;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 2)
        self.x_coord = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_coord.sizePolicy().hasHeightForWidth())
        self.x_coord.setSizePolicy(sizePolicy)
        self.x_coord.setMinimumSize(QtCore.QSize(0, 130))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.x_coord.setFont(font)
        self.x_coord.setStyleSheet("background-color: rgb(1,10,30);\n"
"border: 4px solid white;\n"
"border-radius: 25px;\n"
"color: yellow;")
        self.x_coord.setText("")
        self.x_coord.setAlignment(QtCore.Qt.AlignCenter)
        self.x_coord.setObjectName("x_coord")
        self.gridLayout.addWidget(self.x_coord, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.y_label.setText(_translate("Form", "Y"))
        self.x_label.setText(_translate("Form", "X"))
        self.title.setText(_translate("Form", "Position of mouse cursor on-screen"))

