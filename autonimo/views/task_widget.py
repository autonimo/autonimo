#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_task_widget import Ui_TaskWidget


class TaskWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(TaskWidget, self).__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_TaskWidget()
        self.ui.setupUi(self)


