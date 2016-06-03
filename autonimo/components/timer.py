#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from component import *


class Timer(Component):

    NAME = 'Timer'
    CATEGORY = 'General'
    DESCRIPTION = 'A timer.'

    # parameters to expose
    UI_PARAMETERS = {
        'hours': {
            KEY_NAME: 'Hours',
            KEY_NONE_ALLOWED: False,       # only applies when run as exported to a task
            KEY_EDITOR: QtGui.QSpinBox,
            KEY_EDITOR_PROPS: {
                'setMaximum': 10,
                'setSuffix': ' h',
            },
        },
        'minutes': {
            KEY_NAME: 'Minutes',
            KEY_NONE_ALLOWED: False,
            KEY_EDITOR: QtGui.QSpinBox,
            KEY_EDITOR_PROPS: {
                'setMaximum': 59,
                'setSuffix': ' m',
                'setWrapping': True,
            },
        },
        'seconds': {
            KEY_NAME: 'Seconds',
            KEY_NONE_ALLOWED: False,
            KEY_EDITOR: QtGui.QSpinBox,
            KEY_EDITOR_PROPS: {
                'setMaximum': 59,
                'setSuffix': ' s',
                'setWrapping': True,
            },
        },
    }

    # methods and their parameters to expose
    UI_METHODS = {
        'start': {
            KEY_NAME: 'Start',
            KEY_PARAMETERS: {
                'loop': {
                    KEY_NAME: 'Loop timer',
                    KEY_NONE_ALLOWED: False,
                    KEY_EDITOR: QtGui.QPushButton,
                    KEY_EDITOR_PROPS: {
                        'setCheckable': True,
                        'setIcon': 'boolean_icon',
                    },
                },
            },
        },
        'stop': {
            KEY_NAME: 'Stop',
        },
        'reset': {
            KEY_NAME: 'Reset',
        },
    }





    def set_parameters(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def start(self, loop=False):
        print 'start timer with loop={}'.format(loop)

    def stop(self):
        print 'stop timer'

    def reset(self):
        print 'reset timer'
