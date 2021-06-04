# -*- coding: utf-8 -*-
#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import asd


class Mywindown(QtWidgets.QMainWindow,asd.Ui_MainWindow):
    pass
    def __init__(self, parent=None):
        super(Mywindown,self).__init__(parent)
        self.setupUi(self)
if __name__=="__main__":
    pass
    app=QtWidgets.QApplication(sys.argv)
    win=Mywindown()
    win.show()
    sys.exit(app.exec())

