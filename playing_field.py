#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:38:20 2019

@author: ask
"""
import sys

from PyQt5 import QtCore, QtWidgets, uic

from PyQt5.QtGui import QPixmap

from playing_field_label import playing_field_label
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
        self.field_label = {self.label_111: self.label_111.pos(),
                            self.label_112: self.label_112.pos(),
                            self.label_113: self.label_113.pos(),
                            self.label_121: self.label_121.pos(),
                            self.label_123: self.label_123.pos(),
                            self.label_131: self.label_131.pos(),
                            self.label_132: self.label_132.pos(),
                            self.label_133: self.label_133.pos(),
                            self.label_211: self.label_211.pos(),
                            self.label_212: self.label_212.pos(),
                            self.label_213: self.label_213.pos(),
                            self.label_221: self.label_221.pos(),
                            self.label_223: self.label_223.pos(),
                            self.label_231: self.label_231.pos(),
                            self.label_232: self.label_232.pos(),
                            self.label_312: self.label_312.pos(),
                            self.label_233: self.label_233.pos(),
                            self.label_311: self.label_311.pos(),
                            self.label_313: self.label_313.pos(),
                            self.label_321: self.label_321.pos(),
                            self.label_323: self.label_323.pos(),
                            self.label_331: self.label_331.pos(),
                            self.label_332: self.label_332.pos(),
                            self.label_333: self.label_333.pos()}
        self.blue_token = [self.blau_1, self.blau_2, self.blau_3, self.blau_4, self.blau_5, self.blau_6, self.blau_7, self.blau_8, self.blau_9]
        self.yellow_token = [self.gelb_1, self.gelb_2, self.gelb_3, self.gelb_4, self.gelb_5, self.gelb_6, self.gelb_7, self.gelb_8, self.gelb_9]

    def resetMill(self, image):
        #Ui_MainWindow, WindowBaseClass = uic.loadUiType("Spielfeld_OF_4.ui")
        for label in self.field_label:
            label.clear()
            label.setText("o")
        for label in self.blue_token:
            label.setPixmap(QPixmap("blau.png"))
        for label in self.yellow_token:
            label.setPixmap(QPixmap("gelb.png"))

        self.player1.setStyleSheet('QGroupBox {color: red; }')
        self.player2.setStyleSheet('QGroupBox {color: black; }')

        print("Ausgangszustand")

    def initMe(self):
        edit = token_label("Hello")  # QLabel("gelb_1", self)
        playing_field_corner = playing_field_label("Hello")

    # def removeToken(self, label):
    #   label.clear()
    #  label.setText("o")
    # self.label_111.remove('gelb.svg')


#
# def game_logic(self):
#    # Zugriff von hier auf die Spiellogik
#   pass
# def valid_game_turn(self):
# Ueberpruefung mit if Abfrage, ob ein Spielzug valide ist

def initUI():
    # In Spyder kann nur eine Qt-Applikation laufen und sie werden nicht anschliessend geloescht
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet("MyLabel { border-radius: 10px; min-height: 20px; min-width: 20px}")
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    initUI()
