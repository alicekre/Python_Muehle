# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spielfeld_OF_4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, game):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 900)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(261, 21, 702, 781))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Spielfeld_OF = QtWidgets.QFrame(self.layoutWidget)
        self.Spielfeld_OF.setMinimumSize(QtCore.QSize(700, 600))
        self.Spielfeld_OF.setMaximumSize(QtCore.QSize(800, 800))
        self.Spielfeld_OF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Spielfeld_OF.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Spielfeld_OF.setObjectName("Spielfeld_OF")
        self.line = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line.setGeometry(QtCore.QRect(160, 360, 80, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_2.setGeometry(QtCore.QRect(460, 360, 80, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_3.setGeometry(QtCore.QRect(360, 280, 80, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_5.setGeometry(QtCore.QRect(260, 280, 80, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_4.setGeometry(QtCore.QRect(250, 290, 3, 60))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_6 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_6.setGeometry(QtCore.QRect(450, 290, 3, 60))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_7.setGeometry(QtCore.QRect(250, 370, 3, 60))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_8.setGeometry(QtCore.QRect(450, 370, 3, 60))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_9.setGeometry(QtCore.QRect(260, 440, 80, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_10.setGeometry(QtCore.QRect(360, 440, 80, 3))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_11.setGeometry(QtCore.QRect(350, 450, 3, 60))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_12.setGeometry(QtCore.QRect(350, 210, 3, 60))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_13.setGeometry(QtCore.QRect(350, 130, 3, 60))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_14.setGeometry(QtCore.QRect(350, 530, 3, 60))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_15.setGeometry(QtCore.QRect(360, 200, 180, 3))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_16.setGeometry(QtCore.QRect(160, 200, 180, 3))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_17.setGeometry(QtCore.QRect(360, 120, 280, 3))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_18.setGeometry(QtCore.QRect(60, 120, 280, 3))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_19.setGeometry(QtCore.QRect(560, 360, 80, 3))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_20.setGeometry(QtCore.QRect(60, 360, 80, 3))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_21.setGeometry(QtCore.QRect(160, 520, 180, 3))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_22.setGeometry(QtCore.QRect(360, 520, 180, 3))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_23.setGeometry(QtCore.QRect(360, 600, 280, 3))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_24.setGeometry(QtCore.QRect(60, 600, 280, 3))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_25.setGeometry(QtCore.QRect(650, 130, 3, 220))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_26.setGeometry(QtCore.QRect(650, 370, 3, 220))
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_27.setGeometry(QtCore.QRect(150, 370, 3, 140))
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_28.setGeometry(QtCore.QRect(550, 370, 3, 140))
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_29.setGeometry(QtCore.QRect(550, 210, 3, 140))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_30.setGeometry(QtCore.QRect(150, 210, 3, 140))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_31.setGeometry(QtCore.QRect(50, 370, 3, 220))
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.Spielfeld_OF)
        self.line_32.setGeometry(QtCore.QRect(50, 130, 3, 220))
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.label_312 = playing_field_label(self.Spielfeld_OF, game)
        self.label_312.setGeometry(QtCore.QRect(320, 250, 70, 70))
        self.label_312.setMaximumSize(QtCore.QSize(70, 70))
        self.label_312.setAcceptDrops(True)
        self.label_312.setAlignment(QtCore.Qt.AlignCenter)
        self.label_312.setObjectName("label_312")
        self.label_323 = playing_field_label(self.Spielfeld_OF, game)
        self.label_323.setGeometry(QtCore.QRect(420, 330, 70, 70))
        self.label_323.setMaximumSize(QtCore.QSize(70, 70))
        self.label_323.setAcceptDrops(True)
        self.label_323.setAlignment(QtCore.Qt.AlignCenter)
        self.label_323.setObjectName("label_323")
        self.label_231 = playing_field_label(self.Spielfeld_OF, game)
        self.label_231.setGeometry(QtCore.QRect(120, 480, 70, 70))
        self.label_231.setMaximumSize(QtCore.QSize(70, 70))
        self.label_231.setAcceptDrops(True)
        self.label_231.setAlignment(QtCore.Qt.AlignCenter)
        self.label_231.setObjectName("label_231")
        self.label_213 = playing_field_label(self.Spielfeld_OF, game)
        self.label_213.setGeometry(QtCore.QRect(510, 170, 70, 70))
        self.label_213.setMaximumSize(QtCore.QSize(70, 70))
        self.label_213.setAcceptDrops(True)
        self.label_213.setAlignment(QtCore.Qt.AlignCenter)
        self.label_213.setObjectName("label_213")
        self.label_233 = playing_field_label(self.Spielfeld_OF, game)
        self.label_233.setGeometry(QtCore.QRect(510, 480, 70, 70))
        self.label_233.setMaximumSize(QtCore.QSize(70, 70))
        self.label_233.setAcceptDrops(True)
        self.label_233.setAlignment(QtCore.Qt.AlignCenter)
        self.label_233.setObjectName("label_233")
        self.label_211 = playing_field_label(self.Spielfeld_OF, game)
        self.label_211.setGeometry(QtCore.QRect(120, 170, 70, 70))
        self.label_211.setMaximumSize(QtCore.QSize(70, 70))
        self.label_211.setAcceptDrops(True)
        self.label_211.setAlignment(QtCore.Qt.AlignCenter)
        self.label_211.setObjectName("label_211")
        self.label_131 = playing_field_label(self.Spielfeld_OF, game)
        self.label_131.setGeometry(QtCore.QRect(20, 560, 70, 70))
        self.label_131.setMaximumSize(QtCore.QSize(70, 70))
        self.label_131.setAcceptDrops(True)
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setObjectName("label_131")
        self.label_331 = playing_field_label(self.Spielfeld_OF, game)
        self.label_331.setGeometry(QtCore.QRect(220, 400, 70, 70))
        self.label_331.setMaximumSize(QtCore.QSize(70, 70))
        self.label_331.setAcceptDrops(True)
        self.label_331.setAlignment(QtCore.Qt.AlignCenter)
        self.label_331.setObjectName("label_331")
        self.label_311 = playing_field_label(self.Spielfeld_OF, game)
        self.label_311.setGeometry(QtCore.QRect(220, 250, 70, 70))
        self.label_311.setMaximumSize(QtCore.QSize(70, 70))
        self.label_311.setAcceptDrops(True)
        self.label_311.setAlignment(QtCore.Qt.AlignCenter)
        self.label_311.setObjectName("label_311")
        self.label_232 = playing_field_label(self.Spielfeld_OF, game)
        self.label_232.setGeometry(QtCore.QRect(320, 490, 70, 70))
        self.label_232.setMaximumSize(QtCore.QSize(70, 70))
        self.label_232.setAcceptDrops(True)
        self.label_232.setAlignment(QtCore.Qt.AlignCenter)
        self.label_232.setObjectName("label_232")
        self.label_221 = playing_field_label(self.Spielfeld_OF, game)
        self.label_221.setGeometry(QtCore.QRect(120, 320, 70, 70))
        self.label_221.setMaximumSize(QtCore.QSize(70, 70))
        self.label_221.setAcceptDrops(True)
        self.label_221.setAlignment(QtCore.Qt.AlignCenter)
        self.label_221.setObjectName("label_221")
        self.label_223 = playing_field_label(self.Spielfeld_OF, game)
        self.label_223.setGeometry(QtCore.QRect(510, 320, 70, 70))
        self.label_223.setMaximumSize(QtCore.QSize(70, 70))
        self.label_223.setAcceptDrops(True)
        self.label_223.setAlignment(QtCore.Qt.AlignCenter)
        self.label_223.setObjectName("label_223")
        self.label_112 = playing_field_label(self.Spielfeld_OF, game)
        self.label_112.setGeometry(QtCore.QRect(310, 80, 70, 70))
        self.label_112.setMaximumSize(QtCore.QSize(70, 70))
        self.label_112.setAcceptDrops(True)
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.label_123 = playing_field_label(self.Spielfeld_OF, game)
        self.label_123.setGeometry(QtCore.QRect(620, 320, 70, 70))
        self.label_123.setMaximumSize(QtCore.QSize(70, 70))
        self.label_123.setAcceptDrops(True)
        self.label_123.setAlignment(QtCore.Qt.AlignCenter)
        self.label_123.setObjectName("label_123")
        self.label_133 = playing_field_label(self.Spielfeld_OF, game)
        self.label_133.setGeometry(QtCore.QRect(610, 560, 70, 70))
        self.label_133.setMaximumSize(QtCore.QSize(70, 70))
        self.label_133.setAcceptDrops(True)
        self.label_133.setAlignment(QtCore.Qt.AlignCenter)
        self.label_133.setObjectName("label_133")
        self.label_332 = playing_field_label(self.Spielfeld_OF, game)
        self.label_332.setGeometry(QtCore.QRect(320, 410, 70, 70))
        self.label_332.setMaximumSize(QtCore.QSize(70, 70))
        self.label_332.setAcceptDrops(True)
        self.label_332.setAlignment(QtCore.Qt.AlignCenter)
        self.label_332.setObjectName("label_332")
        self.label_321 = playing_field_label(self.Spielfeld_OF, game)
        self.label_321.setGeometry(QtCore.QRect(210, 330, 70, 70))
        self.label_321.setMaximumSize(QtCore.QSize(70, 70))
        self.label_321.setAcceptDrops(True)
        self.label_321.setAlignment(QtCore.Qt.AlignCenter)
        self.label_321.setObjectName("label_321")
        self.label_132 = playing_field_label(self.Spielfeld_OF, game)
        self.label_132.setGeometry(QtCore.QRect(320, 570, 70, 70))
        self.label_132.setMaximumSize(QtCore.QSize(70, 70))
        self.label_132.setAcceptDrops(True)
        self.label_132.setAlignment(QtCore.Qt.AlignCenter)
        self.label_132.setObjectName("label_132")
        self.label_313 = playing_field_label(self.Spielfeld_OF, game)
        self.label_313.setGeometry(QtCore.QRect(410, 250, 70, 70))
        self.label_313.setMaximumSize(QtCore.QSize(70, 70))
        self.label_313.setAcceptDrops(True)
        self.label_313.setAlignment(QtCore.Qt.AlignCenter)
        self.label_313.setObjectName("label_313")
        self.label_212 = playing_field_label(self.Spielfeld_OF, game)
        self.label_212.setGeometry(QtCore.QRect(320, 170, 70, 70))
        self.label_212.setMaximumSize(QtCore.QSize(70, 70))
        self.label_212.setAcceptDrops(True)
        self.label_212.setAlignment(QtCore.Qt.AlignCenter)
        self.label_212.setObjectName("label_212")
        self.label_333 = playing_field_label(self.Spielfeld_OF, game)
        self.label_333.setGeometry(QtCore.QRect(410, 400, 70, 70))
        self.label_333.setMaximumSize(QtCore.QSize(70, 70))
        self.label_333.setAcceptDrops(True)
        self.label_333.setAlignment(QtCore.Qt.AlignCenter)
        self.label_333.setObjectName("label_333")
        self.label_121 = playing_field_label(self.Spielfeld_OF, game)
        self.label_121.setGeometry(QtCore.QRect(20, 330, 70, 70))
        self.label_121.setMaximumSize(QtCore.QSize(70, 70))
        self.label_121.setAcceptDrops(True)
        self.label_121.setAlignment(QtCore.Qt.AlignCenter)
        self.label_121.setObjectName("label_121")
        self.label_111 = playing_field_label(self.Spielfeld_OF, game)
        self.label_111.setGeometry(QtCore.QRect(10, 80, 70, 70))
        self.label_111.setMaximumSize(QtCore.QSize(70, 70))
        self.label_111.setAcceptDrops(True)
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.label_113 = playing_field_label(self.Spielfeld_OF, game)
        self.label_113.setGeometry(QtCore.QRect(610, 90, 70, 70))
        self.label_113.setMaximumSize(QtCore.QSize(70, 70))
        self.label_113.setAcceptDrops(True)
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.verticalLayout.addWidget(self.Spielfeld_OF)
        self.Reset_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.Reset_pushButton.setObjectName("Reset_pushButton")
        self.verticalLayout.addWidget(self.Reset_pushButton)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(960, 20, 128, 780))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(28, 778, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.player2 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.player2.setObjectName("player2")
        self.gelb_1 = token_label(self.player2)
        self.gelb_1.setGeometry(QtCore.QRect(10, 600, 70, 70))
        self.gelb_1.setStyleSheet("")
        self.gelb_1.setText("")
        self.gelb_1.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_1.setObjectName("gelb_1")
        self.gelb_2 = token_label(self.player2)
        self.gelb_2.setGeometry(QtCore.QRect(10, 520, 70, 70))
        self.gelb_2.setStyleSheet("")
        self.gelb_2.setText("")
        self.gelb_2.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_2.setObjectName("gelb_2")
        self.gelb_3 = token_label(self.player2)
        self.gelb_3.setGeometry(QtCore.QRect(10, 450, 70, 70))
        self.gelb_3.setStyleSheet("")
        self.gelb_3.setText("")
        self.gelb_3.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_3.setObjectName("gelb_3")
        self.gelb_4 = token_label(self.player2)
        self.gelb_4.setGeometry(QtCore.QRect(10, 380, 70, 70))
        self.gelb_4.setStyleSheet("")
        self.gelb_4.setText("")
        self.gelb_4.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_4.setObjectName("gelb_4")
        self.gelb_5 = token_label(self.player2)
        self.gelb_5.setGeometry(QtCore.QRect(10, 310, 70, 70))
        self.gelb_5.setStyleSheet("")
        self.gelb_5.setText("")
        self.gelb_5.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_5.setObjectName("gelb_5")
        self.gelb_6 = token_label(self.player2)
        self.gelb_6.setGeometry(QtCore.QRect(10, 240, 70, 70))
        self.gelb_6.setStyleSheet("")
        self.gelb_6.setText("")
        self.gelb_6.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_6.setObjectName("gelb_6")
        self.gelb_7 = token_label(self.player2)
        self.gelb_7.setGeometry(QtCore.QRect(10, 170, 70, 70))
        self.gelb_7.setStyleSheet("")
        self.gelb_7.setText("")
        self.gelb_7.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_7.setObjectName("gelb_7")
        self.gelb_8 = token_label(self.player2)
        self.gelb_8.setGeometry(QtCore.QRect(10, 100, 70, 70))
        self.gelb_8.setStyleSheet("")
        self.gelb_8.setText("")
        self.gelb_8.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_8.setObjectName("gelb_8")
        self.gelb_9 = token_label(self.player2)
        self.gelb_9.setGeometry(QtCore.QRect(10, 30, 70, 70))
        self.gelb_9.setStyleSheet("")
        self.gelb_9.setText("")
        self.gelb_9.setPixmap(QtGui.QPixmap("gelb.png"))
        self.gelb_9.setObjectName("gelb_9")
        self.Sp2_phase = phase(self.player2)
        self.Sp2_phase.setGeometry(QtCore.QRect(10, 730, 57, 15))
        self.Sp2_phase.setStyleSheet("color: rgb(0, 0, 0);")
        self.Sp2_phase.setObjectName("Sp2_phase")
        self.horizontalLayout_2.addWidget(self.player2)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 20, 113, 780))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.player1 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.player1.setStyleSheet("color: rgb(204, 0, 0);")
        self.player1.setObjectName("player1")
        self.blau_1 = token_label(self.player1)
        self.blau_1.setGeometry(QtCore.QRect(10, 640, 65, 65))
        self.blau_1.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_1.setAcceptDrops(True)
        self.blau_1.setAutoFillBackground(True)
        self.blau_1.setStyleSheet("")
        self.blau_1.setText("")
        self.blau_1.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_1.setWordWrap(False)
        self.blau_1.setObjectName("blau_1")
        self.blau_2 = token_label(self.player1)
        self.blau_2.setGeometry(QtCore.QRect(10, 560, 65, 65))
        self.blau_2.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_2.setAcceptDrops(True)
        self.blau_2.setAutoFillBackground(True)
        self.blau_2.setStyleSheet("")
        self.blau_2.setText("")
        self.blau_2.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_2.setWordWrap(False)
        self.blau_2.setObjectName("blau_2")
        self.blau_3 = token_label(self.player1)
        self.blau_3.setGeometry(QtCore.QRect(10, 480, 65, 65))
        self.blau_3.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_3.setAcceptDrops(True)
        self.blau_3.setAutoFillBackground(True)
        self.blau_3.setStyleSheet("")
        self.blau_3.setText("")
        self.blau_3.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_3.setWordWrap(False)
        self.blau_3.setObjectName("blau_3")
        self.blau_4 = token_label(self.player1)
        self.blau_4.setGeometry(QtCore.QRect(10, 400, 65, 65))
        self.blau_4.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_4.setAcceptDrops(True)
        self.blau_4.setAutoFillBackground(True)
        self.blau_4.setStyleSheet("")
        self.blau_4.setText("")
        self.blau_4.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_4.setWordWrap(False)
        self.blau_4.setObjectName("blau_4")
        self.blau_5 = token_label(self.player1)
        self.blau_5.setGeometry(QtCore.QRect(10, 320, 65, 65))
        self.blau_5.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_5.setAcceptDrops(True)
        self.blau_5.setAutoFillBackground(True)
        self.blau_5.setStyleSheet("")
        self.blau_5.setText("")
        self.blau_5.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_5.setWordWrap(False)
        self.blau_5.setObjectName("blau_5")
        self.blau_6 = token_label(self.player1)
        self.blau_6.setGeometry(QtCore.QRect(10, 250, 65, 65))
        self.blau_6.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_6.setAcceptDrops(True)
        self.blau_6.setAutoFillBackground(True)
        self.blau_6.setStyleSheet("")
        self.blau_6.setText("")
        self.blau_6.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_6.setWordWrap(False)
        self.blau_6.setObjectName("blau_6")
        self.blau_7 = token_label(self.player1)
        self.blau_7.setGeometry(QtCore.QRect(10, 180, 65, 65))
        self.blau_7.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_7.setAcceptDrops(True)
        self.blau_7.setAutoFillBackground(True)
        self.blau_7.setStyleSheet("")
        self.blau_7.setText("")
        self.blau_7.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_7.setWordWrap(False)
        self.blau_7.setObjectName("blau_7")
        self.blau_8 = token_label(self.player1)
        self.blau_8.setGeometry(QtCore.QRect(10, 110, 65, 65))
        self.blau_8.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_8.setAcceptDrops(True)
        self.blau_8.setAutoFillBackground(True)
        self.blau_8.setStyleSheet("")
        self.blau_8.setText("")
        self.blau_8.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_8.setWordWrap(False)
        self.blau_8.setObjectName("blau_8")
        self.blau_9 = token_label(self.player1)
        self.blau_9.setGeometry(QtCore.QRect(10, 40, 65, 65))
        self.blau_9.setMaximumSize(QtCore.QSize(100, 100))
        self.blau_9.setAcceptDrops(True)
        self.blau_9.setAutoFillBackground(True)
        self.blau_9.setStyleSheet("")
        self.blau_9.setText("")
        self.blau_9.setPixmap(QtGui.QPixmap("blau.png"))
        self.blau_9.setWordWrap(False)
        self.blau_9.setObjectName("blau_9")
        self.Sp1_phase = phase(self.player1)
        self.Sp1_phase.setGeometry(QtCore.QRect(10, 730, 57, 15))
        self.Sp1_phase.setStyleSheet("color: rgb(0, 0, 0);")
        self.Sp1_phase.setObjectName("Sp1_phase")
        self.horizontalLayout.addWidget(self.player1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 778, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        self.Reset_pushButton.clicked.connect(Dialog.resetMill)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_312.setText(_translate("Dialog", "o"))
        self.label_323.setText(_translate("Dialog", "o"))
        self.label_231.setText(_translate("Dialog", "o"))
        self.label_213.setText(_translate("Dialog", "o"))
        self.label_233.setText(_translate("Dialog", "o"))
        self.label_211.setText(_translate("Dialog", "o"))
        self.label_131.setText(_translate("Dialog", "o"))
        self.label_331.setText(_translate("Dialog", "o"))
        self.label_311.setText(_translate("Dialog", "o"))
        self.label_232.setText(_translate("Dialog", "o"))
        self.label_221.setText(_translate("Dialog", "o"))
        self.label_223.setText(_translate("Dialog", "o"))
        self.label_112.setText(_translate("Dialog", "o"))
        self.label_123.setText(_translate("Dialog", "o"))
        self.label_133.setText(_translate("Dialog", "o"))
        self.label_332.setText(_translate("Dialog", "o"))
        self.label_321.setText(_translate("Dialog", "o"))
        self.label_132.setText(_translate("Dialog", "o"))
        self.label_313.setText(_translate("Dialog", "o"))
        self.label_212.setText(_translate("Dialog", "o"))
        self.label_333.setText(_translate("Dialog", "o"))
        self.label_121.setText(_translate("Dialog", "o"))
        self.label_111.setText(_translate("Dialog", "o"))
        self.label_113.setText(_translate("Dialog", "o"))
        self.Reset_pushButton.setText(_translate("Dialog", "Reset"))
        self.player2.setTitle(_translate("Dialog", "Spieler_2"))
        self.gelb_1.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_3.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_4.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_5.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_6.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_7.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_8.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.gelb_9.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.Sp2_phase.setText(_translate("Dialog", "Phase1"))
        self.player1.setTitle(_translate("Dialog", "Spieler_1"))
        self.blau_1.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_3.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_4.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_5.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_6.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_7.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_8.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.blau_9.setToolTip(_translate("Dialog", "<html><head/><body><p>Spielstein laesst sich auf die Punkte des Muehlespielfeldes setzen</p></body></html>"))
        self.Sp1_phase.setText(_translate("Dialog", "Phase1"))

from phase import phase
from playing_field_label import playing_field_label
from token_label import token_label
