#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
from PyQt4 import QtGui
from time import sleep
from models.model import KEY_NAME, KEY_NONE_ALLOWED, KEY_EDITOR, KEY_EDITOR_PROPS, KEY_PARAMETERS



class Component(object):
    __metaclass__ = abc.ABCMeta

    NAME = None
    CATEGORY = None
    DESCRIPTION = None
    UI_PARAMETERS = None
    UI_METHODS = None

    def __init__(self, model):
        self.model = model

        self._check_component()
        self.set_parameters()

    def _check_component(self):
        """
        Checks that the component subclass is valid.
        :return:
        """
        if self.NAME is None:
            raise TypeError('NICE_NAME cannot be NoneType')

    def set_parameters(self):
        pass


    # what about buttons etc that are clickable, have actions based on each button, action may recive button state?
    # components have to be written for that





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