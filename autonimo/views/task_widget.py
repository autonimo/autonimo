#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_task_widget import Ui_TaskWidget


class TaskWidget(QtGui.QWidget):
    def __init__(self, parent, task):
        super(TaskWidget, self).__init__(parent)
        self.task = task
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_TaskWidget()
        self.ui.setupUi(self)

        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(24)

        self.ui.pushButton_run.clicked.connect(self.run_task)

        self.setWindowTitle('Task - {}'.format(self.task.NICE_NAME))


        self.ui.tableView.setModel(QtGui.QStringListModel([
            'asdf', 'asdf234f',
            'asdf', 'asdf234f',
            'asdf', 'asdf234f',
            'asdf', 'asdf234f',
            'asdf', 'asdf234f',
            'asdf', 'asdf234f',
        ]))


    def run_task(self):
        self.task.run()
        print 'ran', self

