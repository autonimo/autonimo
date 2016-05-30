#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect


class TaskController(object):
    """
    Control task creation, loading, saving, management, and running.
    """
    def __init__(self, model):


        self.model = model

        self.import_tasks_manually()


    def import_tasks_manually(self):
        from tasks.wait import Wait

        self.model.imported_tasks = [Wait]


        print 'tasks available:', ','.join([task.NICE_NAME for task in self.model.imported_tasks])

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