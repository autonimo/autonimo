#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gen.ui_component_main_window import Ui_ComponentMainWindow


class ComponentMainWindow(QtGui.QMainWindow):
    def __init__(self, parent):
        super(ComponentMainWindow, self).__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_ComponentMainWindow()
        self.ui.setupUi(self)
