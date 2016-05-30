#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from task import Task, TaskValidationError, KeyNames
from time import sleep



class Wait(Task):

    #
    # @property
    # def something(self):
    #     return 1/0


    NICE_NAME = 'Wait'
    CATEGORY = 'Networking'

    # define parameter details for the parameters defined in set_parameters
    PARAMETER_UI_STUFF = {
        'sleep_time': {
            KeyNames.NICE_NAME: 'Time to sleep',
            KeyNames.NONE_ALLOWED: False,
            KeyNames.EDITOR: QtGui.QSpinBox,
            KeyNames.EDITOR_PROPS: {
                'setMaximum': 10,
                'setSuffix': ' sec',
            },
        },
        'other_param': {
            KeyNames.NICE_NAME: 'Another parameter',
            KeyNames.NONE_ALLOWED: False,
            KeyNames.EDITOR: QtGui.QSpinBox,
            KeyNames.EDITOR_PROPS: {
                'setMaximum': 5,
                'setSuffix': ' sec',
            },

        },
    }

    def init_parameters(self):
        self.sleep_time = 3
        self.other_param = 1

    def validate_parameters(self):
        if self.sleep_time > 10:
            raise TaskValidationError('sleep time of {} too long'.format(self.sleep_time))

    def run(self):
        print 'waiting {} second(s)...'.format(self.sleep_time)
        sleep(self.sleep_time)
        print 'done waiting'



if __name__ == '__main__':

    w = Wait(None)
    w._check_parameters()
    w.validate_parameters()
    w.run()