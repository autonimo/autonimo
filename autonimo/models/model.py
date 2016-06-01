#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from tasks_available_tree_model import TasksAvailableTreeModel

from PyQt4 import QtCore, QtGui


class Model(object):
    def __init__(self, app):
        self.app = app



        # self.tasks_available_tree_model = TasksAvailableTreeModel()
        # self.tasks_available = {}
        self.tasks_available_model = QtGui.QStandardItemModel()

        self.tasks_open = [
            # (task1, view1),
        ]


        # p = QtGui.QStandardItem('aaaa')
        # c = QtGui.QStandardItem('23rsdfasdfsaf')
        # p.appendRow(c)
        #
        # p2 = QtGui.QStandardItem('aaaa')
        # c2 = QtGui.QStandardItem('bbbbbb')
        # p2.appendRow(c2)




        # self.tasks_available_model.appendRow(p)
        # self.tasks_available_model.appendRow(p2)






        # use qdirmodel for file system