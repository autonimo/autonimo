# required at first PyQt4 import to force API version 2
import sip
api2_classes = ['QData', 'QDateTime', 'QString', 'QTextStream', 'QTime', 'QUrl', 'QVariant',]
for cl in api2_classes:
    sip.setapi(cl, 2)
from PyQt4 import QtGui, QtCore
import sys


class Autonimo(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(Autonimo, self).__init__(sys_argv)

        # model
        self.model = Model(self)





class Model(object):
    def __init__(self, app):
        self.app = app



if __name__ == '__main__':

       # run app
    app = Autonimo(sys.argv)
    sys.exit(app.exec_())
