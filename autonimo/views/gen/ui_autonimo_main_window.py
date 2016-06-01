# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\ui\autonimo_main_window.ui'
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

class Ui_AutonimoMainWindow(object):
    def setupUi(self, AutonimoMainWindow):
        AutonimoMainWindow.setObjectName(_fromUtf8("AutonimoMainWindow"))
        AutonimoMainWindow.resize(1076, 850)
        AutonimoMainWindow.setStyleSheet(_fromUtf8(""))
        AutonimoMainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(AutonimoMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        AutonimoMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AutonimoMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AutonimoMainWindow.setStatusBar(self.statusbar)
        self.dockWidget_tasks = QtGui.QDockWidget(AutonimoMainWindow)
        self.dockWidget_tasks.setStyleSheet(_fromUtf8(""))
        self.dockWidget_tasks.setObjectName(_fromUtf8("dockWidget_tasks"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.treeView_tasks_available = QtGui.QTreeView(self.dockWidgetContents_2)
        self.treeView_tasks_available.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView_tasks_available.setObjectName(_fromUtf8("treeView_tasks_available"))
        self.gridLayout_6.addWidget(self.treeView_tasks_available, 0, 0, 1, 1)
        self.dockWidget_tasks.setWidget(self.dockWidgetContents_2)
        AutonimoMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_tasks)
        self.toolBar = QtGui.QToolBar(AutonimoMainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        AutonimoMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(AutonimoMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1076, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        AutonimoMainWindow.setMenuBar(self.menuBar)
        self.action_open_task = QtGui.QAction(AutonimoMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/folder-horizontal-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_task.setIcon(icon)
        self.action_open_task.setObjectName(_fromUtf8("action_open_task"))
        self.action_save_task = QtGui.QAction(AutonimoMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_task.setIcon(icon1)
        self.action_save_task.setObjectName(_fromUtf8("action_save_task"))
        self.action_save_task_as = QtGui.QAction(AutonimoMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/disk-rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_task_as.setIcon(icon2)
        self.action_save_task_as.setObjectName(_fromUtf8("action_save_task_as"))
        self.action_exit = QtGui.QAction(AutonimoMainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_about = QtGui.QAction(AutonimoMainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/balloon-smiley.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon3)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.toolBar.addAction(self.action_open_task)
        self.toolBar.addAction(self.action_save_task)
        self.toolBar.addAction(self.action_save_task_as)
        self.menuFile.addAction(self.action_open_task)
        self.menuFile.addAction(self.action_save_task)
        self.menuFile.addAction(self.action_save_task_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AutonimoMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AutonimoMainWindow)

    def retranslateUi(self, AutonimoMainWindow):
        AutonimoMainWindow.setWindowTitle(_translate("AutonimoMainWindow", "MainWindow", None))
        self.dockWidget_tasks.setWindowTitle(_translate("AutonimoMainWindow", "Tasks", None))
        self.toolBar.setWindowTitle(_translate("AutonimoMainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("AutonimoMainWindow", "File", None))
        self.menuHelp.setTitle(_translate("AutonimoMainWindow", "Help", None))
        self.action_open_task.setText(_translate("AutonimoMainWindow", "Open task...", None))
        self.action_open_task.setToolTip(_translate("AutonimoMainWindow", "Open task", None))
        self.action_save_task.setText(_translate("AutonimoMainWindow", "Save task", None))
        self.action_save_task.setToolTip(_translate("AutonimoMainWindow", "Save task", None))
        self.action_save_task_as.setText(_translate("AutonimoMainWindow", "Save task as...", None))
        self.action_save_task_as.setToolTip(_translate("AutonimoMainWindow", "Save task as", None))
        self.action_exit.setText(_translate("AutonimoMainWindow", "Exit", None))
        self.action_about.setText(_translate("AutonimoMainWindow", "About", None))

import autonimo_rc
