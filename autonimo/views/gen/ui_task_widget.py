# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\ui\task_widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TaskWidget(object):
    def setupUi(self, TaskWidget):
        TaskWidget.setObjectName(_fromUtf8("TaskWidget"))
        TaskWidget.resize(504, 581)
        self.gridLayout = QtGui.QGridLayout(TaskWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_check_params = QtGui.QPushButton(TaskWidget)
        self.pushButton_check_params.setObjectName(_fromUtf8("pushButton_check_params"))
        self.gridLayout_2.addWidget(self.pushButton_check_params, 0, 3, 1, 1)
        self.pushButton_reset_params = QtGui.QPushButton(TaskWidget)
        self.pushButton_reset_params.setObjectName(_fromUtf8("pushButton_reset_params"))
        self.gridLayout_2.addWidget(self.pushButton_reset_params, 0, 2, 1, 1)
        self.pushButton_run = QtGui.QPushButton(TaskWidget)
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.gridLayout_2.addWidget(self.pushButton_run, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 0, 1, 1)
        self.tableView = QtGui.QTableView(TaskWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 1, 0, 6, 1)

        self.retranslateUi(TaskWidget)
        QtCore.QMetaObject.connectSlotsByName(TaskWidget)

    def retranslateUi(self, TaskWidget):
        TaskWidget.setWindowTitle(_translate("TaskWidget", "Task", None))
        self.pushButton_check_params.setText(_translate("TaskWidget", "Check parameters", None))
        self.pushButton_reset_params.setText(_translate("TaskWidget", "Reset parameters", None))
        self.pushButton_run.setText(_translate("TaskWidget", "Run task", None))

