# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmacao.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setConfirmacao(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 200)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.frame.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 380, 180))
        self.frame_2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame_2)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 360, 30))
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lb_titulo_modal = QtGui.QLabel(self.frame_2)
        self.lb_titulo_modal.setGeometry(QtCore.QRect(90, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lb_titulo_modal.setFont(font)
        self.lb_titulo_modal.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_titulo_modal.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_titulo_modal.setObjectName(_fromUtf8("lb_titulo_modal"))
        self.lb_info = QtGui.QLabel(self.frame_2)
        self.lb_info.setGeometry(QtCore.QRect(20, 70, 90, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info.setText(_fromUtf8(""))
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setObjectName(_fromUtf8("lb_info"))
        self.lb_descricao = QtGui.QLabel(self.frame_2)
        self.lb_descricao.setGeometry(QtCore.QRect(120, 70, 240, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_descricao.setFont(font)
        self.lb_descricao.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_descricao.setText(_fromUtf8(""))
        self.lb_descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_descricao.setObjectName(_fromUtf8("lb_descricao"))

        self.tradConfirm(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def tradConfirm(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Confirma????o", None))
        self.lb_titulo_modal.setText(_translate("Dialog", "Confirmar Cadastro:", None))

