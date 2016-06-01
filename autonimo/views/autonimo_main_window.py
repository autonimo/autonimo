#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_autonimo_main_window import Ui_AutonimoMainWindow
from views.task_widget import TaskWidget
# from views.component_main_window import ComponentMainWindow
# from views.routine_widget import RoutineWidget



class AutonimoMainWindow(QtGui.QMainWindow):
    def __init__(self, model, task_ctrl):
        super(AutonimoMainWindow, self).__init__(None)
        self.model = model
        self.task_ctrl = task_ctrl
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_AutonimoMainWindow()
        self.ui.setupUi(self)

        # self.build_subwindows()

        # self.ui.action_routine_editor.triggered.connect(self.on_window_routine_editor)




        self.build_tasks_dockwidget()

        self.ui.action_open_task.triggered.connect(self.on_open_task)

    def on_open_task(self):
        print self.model.app.activeWindow()
        print self.ui.mdiArea.activeSubWindow()
        print self.ui.mdiArea.focusWidget()

        print ''



    def build_tasks_dockwidget(self):
        self.ui.treeView_tasks_available.setModel(self.model.tasks_available_model)
        self.ui.treeView_tasks_available.setHeaderHidden(True)
        self.ui.treeView_tasks_available.expandAll()

        # self.ui.treeView_tasks_available.clicked.connect(self.test)

        # self.mouseDoubleClickEvent.connect(self.test)

        # self.mouseDoubleClickEvent.connect(self.test)

        self.ui.treeView_tasks_available.doubleClicked.connect(self.test)
        # self.ui.treeView_tasks_available.clicked.connect(self.cont)


        # self.ui.treeView_tasks_available.contextMenuEvent()
        # self.ui.treeView_tasks_available.contextMenuPolicy()

    # def cont(self, index):
    #     print '**',  e, type(e)



    def test(self, index):

        # make a new task subwindow
        task = self.task_ctrl.create_task(index)
        if task is not None:
            print task
            # self.new_task_subwindow(task)

            self.new_task_subwindow(task)


    def new_task_subwindow(self, task, params=None):
        self.task_widget = TaskWidget(self, task)
        self.ui.mdiArea.addSubWindow(self.task_widget)
        self.task_widget.show()



    #     self.task_widget = TaskWidget(self, task)
    #
    #     # sub_window = QtGui.QMdiSubWindow()
    #     # sub_window.setWidget(task_widget)
    #
    #     # w = QtGui.QWidget(self)
    #     #
    #     # w.add
    #     #
    #     # # w.move(300, 300)
    #     # w.setWindowTitle('Simple')
    #     # w.show()
    #
    #
    #     _ = self.ui.mdiArea.addSubWindow(self.task_widget)
    #
    #     print 'ere'

        # FormWidget.show()



# class FormWidget(QtGui.QWidget):
#     def __init__(self, parent):
#         super(FormWidget, self).__init__(parent)
#         self.layout = QtGui.QVBoxLayout(self)
#
#         self.button1 = QtGui.QPushButton("Button 1")
#         self.layout.addWidget(self.button1)
#
#         self.button2 = QtGui.QPushButton("Button 2")
#         self.layout.addWidget(self.button2)
#
#         self.setLayout(self.layout)




    #
    #
    def build_subwindows(self):
    #     pass




        # samples

        # self.ui.mdiArea.closeAllSubWindows()


        self.task_widget = TaskWidget(self, None)
        _ = self.ui.mdiArea.addSubWindow(self.task_widget)
        # self.task_widget.activateWindow()
        self.task_widget.show()



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

