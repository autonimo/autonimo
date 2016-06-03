#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
from PyQt4 import QtGui
from tasks.task import Task


class TaskController(object):
    """
    Control task creation, loading, saving, management, and running.
    """
    def __init__(self, model):


        self.model = model

        self.import_tasks_manually()


    def import_tasks_manually(self):


        from tasks.wait import Wait
        from tasks.message_print import MessagePrint



        tasks = [Wait, MessagePrint]
        tasks_by_category = {}




        # get categories and tasks
        for task in tasks:
            if task.CATEGORY not in tasks_by_category:
                tasks_by_category[task.CATEGORY] = []
            tasks_by_category[task.CATEGORY].append(task)

        # make category items
        for category in tasks_by_category:
            item_category = QtGui.QStandardItem(category)
            for task in tasks_by_category[category]:
                item = QtGui.QStandardItem(task.NAME)
                # item_desc = QtGui.QStandardItem(task.DESCRIPTION)
                # item.appendRow(item_desc)
                item.setData(task)
                item_category.appendRow(item)
            self.model.tasks_available_model.appendRow(item_category)





            # self.model.imported_tasks = [Wait]


            # print 'tasks available:', ','.join([task.NICE_NAME for task in self.model.imported_tasks])




    def import_tasks(self, path):
        """
        Attempts to load tasks from a given path.
        :param path: Path to tasks.
        :return: None.
        """
        for zz in os.walk(path):
            for module in zz[2]:

                if module.endswith('.py'):

                    import importlib

                    # from tasks.message_popup import *



                    importlib.import_module('tasks.' + module[:-3])

                    print 'imported', module



                # import module

                # mod = sys.modules[module]
                # clsmems = inspect.getmembers(mod, inspect.isclass)
                #
                # print clsmems


                # inspect.getmembers(sys.modules[__name__], inspect.isclass)
        # walk path



    # def create_task(self, ):

    def create_task(self, index):
        task = self.model.tasks_available_model.itemFromIndex(index).data()
        if task is not None and issubclass(task, Task):
            return task(self.model)


