#!/usr/bin/env python
# -*- coding: utf-8 -*-

# required at first PyQt4 import to force API version 2
import sip
api2_classes = ['QData', 'QDateTime', 'QString', 'QTextStream', 'QTime', 'QUrl', 'QVariant',]
for cl in api2_classes:
    sip.setapi(cl, 2)
from PyQt4 import QtGui, QtCore
import sys
from models.model import Model
from ctrls.task_ctrl import TaskController
from views.autonimo_main_window import AutonimoMainWindow



# required for resource files
import autonimo_rc


class Autonimo(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(Autonimo, self).__init__(sys_argv)

        # model
        self.model = Model(self)

        # controllers
        self.task_ctrl = TaskController(self.model)
        # self.task_ctrl.import_tasks('tasks')


        # views
        self.main_view = AutonimoMainWindow(self.model)
        self.main_view.show()


if __name__ == '__main__':

       # run app
    app = Autonimo(sys.argv)
    sys.exit(app.exec_())
