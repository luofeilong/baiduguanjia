# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainform.ui'
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

class Ui_Dialog_Main(object):
    def setupUi(self, Dialog_Main):
        Dialog_Main.setObjectName(_fromUtf8("Dialog_Main"))
        Dialog_Main.resize(899, 649)
        Dialog_Main.setMinimumSize(QtCore.QSize(899, 649))
        Dialog_Main.setStyleSheet(_fromUtf8("#widget_title\n"
"{\n"
"    border: 0px;\n"
"    border-top:1px solid rgb(90, 90, 90);\n"
"    border-left:1px solid rgb(90, 90, 90);\n"
"    border-right:1px solid rgb(90, 90, 90);\n"
"}\n"
"#widget_center\n"
"{\n"
"    border: 0px;\n"
"    border-bottom:1px solid rgb(90, 90, 90);\n"
"    border-left:1px solid rgb(90, 90, 90);\n"
"    border-right:1px solid rgb(90, 90, 90);\n"
"}\n"
"#widget_title\n"
"{\n"
"    background-image: url(:/img/maiform_title.png);\n"
"}\n"
"#widget_tool\n"
"{\n"
"    background-image: url(:/img/mainform_tool.png);\n"
"}\n"
"#widget_status\n"
"{\n"
"    background-image: url(:/img/maiform_statusbar.png);\n"
"}\n"
"#widget_client\n"
"{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#widget_pos\n"
"{\n"
"    background-image: url(:/img/mainform_pos.png);\n"
"}\n"
"#widget_pic\n"
"{\n"
"    background-color: rgb(5, 122, 199);\n"
"}\n"
"#label_pic\n"
"{\n"
"    background-image: url(:/img/mainform_userpic.png);\n"
"}\n"
"#label_username\n"
"{\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:18px;\n"
"    color:white;\n"
"}\n"
"QProgressBar \n"
"{\n"
"border-radius: 7px;\n"
"background: rgb(31, 80, 155);\n"
"text-align: center;\n"
"color: white;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"border-radius:7px;\n"
"border:1px solid rgb(31, 80, 155);\n"
"background:rgb(42, 196, 74);\n"
"}\n"
"\n"
"#pushButton_upload\n"
"{\n"
"    border-image: url(:/img/button_upload_normal.png);\n"
"}\n"
"#pushButton_upload:hover\n"
"{\n"
"    border-image: url(:/img/button_upload_mouseon.png);\n"
"}\n"
"#pushButton_upload:pressed\n"
"{\n"
"    border-image: url(:/img/button_upload_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_download\n"
"{\n"
"    border-image: url(:/img/button_download_normal.png);\n"
"}\n"
"#pushButton_download:hover\n"
"{\n"
"    border-image: url(:/img/button_download_mouseon.png);\n"
"}\n"
"#pushButton_download:pressed\n"
"{\n"
"    border-image: url(:/img/button_download_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_share\n"
"{\n"
"    border-image: url(:/img/button_share_normal.png);\n"
"}\n"
"#pushButton_share:hover\n"
"{\n"
"    border-image: url(:/img/button_share_mouseon.png);\n"
"}\n"
"#pushButton_share:pressed\n"
"{\n"
"    border-image: url(:/img/button_share_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_delete\n"
"{\n"
"    border-image: url(:/img/button_delete_normal.png);\n"
"}\n"
"#pushButton_delete:hover\n"
"{\n"
"    border-image: url(:/img/button_delete_mouseon.png);\n"
"}\n"
"#pushButton_delete:pressed\n"
"{\n"
"    border-image: url(:/img/button_delete_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_newdir\n"
"{\n"
"    border-image: url(:/img/button_newdir_normal.png);\n"
"}\n"
"#pushButton_newdir:hover\n"
"{\n"
"    border-image: url(:/img/button_newdir_mouseon.png);\n"
"}\n"
"#pushButton_newdir:pressed\n"
"{\n"
"    border-image: url(:/img/button_newdir_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_task\n"
"{\n"
"    border-image: url(:/img/button_task_normal.png);\n"
"}\n"
"#pushButton_task:hover\n"
"{\n"
"    border-image: url(:/img/button_task_mouseon.png);\n"
"}\n"
"#pushButton_task:pressed\n"
"{\n"
"    border-image: url(:/img/button_task_mousedown.png);\n"
"}\n"
"\n"
"#pushButton_backward\n"
"{\n"
"    border-image: url(:/img/button_backward_normal.png);\n"
"}\n"
"#pushButton_backward:hover\n"
"{\n"
"    border-image: url(:/img/button_backward_mouseon.png);\n"
"}\n"
"#pushButton_backward:pressed\n"
"{\n"
"    border-image: url(:/img/button_backward_mouseon.png);\n"
"}\n"
"\n"
"#pushButton_forward\n"
"{\n"
"    border-image: url(:/img/button_forward_normal.png);\n"
"}\n"
"#pushButton_forward:hover\n"
"{\n"
"    border-image: url(:/img/button_forward_mouseon.png);\n"
"}\n"
"#pushButton_forward:pressed\n"
"{\n"
"    border-image: url(:/img/button_forward_mouseon.png);\n"
"}\n"
"\n"
"#pushButton_refresh\n"
"{\n"
"    border-image: url(:/img/button_refresh_normal.png);\n"
"}\n"
"#pushButton_refresh:hover\n"
"{\n"
"    border-image: url(:/img/button_refresh_mouseon.png);\n"
"}\n"
"#pushButton_refresh:pressed\n"
"{\n"
"    border-image: url(:/img/button_refresh_mouseon.png);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    border-radius:2px;\n"
"    border:1px solid rgb(225, 225, 225);\n"
"    font-family:\'Microsoft YaHei\';\n"
"}\n"
"\n"
"#pushButton_showclass\n"
"{\n"
"    border-image: url(:/img/button_class_normal.png);\n"
"}\n"
"#pushButton_showclass:hover\n"
"{\n"
"    border-image: url(:/img/button_class_mouseon.png);\n"
"}\n"
"#pushButton_showclass:pressed\n"
"{\n"
"    border-image: url(:/img/button_class_mouseon.png);\n"
"}\n"
"\n"
"#pushButton_changemodel\n"
"{\n"
"    border-image: url(:/img/button_icon_normal.png);\n"
"}\n"
"#pushButton_changemodel:hover\n"
"{\n"
"    border-image: url(:/img/button_icon_mouseon.png);\n"
"}\n"
"#pushButton_changemodel:pressed\n"
"{\n"
"    border-image: url(:/img/button_icon_mouseon.png);\n"
"}\n"
"\n"
"#listWidget_file, #treeWidget\n"
"{\n"
"    border: 0px;\n"
"    font-family:\'Microsoft YaHei\';\n"
"}\n"
"\n"
"#listWidget_class\n"
"{\n"
"    border: 0px;\n"
"    border-right:1px solid rgb(230, 230, 230);\n"
"    font-family:\'Microsoft YaHei\';\n"
"    padding-left:22;\n"
"}"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog_Main)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_title = QtGui.QWidget(Dialog_Main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(0, 97))
        self.widget_title.setMaximumSize(QtCore.QSize(16777215, 97))
        self.widget_title.setObjectName(_fromUtf8("widget_title"))
        self.widget_pic = QtGui.QWidget(self.widget_title)
        self.widget_pic.setGeometry(QtCore.QRect(15, 15, 66, 66))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_pic.sizePolicy().hasHeightForWidth())
        self.widget_pic.setSizePolicy(sizePolicy)
        self.widget_pic.setMinimumSize(QtCore.QSize(66, 66))
        self.widget_pic.setMaximumSize(QtCore.QSize(66, 66))
        self.widget_pic.setObjectName(_fromUtf8("widget_pic"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_pic)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_pic = QtGui.QLabel(self.widget_pic)
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.verticalLayout_2.addWidget(self.label_pic)
        self.label_username = QtGui.QLabel(self.widget_title)
        self.label_username.setGeometry(QtCore.QRect(94, 27, 111, 21))
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.progressBar = QtGui.QProgressBar(self.widget_title)
        self.progressBar.setGeometry(QtCore.QRect(94, 56, 131, 14))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.widget_title)
        self.widget_center = QtGui.QWidget(Dialog_Main)
        self.widget_center.setObjectName(_fromUtf8("widget_center"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_center)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_tool = QtGui.QWidget(self.widget_center)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_tool.sizePolicy().hasHeightForWidth())
        self.widget_tool.setSizePolicy(sizePolicy)
        self.widget_tool.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_tool.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_tool.setObjectName(_fromUtf8("widget_tool"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_tool)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget_3 = QtGui.QWidget(self.widget_tool)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setContentsMargins(10, 3, 3, 3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_upload = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upload.sizePolicy().hasHeightForWidth())
        self.pushButton_upload.setSizePolicy(sizePolicy)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(75, 32))
        self.pushButton_upload.setMaximumSize(QtCore.QSize(75, 32))
        self.pushButton_upload.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_upload.setText(_fromUtf8(""))
        self.pushButton_upload.setObjectName(_fromUtf8("pushButton_upload"))
        self.horizontalLayout_2.addWidget(self.pushButton_upload)
        self.pushButton_download = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_download.sizePolicy().hasHeightForWidth())
        self.pushButton_download.setSizePolicy(sizePolicy)
        self.pushButton_download.setMinimumSize(QtCore.QSize(75, 32))
        self.pushButton_download.setMaximumSize(QtCore.QSize(75, 32))
        self.pushButton_download.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_download.setText(_fromUtf8(""))
        self.pushButton_download.setObjectName(_fromUtf8("pushButton_download"))
        self.horizontalLayout_2.addWidget(self.pushButton_download)
        self.pushButton_share = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_share.sizePolicy().hasHeightForWidth())
        self.pushButton_share.setSizePolicy(sizePolicy)
        self.pushButton_share.setMinimumSize(QtCore.QSize(75, 32))
        self.pushButton_share.setMaximumSize(QtCore.QSize(75, 32))
        self.pushButton_share.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_share.setText(_fromUtf8(""))
        self.pushButton_share.setObjectName(_fromUtf8("pushButton_share"))
        self.horizontalLayout_2.addWidget(self.pushButton_share)
        self.pushButton_delete = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(75, 32))
        self.pushButton_delete.setMaximumSize(QtCore.QSize(75, 32))
        self.pushButton_delete.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_delete.setText(_fromUtf8(""))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.horizontalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_newdir = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_newdir.sizePolicy().hasHeightForWidth())
        self.pushButton_newdir.setSizePolicy(sizePolicy)
        self.pushButton_newdir.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_newdir.setMaximumSize(QtCore.QSize(110, 32))
        self.pushButton_newdir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_newdir.setText(_fromUtf8(""))
        self.pushButton_newdir.setObjectName(_fromUtf8("pushButton_newdir"))
        self.horizontalLayout_2.addWidget(self.pushButton_newdir)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget_2 = QtGui.QWidget(self.widget_tool)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(354, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_task = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_task.sizePolicy().hasHeightForWidth())
        self.pushButton_task.setSizePolicy(sizePolicy)
        self.pushButton_task.setMinimumSize(QtCore.QSize(92, 34))
        self.pushButton_task.setMaximumSize(QtCore.QSize(92, 34))
        self.pushButton_task.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_task.setText(_fromUtf8(""))
        self.pushButton_task.setObjectName(_fromUtf8("pushButton_task"))
        self.horizontalLayout.addWidget(self.pushButton_task)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_tool)
        self.widget_pos = QtGui.QWidget(self.widget_center)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_pos.sizePolicy().hasHeightForWidth())
        self.widget_pos.setSizePolicy(sizePolicy)
        self.widget_pos.setMinimumSize(QtCore.QSize(0, 39))
        self.widget_pos.setMaximumSize(QtCore.QSize(16777215, 39))
        self.widget_pos.setObjectName(_fromUtf8("widget_pos"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_pos)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setContentsMargins(5, 2, 2, 2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.widget_4 = QtGui.QWidget(self.widget_pos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(125, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(125, 16777215))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.pushButton_backward = QtGui.QPushButton(self.widget_4)
        self.pushButton_backward.setGeometry(QtCore.QRect(20, 10, 18, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_backward.sizePolicy().hasHeightForWidth())
        self.pushButton_backward.setSizePolicy(sizePolicy)
        self.pushButton_backward.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_backward.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_backward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_backward.setText(_fromUtf8(""))
        self.pushButton_backward.setObjectName(_fromUtf8("pushButton_backward"))
        self.pushButton_forward = QtGui.QPushButton(self.widget_4)
        self.pushButton_forward.setGeometry(QtCore.QRect(50, 10, 18, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_forward.sizePolicy().hasHeightForWidth())
        self.pushButton_forward.setSizePolicy(sizePolicy)
        self.pushButton_forward.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_forward.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_forward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_forward.setText(_fromUtf8(""))
        self.pushButton_forward.setObjectName(_fromUtf8("pushButton_forward"))
        self.pushButton_refresh = QtGui.QPushButton(self.widget_4)
        self.pushButton_refresh.setGeometry(QtCore.QRect(90, 10, 18, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        self.pushButton_refresh.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_refresh.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_refresh.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_refresh.setText(_fromUtf8(""))
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.label_loding = QtGui.QLabel(self.widget_4)
        self.label_loding.setGeometry(QtCore.QRect(90, 10, 18, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_loding.sizePolicy().hasHeightForWidth())
        self.label_loding.setSizePolicy(sizePolicy)
        self.label_loding.setMaximumSize(QtCore.QSize(18, 18))
        self.label_loding.setText(_fromUtf8(""))
        self.label_loding.setObjectName(_fromUtf8("label_loding"))
        self.horizontalLayout_4.addWidget(self.widget_4)
        self.lineEdit_pos = QtGui.QLineEdit(self.widget_pos)
        self.lineEdit_pos.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pos.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_pos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_pos.setReadOnly(True)
        self.lineEdit_pos.setObjectName(_fromUtf8("lineEdit_pos"))
        self.horizontalLayout_4.addWidget(self.lineEdit_pos)
        self.lineEdit_search = QtGui.QLineEdit(self.widget_pos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.horizontalLayout_4.addWidget(self.lineEdit_search)
        self.widget = QtGui.QWidget(self.widget_pos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(60, 0))
        self.widget.setMaximumSize(QtCore.QSize(60, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton_showclass = QtGui.QPushButton(self.widget)
        self.pushButton_showclass.setGeometry(QtCore.QRect(10, 12, 14, 14))
        self.pushButton_showclass.setText(_fromUtf8(""))
        self.pushButton_showclass.setObjectName(_fromUtf8("pushButton_showclass"))
        self.pushButton_changemodel = QtGui.QPushButton(self.widget)
        self.pushButton_changemodel.setGeometry(QtCore.QRect(37, 12, 14, 14))
        self.pushButton_changemodel.setText(_fromUtf8(""))
        self.pushButton_changemodel.setObjectName(_fromUtf8("pushButton_changemodel"))
        self.horizontalLayout_4.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_pos)
        self.widget_client = QtGui.QWidget(self.widget_center)
        self.widget_client.setObjectName(_fromUtf8("widget_client"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_client)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.listWidget_class = QtGui.QListWidget(self.widget_client)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_class.sizePolicy().hasHeightForWidth())
        self.listWidget_class.setSizePolicy(sizePolicy)
        self.listWidget_class.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidget_class.setMaximumSize(QtCore.QSize(120, 16777215))
        self.listWidget_class.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget_class.setSpacing(5)
        self.listWidget_class.setObjectName(_fromUtf8("listWidget_class"))
        self.horizontalLayout_5.addWidget(self.listWidget_class)
        self.widget_right = QtGui.QWidget(self.widget_client)
        self.widget_right.setObjectName(_fromUtf8("widget_right"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_right)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.treeWidget = QtGui.QTreeWidget(self.widget_right)
        self.treeWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.treeWidget.setIndentation(2)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.headerItem().setText(1, _fromUtf8("2"))
        self.treeWidget.headerItem().setText(2, _fromUtf8("3"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.horizontalLayout_6.addWidget(self.treeWidget)
        self.listWidget_file = QtGui.QListWidget(self.widget_right)
        self.listWidget_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_file.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget_file.setLineWidth(0)
        self.listWidget_file.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.listWidget_file.setAlternatingRowColors(False)
        self.listWidget_file.setIconSize(QtCore.QSize(131, 100))
        self.listWidget_file.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget_file.setMovement(QtGui.QListView.Static)
        self.listWidget_file.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget_file.setLayoutMode(QtGui.QListView.SinglePass)
        self.listWidget_file.setSpacing(10)
        self.listWidget_file.setGridSize(QtCore.QSize(135, 122))
        self.listWidget_file.setViewMode(QtGui.QListView.IconMode)
        self.listWidget_file.setUniformItemSizes(True)
        self.listWidget_file.setWordWrap(False)
        self.listWidget_file.setSelectionRectVisible(False)
        self.listWidget_file.setObjectName(_fromUtf8("listWidget_file"))
        item = QtGui.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/folder-131-100.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon)
        self.listWidget_file.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget_file.addItem(item)
        self.horizontalLayout_6.addWidget(self.listWidget_file)
        self.horizontalLayout_5.addWidget(self.widget_right)
        self.verticalLayout.addWidget(self.widget_client)
        self.widget_status = QtGui.QWidget(self.widget_center)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_status.sizePolicy().hasHeightForWidth())
        self.widget_status.setSizePolicy(sizePolicy)
        self.widget_status.setMinimumSize(QtCore.QSize(0, 34))
        self.widget_status.setMaximumSize(QtCore.QSize(16777215, 34))
        self.widget_status.setObjectName(_fromUtf8("widget_status"))
        self.label_status = QtGui.QLabel(self.widget_status)
        self.label_status.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.verticalLayout.addWidget(self.widget_status)
        self.verticalLayout_3.addWidget(self.widget_center)

        self.retranslateUi(Dialog_Main)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Main)

    def retranslateUi(self, Dialog_Main):
        Dialog_Main.setWindowTitle(_translate("Dialog_Main", "Dialog", None))
        self.label_username.setText(_translate("Dialog_Main", "Dragon", None))
        self.lineEdit_search.setPlaceholderText(_translate("Dialog_Main", "搜索我的网盘文件", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog_Main", "111", None))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Dialog_Main", "111", None))
        self.treeWidget.topLevelItem(0).setText(2, _translate("Dialog_Main", "111", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog_Main", "222", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("Dialog_Main", "222", None))
        self.treeWidget.topLevelItem(1).setText(2, _translate("Dialog_Main", "222", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_file.isSortingEnabled()
        self.listWidget_file.setSortingEnabled(False)
        item = self.listWidget_file.item(0)
        item.setText(_translate("Dialog_Main", "新建项目", None))
        item = self.listWidget_file.item(1)
        item.setText(_translate("Dialog_Main", "新建项目112211221122asaasasasas", None))
        self.listWidget_file.setSortingEnabled(__sortingEnabled)

import res_mainform_rc
