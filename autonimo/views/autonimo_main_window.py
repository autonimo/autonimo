#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_autonimo_main_window import Ui_AutonimoMainWindow
# from views.task_widget import TaskWidget
# from views.component_main_window import ComponentMainWindow
# from views.routine_widget import RoutineWidget


class AutonimoMainWindow(QtGui.QMainWindow):
    def __init__(self, model):
        super(AutonimoMainWindow, self).__init__(None)
        self.model = model
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_AutonimoMainWindow()
        self.ui.setupUi(self)

        self.build_subwindows()

        # self.ui.action_routine_editor.triggered.connect(self.on_window_routine_editor)

        self.build_tasks_dockwidget()


    def build_tasks_dockwidget(self):


        self.ui.treeView_tasks_available.setModel(self.model.tasks_available_model)


        self.ui.treeView_tasks_available.setHeaderHidden(True)
        self.ui.treeView_tasks_available.expandAll()

    def build_subwindows(self):
        pass




        # samples

        # self.task_widget = TaskWidget(self)
        # _ = self.ui.mdiArea.addSubWindow(self.task_widget)
        #
        # self.task_widget2 = TaskWidget(self)
        # self.task_widget2.setWindowTitle('hello!')
        # _ = self.ui.mdiArea.addSubWindow(self.task_widget2)
        #
        # # try putting a main window in a sub window
        # self.component_main_window = ComponentMainWindow(self)
        # _ = self.ui.mdiArea.addSubWindow(self.component_main_window)
        # # self.component_main_window.show()
        #
        # self.routine_widget = RoutineWidget(self)
        # _ =  self.ui.mdiArea.addSubWindow(self.routine_widget)




    #     self.routine_editor = RoutineEditor(self)
    #     flags = self.routine_editor.windowFlags()
    #     # self.routine_editor.setWindowFlags(flags | QtCore.Qt.WindowStaysOnTopHint)
    #     # self.routine_editor.setWindowModality(QtCore.Qt)
    #
    # def on_window_routine_editor(self, checked):
    #     if checked:
    #         self.routine_editor.show()
    #     else:
    #         self.routine_editor.hide()

