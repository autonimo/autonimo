#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from tasks_available_tree_model import TasksAvailableTreeModel

from PyQt4 import QtCore, QtGui


APP_VERSION = '0.1'
APP_NAME = 'Autonimo'
APP_URL = r'https://github.com/autonimo/autonimo/'


KEY_NAME = 'nice_name'
KEY_NONE_ALLOWED = 'none_allowed'
KEY_EDITOR = 'editor'
KEY_EDITOR_PROPS = 'editor_props'
KEY_PARAMETERS = 'parameters'


class Model(object):
    def __init__(self, app):
        self.app = app

        self.tasks_available_model = QtGui.QStandardItemModel()
        self.comps_available_model = QtGui.QStandardItemModel()


