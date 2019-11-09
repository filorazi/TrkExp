from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QDateTime, Qt, QTimer
from gui import *
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    gallery = Gui()
    gallery.show()
    appctxt.app.exec_()
