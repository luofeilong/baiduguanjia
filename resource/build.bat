echo off

call pyuic4 ui_loginform.ui > ui_loginform.py
call pyrcc4 res_loginform.qrc > res_loginform_rc.py

copy ui_loginform.py ..\ /Y
copy res_loginform_rc.py ..\ /Y

call pyuic4 ui_mainform.ui > ui_mainform.py
call pyrcc4 res_mainform.qrc > res_mainform_rc.py

copy ui_mainform.py ..\ /Y
copy res_mainform_rc.py ..\ /Y