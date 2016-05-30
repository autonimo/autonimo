#!/usr/bin/env python
# -*- coding: utf-8 -*-

# required at first PyQt4 import to force API version 2
import sip
api2_classes = ['QData', 'QDateTime', 'QString', 'QTextStream', 'QTime', 'QUrl', 'QVariant',]
for cl in api2_classes:
    sip.setapi(cl, 2)
from PyQt4 import QtGui, QtCore
import sys


class StandaloneComponentDemo(QtGui.QApplication):

    test_sig = QtCore.pyqtSignal()

    def __init__(self, sys_argv):
        super(StandaloneComponentDemo, self).__init__(sys_argv)

        # views
        # self.main = QtGui.QMainWindow()
        # self.main.show()

        # attempt to add a toolbar to a standalone component (a widget) and then add it to a main window
        self.standalone_component = QtGui.QWidget(None)

        self.sc_layout = QtGui.QGridLayout()
        self.standalone_component.setLayout(self.sc_layout)


        self.sc_menubar = QtGui.QMenuBar()
        self.sc_menubar.addMenu('File')
        self.sc_layout.setMenuBar(self.sc_menubar)


        # self.sc_toolbar = QtGui.QToolBar()
        # self.sc_action1 = QtGui.QAction("asdf", self.standalone_component)
        # self.sc_toolbar.addAction(self.sc_action1)
        # self.sc_layout.addWidget(self.sc_toolbar)



        self.standalone_component.show()

        # self.main.addToolBar()




if __name__ == '__main__':
    app = StandaloneComponentDemo(sys.argv)
    sys.exit(app.exec_())
