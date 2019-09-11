# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:44:56 2019

@author: Kira
"""
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
 
class App(QWidget):
    def __init__(self):  
        super().__init__()
        self.title = 'End'
        self.left = 800
        self.top = 400
        self.width = 320
        self.height = 200
        
        
         
           
    def initUI(self, text, title):
        label_new_window=QtWidgets.QLabel(self)
        label_new_window.setText(self.text)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
                
        self.show()
    


