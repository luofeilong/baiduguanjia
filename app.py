# encoding: utf-8

import sys
from PyQt4.QtGui import *
from form_login import LoginDlg

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')

    app = QApplication(sys.argv)
    dialog = LoginDlg()
    dialog.show()
    app.exec_()
