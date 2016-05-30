#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from task import Task, TaskValidationError, KeyNames
from time import sleep



class MessagePrint(Task):

    NICE_NAME = 'Print a message'
    CATEGORY = 'General'

    # define parameter details for the parameters defined in set_parameters
    PARAMETER_TYPES_STUFF = {
        'message': {
            KeyNames.NICE_NAME: 'Message',
            KeyNames.NONE_ALLOWED: False,
            KeyNames.EDITOR: QtGui.QLineEdit,
            # Keys.EDITOR_PROPS: {
            # },
        },
    }

    def set_parameters(self):
        """
        Set task parameter attributes and their default values.
        :return: None
        """
        self.message = 'hi'

    def run(self):
        self.validate()
        print self.message


if __name__ == '__main__':

    w = MessagePrint()
    w.run()