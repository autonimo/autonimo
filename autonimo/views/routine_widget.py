#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_routine_widget import Ui_RoutineWidget


class RoutineWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(RoutineWidget, self).__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_RoutineWidget()
        self.ui.setupUi(self)
