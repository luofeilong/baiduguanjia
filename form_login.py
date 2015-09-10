# encoding: utf-8

import os
import json
import BeautifulSoup
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from bcloud import gutil
from bcloud import auth
from bcloud import util
from bcloud.log import logger
from bcloud.log import configlogger
from bcloud import Config
from bcloud.RequestCookie import RequestCookie
from ui_loginform import Ui_Dialog_Login
from form_thirdpartlogin import ThirdPartDlg
from form_main import MainDlg

# 登录窗口
class LoginDlg(QWidget, Ui_Dialog_Login):
    profile = None
    password_changed = False
    userLogin = QtCore.pyqtSignal()

    @pyqtSlot("PyQt_PyObject", "PyQt_PyObject", "PyQt_PyObject")
    def callbackInMainThread(self, func, info, error):
        func(info, error)

    # 通过开线程调用runfunc函数，然后通过反射机制将执行结果函数在主线程调用，防止线程中操作界面的问题
    def async_call(self, runfunc, callbackfunc, *args):
        gutil.async_call(self, "callbackInMainThread", runfunc, callbackfunc, *args)

    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.label_error.setVisible(False)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # 绑定登录按钮点击信号处理
        QObject.connect(self.pushButton_login, SIGNAL("clicked()"), self.clicklogin)
        QObject.connect(self.pushButton_close, SIGNAL("clicked()"), self.onClickClose)
        QObject.connect(self.pushButton_min, SIGNAL("clicked()"), self.onClickMin)

        # 绑定使用qq登录
        QObject.connect(self.pushButton_QQlogin, SIGNAL("clicked()"), self.clickQQlogin)

        # 设置忘记密码点击弹窗
        self.label_forgetpwd.setOpenExternalLinks(True)
        self.label_forgetpwd.setText(QtCore.QString.fromUtf8("<a style='color: rgb(9,124,224);' href = \"https://passport.baidu.com/?getpass_index\">忘记密码?</a>"))

        # 初始化logger变量
        configlogger(logger, 0)

        self.conf = Config.load_conf()
        self.profile = None

        self.dragPos = QPoint(0, 0)
        self.isMousePress = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
            curpos = event.pos()
            if curpos.y() < 85:
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

    def onClickClose(self):
        self.close()

    def onClickMin(self):
        self.showMinimized()

    # 使用第三方登录：QQ
    def clickQQlogin(self):
        cookie = RequestCookie()
        tokens = {}
        username = ''

        self.dlg = ThirdPartDlg(self)
        data = self.dlg.showThirdPartLoginDlg('http://passport.baidu.com/phoenix/account/startlogin?u=http://pan.baidu.com&type=15&display=pc&tpl=netdisk&act=implicit')

        tags = BeautifulSoup.BeautifulSoup(data).findAll('bduss')
        if tags and len(tags) > 0:
            for tag in tags:
                temp = []
                temp.append(''.join("BDUSS=%s"%str(tag.text)))
                tokens['bduss'] = tag.text
                cookie.load_list(temp)

        tags = BeautifulSoup.BeautifulSoup(data).findAll('ptoken')
        if tags and len(tags) > 0:
            for tag in tags:
                temp = []
                temp.append(''.join("ptoken=%s"%str(tag.text)))
                tokens['ptoken'] = tag.text
                cookie.load_list(temp)

        tags = BeautifulSoup.BeautifulSoup(data).findAll('display_name')
        if tags and len(tags) > 0:
            for tag in tags:
                username = str(tag.text)

        def on_get_bdstoken(bdstoken, error=None):
            if error or not bdstoken:
                logger.error('SigninDialog.on_get_bdstoken: %s, %s' % (bdstoken, error))
                self.login_failed(('Failed to get bdstoken!'))
            else:
                tokens['bdstoken'] = bdstoken
                self.update_profile(username, "", cookie, tokens, dump=True)

        if data != "":
            self.async_call(auth.get_bdstoken, on_get_bdstoken, cookie)

    def login_failed(self, error=None):
        if error:
            self.label_error.setVisible(True)
            self.label_errorinfo.setText(error)

        self.pushButton_login.setText(u'登录')
        self.pushButton_login.setDisabled(False)

    # 处理点击登录按钮
    def clicklogin(self):
        def on_get_bdstoken(bdstoken, error=None):
            if error or not bdstoken:
                logger.error('SigninDialog.on_get_bdstoken: %s, %s' % (bdstoken, error))
                self.login_failed(('Failed to get bdstoken!'))
            else:
                tokens['bdstoken'] = bdstoken
                self.update_profile(username, password, cookie, tokens, dump=True)

        def on_post_login(info, error=None):
            if error or not info:
                logger.error('SigninDialog.on_post_login: %s, %s' % (info, error))
                self.login_failed(('Login failed, please try again'))
            else:
                errno, query = info
                if errno == 0:
                    query = query.split(';')
                    cookie.load_list(query)
                    self.pushButton_login.setText('Get bdstoken...')
                    self.async_call(auth.get_bdstoken, on_get_bdstoken, cookie)
                # 257: 需要输入验证码
                elif errno == 257:
                    vcodetype = query['vcodetype']
                    codeString = query['codeString']

                    self.login_failed((u'请输入验证码'))
                    # dialog = SigninVcodeDialog(self, username, cookie,
                    #                            tokens['token'], codeString,
                    #                            vcodetype)
                    # response = dialog.run()
                    # verifycode = dialog.get_vcode()
                    # codeString = dialog.codeString
                    # dialog.destroy()
                    # if not verifycode or len(verifycode) != 4:
                    #     self.signin_failed(_('Please input verification code!'))
                    #     return
                    # else:
                    #     self.signin_button.set_label(_('Get bdstoken...'))
                    #     gutil.async_call(auth.post_login, cookie,
                    #                      tokens, username,
                    #                      password_enc, rsakey, verifycode,
                    #                      codeString, callback=on_post_login)
                # 密码错误
                elif errno == 4:
                    logger.error('SigninDialog.on_post_login: %s, %s' % (info, error))
                    self.login_failed(('Password error, please try again'))
                # 验证码错误
                elif errno == 6:
                    print 'Verfication code error'
                    self.login_failed(('Verfication code error, please try again'))
                # 需要短信验证
                elif errno == 400031:
                    logger.error('SigninDialog.on_post_login: %s, %s' % (info, error))
                    self.login_failed(('Does not support SMS/Email verification!'))
                else:
                    logger.error('SigninDialog.on_post_login: %s, %s' % (info, error))
                    self.login_failed(('Unknown error, please try again'))

        def on_get_public_key(info, error=None):
            if not info or error:
                logger.error('SigninDialog.on_get_public_key: %s, %s' % (info, error))
                self.login_failed(('Failed to request public key, please try again'))
            else:
                pubkey = info['pubkey']
                rsakey = info['key']
                password_enc = util.RSA_encrypt(pubkey, password)
                self.pushButton_login.setText("postLogin")
                self.async_call(auth.post_login, on_post_login, cookie, tokens,
                                 username, password_enc, rsakey, verifycode,
                                 codeString)

        def on_check_login(info, error=None):
            if not info or error:
                logger.error('SigninDialog.on_check_login: %s, %s' % (info, error))
                self.login_failed(('Failed to check login, please try again'))
            else:
                ubi_cookie, status = info
                ubi_cookie = ubi_cookie.split(';')
                cookie.load_list(ubi_cookie)

                codeString = status['data']['codeString']
                vcodetype = status['data']['vcodetype']
                if codeString:
                    print "need vcode..."
                    # dialog = SigninVcodeDialog(self, username, cookie,
                    #                            tokens, codeString, vcodetype)
                    # response = dialog.run()
                    # verifycode = dialog.get_vcode()
                    # codeString = dialog.codeString
                    # dialog.destroy()
                    # if not verifycode or len(verifycode) != 4:
                    #     self.signin_failed(_('Please input verification code!'))
                    #     return
                    # else:
                    #     gutil.async_call(auth.get_public_key, cookie,
                    #                      tokens, callback=on_get_public_key)
                else:
                    self.pushButton_login.setText("GetPublicKey")
                    self.async_call(auth.get_public_key, on_get_public_key, cookie, tokens)

        def on_get_UBI(ubi_cookie, error=None):
            if error or not ubi_cookie:
                logger.error('SigninDialog.on_getUBI: %s, %s' % (ubi_cookie, error))
                self.login_failed(('Failed to get UBI, please try again.'))
            else:
                ubi_cookie = ubi_cookie.split(';')
                cookie.load_list(ubi_cookie)
                self.pushButton_login.setText('Check login')
                self.async_call(auth.check_login, on_check_login, cookie, tokens, username)

        def on_get_token(info, error=None):
            if error or not info:
                logger.error('SigninDialog.on_get_token: %s, %s' % (info, error))
                self.login_failed(('Failed to get token, please try again.'))
            else:
                hosupport, token = info
                hosupport = hosupport.split(';')
                cookie.load_list(hosupport)
                cookie.load('cflag=65535%3A1; PANWEB=1;')
                tokens['token'] = token
                self.pushButton_login.setText('Get UBI...')
                self.async_call(auth.get_UBI, on_get_UBI, cookie, tokens)

        def on_get_BAIDUID(uid_cookie, error=None):
            if error or not uid_cookie:
                logger.error('SigninDialog.on_get_BAIDUID: %s, %s' % (uid_cookie, error))

                self.pushButton_login.setText(u"登录")
                self.pushButton_login.setDisabled(False)
            else:
                uid_cookie = uid_cookie.split(';')
                cookie.load_list(uid_cookie)
                self.pushButton_login.setText('Get TOKEN...')
                self.async_call(auth.get_token, on_get_token, cookie)

        username = str(self.lineEdit_user.text()).strip()
        password = str(self.lineEdit_pwd.text()).strip()
        # if len(username) < 1:
        #     self.login_failed(u"请输入帐号")
        #     self.lineEdit_user.setFocus()
        #     return
        #
        # if len(username) < 1:
        #     self.login_failed(u"请输入密码")
        #     self.lineEdit_pwd.setFocus()
        #     return

        # 使用本地的缓存token, 有效期是三天
        # if not self.password_changed and self.signin_check.get_active():
        #     cookie, tokens = self.load_auth(username)
        #     if cookie and tokens:
        #         self.update_profile(username, password, cookie, tokens)
        #         return

        cookie = RequestCookie()
        tokens = {}
        verifycode = ''
        codeString = ''
        password_enc = ''
        rsakey = ''
        self.pushButton_login.setDisabled(True)
        self.pushButton_login.setText('Get BAIDUID...')
        self.async_call(auth.get_BAIDUID, on_get_BAIDUID)

        # self.mainform = MainDlg()
        # self.mainform.showNormal()
        # self.hide()


    def update_profile(self, username, password, cookie, tokens, dump=False):
        self.mycookie = cookie
        self.mytoken = tokens
        if not self.profile:
            self.profile = gutil.load_profile(username)
        self.profile['username'] = username
        self.profile['remember-password'] = self.checkBox_rempwd.checkState()
        self.profile['auto-signin'] = self.checkBox_autologin.checkState()
        if self.profile['remember-password']:
            self.profile['password'] = password
        else:
            self.profile['password'] = ''
        gutil.dump_profile(self.profile)

        if username not in self.conf['profiles']:
            self.conf['profiles'].append(username)
        if self.profile['auto-signin']:
            self.conf['default'] = username
        Config.dump_conf(self.conf)
        #self.app.cookie = cookie
        #self.app.tokens = tokens
        # dump auth info
        if dump:
            self.dump_auth(username, cookie, tokens)

        # 显示主窗口
        self.mainform = MainDlg(cookie, tokens)
        self.mainform.showNormal()
        self.hide()

    def dump_auth(self, username, cookie, tokens):
        auth_file = os.path.join(Config.get_tmp_path(username), 'auth.json')
        with open(auth_file, 'w') as fh:
            json.dump([str(cookie), tokens], fh)