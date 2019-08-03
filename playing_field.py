#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:38:20 2019

@author: ask
"""
import sys

from PyQt5 import QtCore, QtWidgets, uic

# import get_position
from playing_field_label import playing_field_label
from positions import Positions
from token_label import token_label

Ui_MainWindow, WindowBaseClass = uic.loadUiType("Spielfeld_OF_4.ui")


class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.resize(1200, 900)
        self.update()
        self.initMe()

    #        self.token_label().setImage('blau.svg')
    # self.label_111.setImage('gelb.svg')

    def initMe(self):
        edit = token_label("Hello")  # QLabel("gelb_1", self)
        playing_field_corner = playing_field_label("Hello")

        edit.move(100, 100)
        btn = Positions("0")
    # def removeToken(self, label):
    #   label.clear()
    #  label.setText("o")
    # self.label_111.remove('gelb.svg')


if __name__ == "__main__":

    # In Spyder kann nur eine Qt-Applikation laufen und sie werden nicht anschliessend geloescht
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    # app.setStyleSheet("MyLabel { border-radius: 10px; min-height: 20px; min-width: 20px}")
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
