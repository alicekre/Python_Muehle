#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:19:53 2019

@author: ask
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic 

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage
from PyQt5.QtCore import QMimeData, Qt


class Positions(QPushButton):
    def __init__(self, title):
        super().__init__(title)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('image/*'):
            e.accept()
            print("event accepted")
        else:
            e.ignore()
            
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        