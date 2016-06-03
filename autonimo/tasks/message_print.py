#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from task import *
from time import sleep



class MessagePrint(Task):

    NAME = 'Print a message'
    CATEGORY = 'Other'

    # define parameter details for the parameters defined in set_parameters
    PARAMETER_TYPES_STUFF = {
        'message': {
            KEY_NAME: 'Message',
            KEY_NONE_ALLOWED: False,
            KEY_EDITOR: QtGui.QLineEdit,
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