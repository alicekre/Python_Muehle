#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:38:20 2019

@author: ask
"""
import sys

from PyQt5 import QtCore, QtWidgets, uic, QtGui

from PyQt5.QtGui import QPixmap


from mill import *
from open_window import Window
import storage

# create logger
logger = logging.getLogger('application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages and another which logs even info messages
fh_1 = logging.FileHandler('debug.log')
fh_2 = logging.FileHandler('info.log')
fh_1.setLevel(logging.DEBUG)
fh_2.setLevel(logging.INFO)
# create formatters and add it to the handlers
formatter_1 = logging.Formatter('%(asctime)s - %(name)30s : %(funcName)30s, ln %(lineno)4s - %(levelname)8s - '
                                '%(message)s')
formatter_2 = logging.Formatter('%(asctime)s - %(name)30s : %(levelname)8s - %(message)s')
fh_1.setFormatter(formatter_1)
fh_2.setFormatter(formatter_2)

# add the handlers to the logger
logger.addHandler(fh_1)
logger.addHandler(fh_2)

Ui_MainWindow, WindowBaseClass = uic.loadUiType("Spielfeld_OF_4.ui")


class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.resize(1200, 900)
        self.update()
        self.start_label = None
        self.end_label = None

        self.field_names = ["111", "112", "113", "121", "123", "131", "132", 
                            "133", "211", "212", "213", "221", "223", "231",
                            "232", "233", "312", "311", "313", "321", "323",
                            "331", "332", "333"]
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

        for label in self.field_label:
            label.saveDialog(self)

        self.blue_token = [self.blau_1, self.blau_2, self.blau_3, self.blau_4, self.blau_5, self.blau_6, self.blau_7,
                           self.blau_8, self.blau_9]
        self.yellow_token = [self.gelb_1, self.gelb_2, self.gelb_3, self.gelb_4, self.gelb_5, self.gelb_6, self.gelb_7,
                             self.gelb_8, self.gelb_9]

        for label in self. blue_token:
            label.saveDialog(self)

        for label in self. yellow_token:
            label.saveDialog(self)

        self.game = Game()
        self.window1 = Window()
        self.window2 = Window()
        self.window3 = Window()
        self.window4 = Window()
        self.removable = False

    def turn(self):
        print(self.start_label, self.end_label)

        start_pos = (int(self.start_label[0]), int(self.start_label[1]), int(self.start_label[2]))
        print(start_pos)
        end_pos = (int(self.end_label[0]), int(self.end_label[1]), int(self.end_label[2]))

        try:
            self.game.move(start_pos, end_pos)
            if self.game.check_on_mill(end_pos):
                self.window1.initUI("Du darfst einen Spielstein des Gegners entfernen", "Mühle")
                print("{} is in a mill.".format(end_pos))
                self.removable = True
                self.update_field()
            
        except ValueError:
            print("Invalid node. Try again: ")

        except MoveException:
            self.window3.initUI("Zug nicht erlaubt. \n Probier's nochmal!", "Unerlaubter Zug")

        except MillException:
            self.update_field()   

        except WinException as e:
            print("Player {} wins, player {} looses".format(e.number_winner, e.number_looser))
            self.won_ui(e.number_winner, e.number_looser, e.reason)

        except RemisException as e:
            print("Remis! Nobody wins.")
            self.remis_ui(e.reason)

        finally:
            self.update_field()

    def update_field(self):
        self.Sp1_phase.setText("Phase{}".format(self.game.get_player_1().phase))
        self.Sp2_phase.setText("Phase{}".format(self.game.get_player_2().phase))
        print(self.game.get_player_1().phase)
        print(self.game.get_player_2().phase)

        if self.game.get_turn() == 1:
            self.player1.setStyleSheet('QGroupBox {color: red; }')
            self.player2.setStyleSheet('QGroupBox {color: black; }')

        if self.game.get_turn() == 2:
            self.player1.setStyleSheet('QGroupBox {color: black; }')
            self.player2.setStyleSheet('QGroupBox {color: red; }')
            
        current_field = self.game.get_field()

        for label in self.field_names:
            label_tuple = (int(label[0]), int(label[1]), int(label[2]))

            if current_field[label_tuple] == 0:
                getattr(self, "label_{}".format(label)).clear()
            elif current_field[label_tuple] == 1:
                getattr(self, "label_{}".format(label)).setPixmap(QtGui.QPixmap("blau.png"))
            elif current_field[label_tuple] == 2:
                getattr(self, "label_{}".format(label)).setPixmap(QtGui.QPixmap("gelb.png"))
                print(label)
                
        chips_left_player_1 = self.game.get_player_1().get_number_chips()
        for i in range(1, chips_left_player_1 + 1):
            getattr(self, "blau_{}".format(i)).setPixmap(QtGui.QPixmap("blau.png"))

        for i in range(chips_left_player_1 + 1, 10):
            getattr(self, "blau_{}".format(i)).clear()

        chips_left_player_2 = self.game.get_player_2().get_number_chips()

        for i in range(1, chips_left_player_2 + 1):
            getattr(self, "gelb_{}".format(i)).setPixmap(QtGui.QPixmap("gelb.png"))

        for i in range(chips_left_player_2 + 1, 10):
            getattr(self, "gelb_{}".format(i)).clear()
            
    def remove(self):     
        try:
            self.game.remove_chip((int(self.start_label[0]), int(self.start_label[1]), int(self.start_label[2])))
            self.removable = False
            getattr(self, "label_{}".format(self.start_label)).clear()

        except MoveException:
            print("Choose valid chip to remove.")
            self.window2.initUI("Du darfst diesen Stein nicht entfernen." + "\n" +
                                "Wähle einen anderen.", "Falscher Stein entfernt")

        except WinException as e:
            print("Player {} wins, player {} looses".format(e.number_winner, e.number_looser))
            self.won_ui(e.number_winner, e.number_looser, e.reason)

        except RemisException as e:
            print("Remis! Nobody wins.")
            self.remis_ui(e.reason)

        finally:
            self.update_field()

#        self.Sp1_phase.setText("Phase{}".format(self.game.get_player_1().phase))
#        self.Sp2_phase.setText("Phase{}".format(self.game.get_player_1().phase))
#
#        if self.game.get_turn() == 1:
#            self.player1.setStyleSheet('QGroupBox {color: red; }')
#            self.player2.setStyleSheet('QGroupBox {color: black; }')
#
#        if self.game.get_turn() == 2:
#            self.player1.setStyleSheet('QGroupBox {color: black; }')
#            self.player2.setStyleSheet('QGroupBox {color: red; }')

    def resetMill(self):
        self.blue_token = [self.blau_1, self.blau_2, self.blau_3, self.blau_4, self.blau_5, self.blau_6, self.blau_7,
                           self.blau_8, self.blau_9]

        self.yellow_token = [self.gelb_1, self.gelb_2, self.gelb_3, self.gelb_4, self.gelb_5, self.gelb_6, self.gelb_7,
                             self.gelb_8, self.gelb_9]

        for label in self.blue_token:
            label.saveDialog(self)

        for label in self.yellow_token:
            label.saveDialog(self)

        for label in self.field_label:
            label.clear()

        for label in self.blue_token:
            label.setPixmap(QPixmap("blau.png"))

        for label in self.yellow_token:
            label.setPixmap(QPixmap("gelb.png"))

        self.player1.setStyleSheet('QGroupBox {color: red; }')
        self.player2.setStyleSheet('QGroupBox {color: black; }')
        self.Sp1_phase.setText("Phase1")
        self.Sp2_phase.setText("Phase1")

        empty_field = {
                        (1, 1, 1): 0,
                        (1, 1, 2): 0,
                        (1, 1, 3): 0,
                        (1, 2, 1): 0,
                        (1, 2, 3): 0,
                        (1, 3, 1): 0,
                        (1, 3, 2): 0,
                        (1, 3, 3): 0,
                        (2, 1, 1): 0,
                        (2, 1, 2): 0,
                        (2, 1, 3): 0,
                        (2, 2, 1): 0,
                        (2, 2, 3): 0,
                        (2, 3, 1): 0,
                        (2, 3, 2): 0,
                        (2, 3, 3): 0,
                        (3, 1, 1): 0,
                        (3, 1, 2): 0,
                        (3, 1, 3): 0,
                        (3, 2, 1): 0,
                        (3, 2, 3): 0,
                        (3, 3, 1): 0,
                        (3, 3, 2): 0,
                        (3, 3, 3): 0
                        }
        player_1 = Player(1)
        player_2 = Player(2)
        turn = player_1
        history = History()
        mill = False

        self.game = Game(field=Field(empty_field), player_1=player_1, player_2=player_2, turn=turn, history=history,
                         mill=mill)
        print("Ausgangszustand")

        self.removable = False
        self.update_field()

    def won_ui(self, winner, looser, reason):
        if reason == 1:
            reason_text = "Spieler {} hat nur zwei Spielsteine übrig.".format(looser)

        if reason == 2:
            reason_text = "Spieler {} kann sich nicht mehr bewegen.".format(looser)

        self.window4.initUI("Spieler {} hat gewonnen. ".format(winner) + reason_text, "Won")
        self.resetMill()

    def remis_ui(self, reason):
        if reason == 1:
            self.window3.initUI("Remis: Es gab in 50 aufeinanderfolgenden Züge keine Mühle ", "Remis")

        if reason == 2:
            self.window3.initUI("Remis: Es wurde drei mal die selbe Stellung erreicht", "Remis")

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
