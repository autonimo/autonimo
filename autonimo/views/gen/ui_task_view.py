# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\ui\task_view.ui'
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

class Ui_TaskView(object):
    def setupUi(self, TaskView):
        TaskView.setObjectName(_fromUtf8("TaskView"))
        TaskView.resize(355, 260)
        self.centralwidget = QtGui.QWidget(TaskView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        TaskView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(TaskView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TaskView.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(TaskView)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        TaskView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(TaskView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionRun = QtGui.QAction(TaskView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/control.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionRun)

        self.retranslateUi(TaskView)
        QtCore.QMetaObject.connectSlotsByName(TaskView)

    def retranslateUi(self, TaskView):
        TaskView.setWindowTitle(_translate("TaskView", "MainWindow", None))
        self.pushButton.setText(_translate("TaskView", "Reset", None))
        self.pushButton_3.setText(_translate("TaskView", "Validate", None))
        self.pushButton_2.setText(_translate("TaskView", "Run", None))
        self.toolBar.setWindowTitle(_translate("TaskView", "toolBar", None))
        self.actionSave.setText(_translate("TaskView", "save", None))
        self.actionRun.setText(_translate("TaskView", "run", None))

import autonimo_rc
