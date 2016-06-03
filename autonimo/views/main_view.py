#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.ui_main_view import Ui_MainView
from views.component_view import ComponentView
from views.task_view import TaskView
# from views.component_main_window import ComponentMainWindow
# from views.routine_widget import RoutineWidget
from models import model


class MainView(QtGui.QMainWindow):
    def __init__(self, model, comp_ctrl, task_ctrl):
        super(MainView, self).__init__(None)
        self.model = model
        self.comp_ctrl = comp_ctrl
        self.task_ctrl = task_ctrl
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)

        # self.build_subwindows()

        # self.ui.action_routine_editor.triggered.connect(self.on_window_routine_editor)



        self.build_menu_bar()



        self.build_comps_dockwidget()
        self.build_tasks_dockwidget()


        self.ui.action_open_task.triggered.connect(self.on_open_task)

    def build_menu_bar(self):
        self.ui.action_about.triggered.connect(self.show_about)

    def show_about(self):
        QtGui.QMessageBox.information(self, model.APP_NAME, '{} v{}\n\n{}'.format(model.APP_NAME,
                                                                                  model.APP_VERSION,
                                                                                  model.APP_URL))




    def on_open_task(self):
        print self.model.app.activeWindow()
        print self.ui.mdiArea.activeSubWindow()
        print self.ui.mdiArea.focusWidget()

        print ''

    def build_comps_dockwidget(self):
        self.ui.treeView_comps_available.setModel(self.model.comps_available_model)
        self.ui.treeView_comps_available.setHeaderHidden(True)
        self.ui.treeView_comps_available.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.treeView_comps_available.expandAll()

        self.ui.treeView_comps_available.doubleClicked.connect(self.test2)

    def build_tasks_dockwidget(self):
        self.ui.treeView_tasks_available.setModel(self.model.tasks_available_model)
        self.ui.treeView_tasks_available.setHeaderHidden(True)
        self.ui.treeView_tasks_available.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.treeView_tasks_available.expandAll()

        self.ui.treeView_tasks_available.doubleClicked.connect(self.test)

    def test2(self, index):

        # make a new task subwindow
        comp = self.comp_ctrl.create_comp(index)
        if comp is not None:
            self.new_comp_subwindow(comp)

    def test(self, index):

        # make a new task subwindow
        task = self.task_ctrl.create_task(index)
        if task is not None:
            self.new_task_subwindow(task)


    def new_comp_subwindow(self, comp, params=None):
        self.comp_view = ComponentView(self, comp)
        self.ui.mdiArea.addSubWindow(self.comp_view)
        self.comp_view.show()

    def new_task_subwindow(self, task, params=None):
        self.task_view = TaskView(self, task)
        self.ui.mdiArea.addSubWindow(self.task_view)
        self.task_view.show()



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

