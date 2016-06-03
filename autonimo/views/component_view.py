#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gen.ui_component_view import Ui_ComponentView


class ComponentView(QtGui.QMainWindow):
    def __init__(self, parent, comp):
        super(ComponentView, self).__init__(parent)
        self.comp = comp
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_ComponentView()
        self.ui.setupUi(self)

        self.setWindowTitle('Component - {}'.format(self.comp.NAME))
