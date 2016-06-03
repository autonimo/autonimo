# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\ui\main_view.ui'
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

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName(_fromUtf8("MainView"))
        MainView.resize(1076, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainView.setWindowIcon(icon)
        MainView.setStyleSheet(_fromUtf8(""))
        MainView.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainView.setStatusBar(self.statusbar)
        self.dockWidget_tasks = QtGui.QDockWidget(MainView)
        self.dockWidget_tasks.setStyleSheet(_fromUtf8(""))
        self.dockWidget_tasks.setObjectName(_fromUtf8("dockWidget_tasks"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.treeView_tasks_available = QtGui.QTreeView(self.dockWidgetContents_2)
        self.treeView_tasks_available.setObjectName(_fromUtf8("treeView_tasks_available"))
        self.gridLayout_6.addWidget(self.treeView_tasks_available, 0, 0, 1, 1)
        self.dockWidget_tasks.setWidget(self.dockWidgetContents_2)
        MainView.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_tasks)
        self.toolBar = QtGui.QToolBar(MainView)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainView)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1076, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainView.setMenuBar(self.menuBar)
        self.dockWidget = QtGui.QDockWidget(MainView)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.treeView_comps_available = QtGui.QTreeView(self.dockWidgetContents)
        self.treeView_comps_available.setObjectName(_fromUtf8("treeView_comps_available"))
        self.gridLayout_2.addWidget(self.treeView_comps_available, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainView.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_open_task = QtGui.QAction(MainView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/folder-horizontal-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_task.setIcon(icon1)
        self.action_open_task.setObjectName(_fromUtf8("action_open_task"))
        self.action_save_task = QtGui.QAction(MainView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_task.setIcon(icon2)
        self.action_save_task.setObjectName(_fromUtf8("action_save_task"))
        self.action_save_task_as = QtGui.QAction(MainView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/disk-rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_task_as.setIcon(icon3)
        self.action_save_task_as.setObjectName(_fromUtf8("action_save_task_as"))
        self.action_exit = QtGui.QAction(MainView)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_about = QtGui.QAction(MainView)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/balloon-smiley.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon4)
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

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(_translate("MainView", "Autonimo", None))
        self.dockWidget_tasks.setWindowTitle(_translate("MainView", "Tasks", None))
        self.toolBar.setWindowTitle(_translate("MainView", "toolBar", None))
        self.menuFile.setTitle(_translate("MainView", "File", None))
        self.menuHelp.setTitle(_translate("MainView", "Help", None))
        self.dockWidget.setWindowTitle(_translate("MainView", "Components", None))
        self.action_open_task.setText(_translate("MainView", "Open task...", None))
        self.action_open_task.setToolTip(_translate("MainView", "Open task", None))
        self.action_save_task.setText(_translate("MainView", "Save task", None))
        self.action_save_task.setToolTip(_translate("MainView", "Save task", None))
        self.action_save_task_as.setText(_translate("MainView", "Save task as...", None))
        self.action_save_task_as.setToolTip(_translate("MainView", "Save task as", None))
        self.action_exit.setText(_translate("MainView", "Exit", None))
        self.action_about.setText(_translate("MainView", "About", None))

import autonimo_rc
