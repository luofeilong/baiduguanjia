# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_loginform.ui'
#
# Created: Tue Apr 28 20:28:56 2015
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog_Login(object):
    def setupUi(self, Dialog_Login):
        Dialog_Login.setObjectName(_fromUtf8("Dialog_Login"))
        Dialog_Login.resize(659, 439)
        Dialog_Login.setStyleSheet(_fromUtf8("#Dialog_Login\n"
"{\n"
"    border-radius:3px;\n"
"    border:1px solid rgb(56, 76, 158);\n"
"}\n"
"#widget_client\n"
"{\n"
"    background-image: url(:/img/login.PNG);\n"
"    border-radius:3px;\n"
"    border:1px solid rgb(56, 76, 158);\n"
"}\n"
"#pushButton_login\n"
"{\n"
"    border-image: url(:/img/login_button_normal.PNG);\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:16px;\n"
"    color:white;\n"
"}\n"
"#pushButton_login:hover\n"
"{\n"
"    border-image: url(:/img/login_button_on.PNG);\n"
"}\n"
"#pushButton_login:pressed\n"
"{\n"
"    border-image: url(:/img/login_button_down.PNG);\n"
"}\n"
"#pushButton_min\n"
"{\n"
"    border-image: url(:/img/button_min_normal.png);\n"
"}\n"
"#pushButton_min:hover\n"
"{\n"
"    border-image: url(:/img/button_min_mouseon.png);\n"
"}\n"
"#pushButton_min:pressed\n"
"{\n"
"    border-image: url(:/img/button_min_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_close\n"
"{\n"
"    border-image: url(:/img/button_close_normal.png);\n"
"}\n"
"#pushButton_close:hover\n"
"{\n"
"    border-image: url(:/img/button_close_mouseon.png);\n"
"}\n"
"#pushButton_close:pressed\n"
"{\n"
"    border-image: url(:/img/button_close_mousedown.png);\n"
"}\n"
"\n"
"lineEdit\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"}\n"
"#lineEdit_user\n"
"{\n"
"    padding-left:22;\n"
"    border-image: url(:/img/lineEdit_user.PNG);\n"
"}\n"
"\n"
"#lineEdit_pwd\n"
"{\n"
"    padding-left:22;\n"
"    border-image: url(:/img/lineEdit_pwd.PNG);\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:rgb(90,90,90);\n"
"}\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"    image:url(:/img/checkbox_unchecked.PNG);\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/img/checkbox_checked.PNG);\n"
"}\n"
"\n"
"#label_forgetpwd\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:rgb(9,124,224);\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#label_forgetpwd:hover\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:rgb(9,124,224);\n"
"}\n"
"\n"
"#label_xinlang:hover, #label_qq:hover, #label_renren:hover\n"
"{\n"
"    border-radius:3px;\n"
"    border:1px solid rgb(171, 175, 177);\n"
"}\n"
"\n"
"#label_error\n"
"{\n"
"    border-image: url(:/img/button_error.png);\n"
"}\n"
"\n"
"#label_errorinfo\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:red;\n"
"}\n"
"\n"
"#label_auth\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:rgb(170,170,170);\n"
"}\n"
"\n"
"#pushButton_QQlogin\n"
"{\n"
"    border-image: url(:/img/button_qqlogin_normal.png);\n"
"}\n"
"#pushButton_QQlogin:hover\n"
"{\n"
"    border-image: url(:/img/button_qqlogin_mouseon.png);\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_Login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_client = QtGui.QWidget(Dialog_Login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_client.sizePolicy().hasHeightForWidth())
        self.widget_client.setSizePolicy(sizePolicy)
        self.widget_client.setMinimumSize(QtCore.QSize(659, 439))
        self.widget_client.setMaximumSize(QtCore.QSize(659, 439))
        self.widget_client.setStyleSheet(_fromUtf8(""))
        self.widget_client.setObjectName(_fromUtf8("widget_client"))
        self.pushButton_login = QtGui.QPushButton(self.widget_client)
        self.pushButton_login.setGeometry(QtCore.QRect(362, 277, 249, 37))
        self.pushButton_login.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_login.setAutoDefault(False)
        self.pushButton_login.setDefault(False)
        self.pushButton_login.setFlat(True)
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.lineEdit_user = QtGui.QLineEdit(self.widget_client)
        self.lineEdit_user.setGeometry(QtCore.QRect(363, 175, 245, 25))
        self.lineEdit_user.setMaxLength(64)
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.lineEdit_pwd = QtGui.QLineEdit(self.widget_client)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(363, 210, 245, 25))
        self.lineEdit_pwd.setMaxLength(32)
        self.lineEdit_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName(_fromUtf8("lineEdit_pwd"))
        self.checkBox_rempwd = QtGui.QCheckBox(self.widget_client)
        self.checkBox_rempwd.setGeometry(QtCore.QRect(379, 246, 71, 16))
        self.checkBox_rempwd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_rempwd.setObjectName(_fromUtf8("checkBox_rempwd"))
        self.checkBox_autologin = QtGui.QCheckBox(self.widget_client)
        self.checkBox_autologin.setGeometry(QtCore.QRect(460, 246, 71, 16))
        self.checkBox_autologin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_autologin.setObjectName(_fromUtf8("checkBox_autologin"))
        self.label_forgetpwd = QtGui.QLabel(self.widget_client)
        self.label_forgetpwd.setGeometry(QtCore.QRect(550, 247, 70, 16))
        self.label_forgetpwd.setScaledContents(False)
        self.label_forgetpwd.setObjectName(_fromUtf8("label_forgetpwd"))
        self.label_error = QtGui.QLabel(self.widget_client)
        self.label_error.setGeometry(QtCore.QRect(365, 158, 14, 14))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy)
        self.label_error.setMinimumSize(QtCore.QSize(14, 14))
        self.label_error.setMaximumSize(QtCore.QSize(14, 14))
        self.label_error.setText(_fromUtf8(""))
        self.label_error.setObjectName(_fromUtf8("label_error"))
        self.label_errorinfo = QtGui.QLabel(self.widget_client)
        self.label_errorinfo.setGeometry(QtCore.QRect(390, 158, 211, 16))
        self.label_errorinfo.setText(_fromUtf8(""))
        self.label_errorinfo.setObjectName(_fromUtf8("label_errorinfo"))
        self.label_auth = QtGui.QLabel(self.widget_client)
        self.label_auth.setGeometry(QtCore.QRect(393, 400, 241, 20))
        self.label_auth.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_auth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_auth.setObjectName(_fromUtf8("label_auth"))
        self.pushButton_QQlogin = QtGui.QPushButton(self.widget_client)
        self.pushButton_QQlogin.setGeometry(QtCore.QRect(457, 357, 22, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_QQlogin.sizePolicy().hasHeightForWidth())
        self.pushButton_QQlogin.setSizePolicy(sizePolicy)
        self.pushButton_QQlogin.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_QQlogin.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton_QQlogin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_QQlogin.setText(_fromUtf8(""))
        self.pushButton_QQlogin.setObjectName(_fromUtf8("pushButton_QQlogin"))
        self.pushButton_min = QtGui.QPushButton(self.widget_client)
        self.pushButton_min.setGeometry(QtCore.QRect(591, 1, 32, 20))
        self.pushButton_min.setMinimumSize(QtCore.QSize(32, 20))
        self.pushButton_min.setMaximumSize(QtCore.QSize(32, 20))
        self.pushButton_min.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_min.setText(_fromUtf8(""))
        self.pushButton_min.setObjectName(_fromUtf8("pushButton_min"))
        self.pushButton_close = QtGui.QPushButton(self.widget_client)
        self.pushButton_close.setGeometry(QtCore.QRect(624, 1, 32, 20))
        self.pushButton_close.setMinimumSize(QtCore.QSize(32, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(32, 20))
        self.pushButton_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_close.setText(_fromUtf8(""))
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.verticalLayout.addWidget(self.widget_client)

        self.retranslateUi(Dialog_Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Login)

    def retranslateUi(self, Dialog_Login):
        Dialog_Login.setWindowTitle(_translate("Dialog_Login", "Dialog", None))
        self.pushButton_login.setText(_translate("Dialog_Login", "登录", None))
        self.lineEdit_user.setPlaceholderText(_translate("Dialog_Login", "手机号/邮箱/用户名", None))
        self.lineEdit_pwd.setPlaceholderText(_translate("Dialog_Login", "密码", None))
        self.checkBox_rempwd.setText(_translate("Dialog_Login", "记住密码", None))
        self.checkBox_autologin.setText(_translate("Dialog_Login", "自动登录", None))
        self.label_forgetpwd.setText(_translate("Dialog_Login", "忘记密码?", None))
        self.label_auth.setText(_translate("Dialog_Login", "2015 Dragon All Rights Reserved", None))

import res_loginform_rc
