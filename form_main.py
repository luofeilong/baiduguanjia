# encoding: utf-8

from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time

from bcloud import gutil
from ui_mainform import Ui_Dialog_Main
# from bcloud.log import logger
# from bcloud.log import configlogger
# from bcloud import util
from bcloud import pcs

# 主窗口
class MainDlg(QWidget, Ui_Dialog_Main):
    def __init__(self, cookie=None, tokens=None, parent=None):
        super(MainDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.cookie = cookie
        self.tokens = tokens

        item = QTreeWidgetItem()
        item.setData(0, QtCore.Qt.DisplayRole, u"文件名")
        item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setData(1, QtCore.Qt.DisplayRole, u"大小")
        item.setData(2, QtCore.Qt.DisplayRole, u"修改时间")

        self.treeWidget.clear()
        self.treeWidget.setHeaderItem(item)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setIconSize(QSize(16, 16))
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setColumnWidth(0, 300)

        self.listWidget_file.clear()
        self.listWidget_file.setSpacing(8)
        self.listWidget_file.setViewMode(QListWidget.IconMode)
        self.listWidget_file.setIconSize(QSize(131, 100))
        self.listWidget_file.setGridSize(QSize(135, 120))

        self.listWidget_class.setViewMode(QListWidget.ListMode)
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_pic.png"), u"图片"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_doc.png"), u"文档"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_video.png"), u"视频"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_bt.png"), u"种子"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_music.png"), u"音乐"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_app.png"), u"应用"))
        self.listWidget_class.addItem(QListWidgetItem(QIcon(":/img/icon_class_other.png"), u"其他"))

        movie = QMovie(":/img/loding.gif")
        self.label_loding.setMovie(movie)
        movie.start()
        self.label_loding.setVisible(False)

        self.testShowClass = False
        self.testChangeModel = False
        self.lastClickItem = None
        self.lastActivatedItem = None
        self.lastActivatedItemText = None
        self.historyDir = []
        self.historyIndex = -1

        self.clickToChangeModel()
        self.clickToShowClass()

        QObject.connect(self.pushButton_backward, SIGNAL("clicked()"), self.onClickBackward)
        QObject.connect(self.pushButton_forward, SIGNAL("clicked()"), self.onClickForward)
        QObject.connect(self.pushButton_refresh, SIGNAL("clicked()"), self.onClickRefresh)
        QObject.connect(self.pushButton_newdir, SIGNAL("clicked()"), self.onClickNewDir)
        QObject.connect(self.pushButton_showclass, SIGNAL("clicked()"), self.clickToShowClass)
        QObject.connect(self.pushButton_changemodel, SIGNAL("clicked()"), self.clickToChangeModel)
        QObject.connect(self.treeWidget, SIGNAL("itemDoubleClicked(QTreeWidgetItem*, int)"), self.doubleClickTreeItem)

        QObject.connect(self.listWidget_file, SIGNAL("currentItemChanged (QListWidgetItem*,QListWidgetItem*)"), self.onListWidget_currentItemChanged)
        QObject.connect(self.listWidget_file, SIGNAL("currentRowChanged (int)"), self.onListWidget_currentRowChanged)
        QObject.connect(self.listWidget_file, SIGNAL("currentTextChanged (const QString&)"), self.onListWidget_textChanged)
        QObject.connect(self.listWidget_file, SIGNAL("itemActivated (QListWidgetItem*)"), self.onListWidget_activated)
        QObject.connect(self.listWidget_file, SIGNAL("itemChanged(QListWidgetItem*)"), self.onListWidget_itemChanged)
        QObject.connect(self.listWidget_file, SIGNAL("itemClicked (QListWidgetItem*)"), self.onListWidget_itemClicked)
        QObject.connect(self.listWidget_file, SIGNAL("itemDoubleClicked (QListWidgetItem*)"), self.onListWidget_doubleClick)
        QObject.connect(self.listWidget_file, SIGNAL("itemEntered (QListWidgetItem*)"), self.onListWidget_itemEntered)
        QObject.connect(self.listWidget_file, SIGNAL("itemPressed (QListWidgetItem*)"), self.onListWidget_itemPressed)
        QObject.connect(self.listWidget_file, SIGNAL("itemSelectionChanged()"), self.onListWidget_selectionChanged)

        # 显示第一层的文件
        self.beforeRefreshDir("/", True)

        self.dragPos = QPoint(0, 0)
        self.isMousePress = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
            if event.pos().y() < 97:
                self.isMousePress = True

        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 以下代码用于进行widget的拖拽
        if QMouseEvent.buttons() == Qt.LeftButton:
            if self.isMousePress:
                self.move(QMouseEvent.globalPos() - self.dragPos)
                QMouseEvent.accept()

        if QMouseEvent.buttons() == Qt.RightButton:
            QMouseEvent.ignore()

    def mouseReleaseEvent(self, QMouseEvent):
        self.isMousePress = False

    @pyqtSlot("PyQt_PyObject", "PyQt_PyObject", "PyQt_PyObject")
    def callbackInMainThread(self, func, info, error):
        func(info, error)

    # 通过开线程调用runfunc函数，然后通过反射机制将执行结果函数在主线程调用，防止线程中操作界面的问题
    def async_call(self, runfunc, callbackfunc, *args):
        gutil.async_call(self, "callbackInMainThread", runfunc, callbackfunc, *args)

    '''
    公用的一些函数处理
    '''
    def beforeRefreshDir(self, dirPath, isDoubleClick):
        self.label_loding.setVisible(True)
        self.pushButton_refresh.setVisible(False)
        self.pushButton_backward.setEnabled(False)
        self.pushButton_forward.setEnabled(False)
        self.listWidget_file.clear()
        self.treeWidget.clear()
        self.lineEdit_pos.setText(dirPath.decode('utf-8'))

        if isDoubleClick:
            if self.historyIndex >= 0 and self.historyIndex+1 < len(self.historyDir):
                for i in range(len(self.historyDir)-1, self.historyIndex, -1):
                    self.historyDir.pop(i)

            self.historyDir.append(dirPath)
            self.historyIndex = len(self.historyDir)-1

        self.pushButton_forward.setEnabled(False)
        self.pushButton_backward.setEnabled(False)
        self.async_call(self.refreshDir, self.onRefreshDir, dirPath)

    def afterRefreshDir(self):
        self.label_loding.setVisible(False)
        self.pushButton_refresh.setVisible(True)

        if len(self.historyDir) > 0 and self.historyIndex > 0:
            self.pushButton_backward.setEnabled(True)
        else:
            self.pushButton_backward.setEnabled(False)

        if self.historyIndex < len(self.historyDir)-1:
            self.pushButton_forward.setEnabled(True)
        else:
            self.pushButton_forward.setEnabled(False)
    '''
    QTreeWidget相关处理
    '''
    # 双击TreeWidget下的项，打开下一层文件夹
    def doubleClickTreeItem(self, item, col):
        path = self.lineEdit_pos.text() + item.text(0) + '/'
        path = str(path.toUtf8())
        self.beforeRefreshDir(path, True)


    '''
    QListWidget的相关信号处理
    '''

    # ListWidget下的项currentItemChanged
    def onListWidget_currentItemChanged(self, item1, item2):
        print 'currentItemChanged ', str(item1.text()), '  ', str(item2.text())
        pass

    # ListWidget下的项currentRowChanged
    def onListWidget_currentRowChanged(self, num):
        print 'currentRowChanged ', num
        pass

    # ListWidget下的项textChanged
    def onListWidget_textChanged(self, string):
        print 'textChanged ',str(string)
        pass

    # ListWidget下的itemActivated
    def onListWidget_activated(self, item):
        print 'itemActivated ', item.text()
        self.lastActivatedItem = item
        self.lastActivatedItemText = item.text()

        count = self.listWidget_file.count()
        for i in range(0, count):
            self.listWidget_file.closePersistentEditor(self.listWidget_file.item(i))
        pass

    # ListWidget下的itemChanged
    def onListWidget_itemChanged(self, item):
        print 'itemChanged ', item.text()
        if self.lastActivatedItem == item:
            print "try to change %s to %s" % (self.lastActivatedItemText, item.text())
            # if self.lastActivatedItemText:
            #     item.setText(self.lastActivatedItemText)
        pass

    #ListWidget下的itemClicked
    def onListWidget_itemClicked(self, item):
        if self.lastClickItem == item:
            self.listWidget_file.openPersistentEditor(item)
        print 'itemClicked ', item.text()
        self.lastClickItem = item
        pass

    # 双击ListWidget下的项
    def onListWidget_doubleClick(self, item):
        print 'doubleClick ', item.text()
        path = self.lineEdit_pos.text() + item.text() + '/'
        path = str(path.toUtf8())
        self.beforeRefreshDir(path, True)

    # ListWidget下的itemEntered
    def onListWidget_itemEntered(self, item):
        print 'itemEntered ', item.text()
        pass

    # ListWidget下的itemPressed
    def onListWidget_itemPressed(self, item):
        print 'itemPressed ', item.text()
        pass

    # ListWidget下选择项变更
    def onListWidget_selectionChanged(self):
        print 'selectionChanged '
        count = self.listWidget_file.count()
        for i in range(0, count):
            self.listWidget_file.closePersistentEditor(self.listWidget_file.item(i))

    # 后退
    def onClickBackward(self):
        if self.historyIndex > 0:
            self.historyIndex -= 1
            self.beforeRefreshDir(self.historyDir[self.historyIndex], False)

    # 向前
    def onClickForward(self):
        if self.historyIndex < (len(self.historyDir)-1):
            self.historyIndex += 1
            self.beforeRefreshDir(self.historyDir[self.historyIndex], False)

    # 刷新当前页面
    def onClickRefresh(self):
        self.beforeRefreshDir(self.historyDir[self.historyIndex], False)

    # 点击创建文件夹按钮
    def onClickNewDir(self):
        self.listWidget_file.clearSelection()
        listItem = QListWidgetItem(QIcon(":/img/folder-131-100.png"), u"新建文件夹")
        listItem.setToolTip(u"新建文件夹")
        self.listWidget_file.insertItem(0, listItem)
        self.listWidget_file.setItemSelected(listItem, True)
        self.listWidget_file.openPersistentEditor(listItem)
        self.listWidget_file.setCurrentItem(listItem)


    # 显示分类栏
    def clickToShowClass(self):
        self.listWidget_class.setVisible(self.testShowClass)
        if self.testShowClass:
            self.testShowClass = False
        else:
            self.testShowClass = True

    # 切换列表模式和图标模式
    def clickToChangeModel(self):
        if self.testChangeModel:
            self.listWidget_file.setVisible(False)
            self.treeWidget.setVisible(True)
            self.testChangeModel = False
        else:
            self.listWidget_file.setVisible(True)
            self.treeWidget.setVisible(False)
            self.testChangeModel = True

    # 刷新指定目录的文件列表
    def refreshDir(self, parent=u'/'):
        parent_, files = pcs.list_dir_all(self.cookie, self.tokens, parent)
        return (parent_, files)

    # 将指定文件项添加到ListWdiget和TreeWidget中
    def addNewItem(self, filename, filesize, modifydate, isDir):
        timeArray = time.localtime(modifydate)
        modifyTimeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        listIcon = ""
        treeIcon = ""
        if isDir:
            listIcon = ":/img/folder-131-100.png"
            treeIcon = ":/img/folder-16-16.png"
            fileSizeStr = "-"
        else:
            listIcon = ":/img/file-131-100.png"
            treeIcon = ":/img/file-16-16.png"
            fileSizeStr = "0KB"
            num = filesize/1024/1024/1024
            if num > 0:
                fileSizeStr = str(num) + "GB"
            else:
                num = filesize/1024/1024
                if num > 0:
                    fileSizeStr = str(num) + "MB"
                else:
                    num = filesize/1024
                    if num > 0:
                        fileSizeStr = str(num) + "KB"
                    else:
                        fileSizeStr = str(num) + "B"

        # 添加到listwidget
        listItem = QListWidgetItem(QIcon(listIcon), filename)
        listItem.setToolTip(filename)
        self.listWidget_file.addItem(listItem)

        # 添加到treewidget
        item = QTreeWidgetItem()
        item.setData(0, QtCore.Qt.DisplayRole, filename)
        item.setIcon(0, QIcon(treeIcon))
        item.setData(1, QtCore.Qt.DisplayRole, fileSizeStr)
        item.setData(2, QtCore.Qt.DisplayRole, modifyTimeStr)
        item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setToolTip(0, filename)

        self.treeWidget.addTopLevelItem(item)

    # 刷新目录完成后的回调函数
    def onRefreshDir(self, info, error):
        self.afterRefreshDir()
        if not info or error:
            #这里要提示出错
            return

        parent_, files = info
        for file_ in files:
            self.addNewItem(file_['server_filename'], file_['size'], file_['server_mtime'], file_['isdir'])
