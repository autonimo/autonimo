#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
from time import sleep


class KeyNames(object):
    """
    Key names for a task's parameters.
    """
    NICE_NAME = 'nice_name'
    NONE_ALLOWED = 'none_allowed'
    EDITOR = 'editor'
    EDITOR_PROPS = 'editor_props'



class Task(object):
    __metaclass__ = abc.ABCMeta

    NICE_NAME = None
    CATEGORY = None
    DESCRIPTION = None
    PARAMETER_UI_STUFF = None

    def __init__(self, model):
        self.model = model

        self._check_task()
        self.init_parameters()



    def _check_task(self):
        """
        Checks that the task class is valid.
        :return:
        """
        if self.NICE_NAME is None:
            raise TypeError('NICE_NAME cannot be NoneType')

    def _check_parameters(self):
        """
        Checks that tasks parameters exist in the task and are of the right type. Runs before the task is run.
        :return: None
        :raises TaskValidationError: the task parameter is missing or invalid.
        """
        if isinstance(self.PARAMETER_UI_STUFF, dict):
            for param in self.PARAMETER_UI_STUFF.keys():
                # check parameter value can be found
                if not hasattr(self, param) and not hasattr(Task, param):
                    raise TaskValidationError('task "{}" defines parameter "{}" but a task attribute with that name '
                                              'could not be found'.format(self.NICE_NAME, param))

                # parameter cannot be None if not explicitly allowed
                if (getattr(self, param) is None
                    and (KeyNames.NONE_ALLOWED not in self.PARAMETER_UI_STUFF[param]
                         or not self.PARAMETER_UI_STUFF[param][KeyNames.NONE_ALLOWED])):
                    raise TaskValidationError('parameter "{}" is None and None is not explicitly allowed'
                                              ''.format(param))

    def init_parameters(self):
        """
        Initialise (or reset) task parameter attributes to their default values.
        :return: None
        """
        pass

    def validate_parameters(self):
        """
        Override to add checks for task parameters and their values. Runs before the task is run.
        :return:
        :raises TaskValidationError: the task parameter is invalid.
        """
        pass

    @abc.abstractmethod
    def run(self):
        pass

    # def after_abort(self):
    #     pass

    # @property
    # def paused(self):
    #     return self._task_runner._paused

    def check_pause(self):
        """
        Call at regular intervals within long running tasks to add pause breakpoints.
        :return: time that the task was paused for, always 0.0 if it didn't pause
        :rtype: float
        """

        # todo task_runner vs model

        pause_time = 0.0
        sleep_time = 0.1
        if self.model.tasks_paused:
            while self.model.tasks_paused:
                sleep(pause_time)
                pause_time += sleep_time
        return pause_time

        #threading.Condition
        # flags? for multiprocessing and theading


    def check_abort(self):
        """
        Call at regular intervals within long running tasks to add abort breakpoints.
        :return: has the task been aborted
        :rtype: bool
        """
        if self.model.tasks_aborted:
            # do abort stuff
            self.abort()
            return True
        return False

    def abort(self):
        # called if aborted
        pass

    def finalise(self):
        # called on clean finish
        pass

    def get_dialog_response(self, severity, message, buttons, etc):
        """
        Get a response from a dialog that is shown by the main thread.
        :return:
        """
        pass

    def get_messagebox_response(self, severity, message, buttons, etc):
        """
        Get a response from a message box that is shown by the main thread.
        :return:
        """
        pass




class TaskValidationError(Exception):
    # todo
    pass


