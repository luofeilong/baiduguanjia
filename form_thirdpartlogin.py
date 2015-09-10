# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_thirdpartlogin.ui'
#
# Created: Thu Apr 02 13:22:25 2015
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtWebKit
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ThirdPartDlg(QDialog):
    def __init__(self, parent=None):
        super(ThirdPartDlg, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.setWindowTitle(_fromUtf8("Third part login"))
        self.resize(710, 414)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(self)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.Tool)
        self.htmlData = ""

        QtCore.QObject.connect(self.webView, QtCore.SIGNAL("loadProgress(int)"), self.load_progress)

    def load_progress(self, load):
        if load == 100:
            url = str(self.webView.url().toString())
            #print "finish load! url=%s" % url
            if url.find('http://passport.baidu.com/phoenix/account/afterauth?mkey=') == 0:
                self.htmlData = str(self.webView.page().currentFrame().documentElement().toInnerXml())
                self.close()

    def showThirdPartLoginDlg(self, url):
        self.webView.load(QUrl(url))
        self.exec_()
        return self.htmlData

