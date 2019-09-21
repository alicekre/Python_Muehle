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



Ui_MainWindow, WindowBaseClass = uic.loadUiType("Spielfeld_OF_4.ui")
#from mill import Game

class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.resize(1200, 900)
        self.update()
        self.start_label=None
        self.end_label=None
#        self.initMe()
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
      
        
        self.blue_token = [self.blau_1, self.blau_2, self.blau_3, self.blau_4, self.blau_5, self.blau_6, self.blau_7, self.blau_8, self.blau_9]
        self.yellow_token = [self.gelb_1, self.gelb_2, self.gelb_3, self.gelb_4, self.gelb_5, self.gelb_6, self.gelb_7, self.gelb_8, self.gelb_9]
        for label in (self.blue_token):
            label.saveDialog(self)
        for label in (self.yellow_token):
            label.saveDialog(self)
        self.game=Game()
        self.window1=Window()
        self.window2=Window()
        self.window3=Window()
        self.window4=Window()
        self.removable=False
        
    def turn(self):
        #self.Sp2_phase.setStyleSheet('QGroupBox {color: red; }')
        print(self.start_label, self.end_label)
        
        if self.start_label!=None:
            start_pos =(int(self.start_label[0]),int(self.start_label[1]),
                    int(self.start_label[2]))
        else:
            start_pos=None
        print(start_pos)
        end_pos = (int(self.end_label[0]),int(self.end_label[1]),
                    int(self.end_label[2])) 
        try:
            self.game.move(start_pos, end_pos)
            if self.game.check_on_mill(end_pos):
                self.window1.initUI("Du darfst einen Spielstein des Gegners entfernen"
                              , "Mühle")
                print("{} is in a mill.".format(end_pos))
                self.removable=True
              
        except ValueError:
            print("Invalid node. Try again: ")
        except MoveException:
            print("Invalid move. Try again: ")
            self.window3.initUI("Zug nicht erlaubt. \n Probier's nochmal!" 
                              , "Unerlaubter Zug")
            
            if self.game.get_turn()==1:
                getattr(self, "label_{}".format(self.start_label)).setPixmap(QtGui.QPixmap("blau.png"))
            if self.game.get_turn()==2:
                getattr(self, "label_{}".format(self.start_label)).setPixmap(QtGui.QPixmap("gelb.png"))
            getattr(self, "label_{}".format(self.end_label)).clear()
            self.label_121.clear()
                                    
        except WinException as e:
            print("Player {} wins, player {} looses".format(e.number_winner, e.number_looser))
            self.won_ui(e.number_winner, e.number_looser,1)
            

# TODO print reason for remis
        except RemisException as e:
            print("Remis! Nobody wins.")
            self.remis_ui(e.reason)
            

        except KeyboardInterrupt:
            print("Quit? (y/n):", end="")
            if input() == "y":
                quit()
                
        self.Sp1_phase.setText("Phase{}".format(self.game.get_phase_player_1()))
        self.Sp2_phase.setText("Phase{}".format(self.game.get_phase_player_1()))  
        print(self.game.get_phase_player_1())
        if self.game.get_turn()==1:
            self.player1.setStyleSheet('QGroupBox {color: red; }')
            self.player2.setStyleSheet('QGroupBox {color: black; }')
        if self.game.get_turn()==2:
            self.player1.setStyleSheet('QGroupBox {color: black; }')
            self.player2.setStyleSheet('QGroupBox {color: red; }')
            

            
    def remove(self):     
        try:
            self.game.remove_chip((int(self.start_label[0]),int(self.start_label[1]),
                    int(self.start_label[2])))
            self.removable=False
            getattr(self, "label_{}".format(self.start_label)).clear()
        except MoveException:
            print("Choose valid chip to remove.")
            self.window2.initUI("Du darfst diesen Stein nicht entfernen." +"\n" +
                                "Wähle einen anderen."
                              , "Falscher Stein entfernt")
            
        if self.game.get_turn()==1:
            self.player1.setStyleSheet('QGroupBox {color: red; }')
            self.player2.setStyleSheet('QGroupBox {color: black; }')
        if self.game.get_turn()==2:
            self.player1.setStyleSheet('QGroupBox {color: black; }')
            self.player2.setStyleSheet('QGroupBox {color: red; }')
        
        
            
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
        self.Sp1_phase.setText("Phase1")
        self.Sp2_phase.setText("Phase1")
        print("Ausgangszustand")
    
    def phase_2_ui(self,player):
        self.window.initUI("Remis: "
                           , "Remis")
    def phase_3_ui(self,player):
        pass
    def won_ui(self, winner, looser, reason):
        if reason == 1:
            reason_text="Spieler {} hat keine Spielsteine mehr.".format(looser)
        if reason == 2:
            reason_text="Spieler {} kann sich nicht mehr bewegen.".format(looser)
        self.window4.initUI("Spieler {} hat gewonnen. ".format(winner)+ reason_text
                           , "Won")
    def remis_ui(self,reason):
        if reason==1:
            self.window3.initUI("Remis: Es gab in 50 aufeinanderfolgenden Züge keine Mühle "
                           , "Remis")
        if reason==2:
            self.window3.initUI("Remis: Es wurde drei mal die selbe Stellung erreicht"
                           , "Remis")
            
        
    def message(self, message_):
        print(message_)

#    def initMe(self):
#        edit = token_label("Hello")  # QLabel("gelb_1", self)
#        playing_field_corner = playing_field_label("Hello")
        
#    def end_phase_1(self):
#        print("hi")
#        if self.blau_1.hasImage()==False:
#            print("end of phase1")
    

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
