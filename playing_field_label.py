from PyQt5 import Qt
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtWidgets import QLabel, QApplication


class playing_field_label(QLabel):
    game = None

    origin = None
    target = None

    def __init__(self, title, game):
        self.game = game
        super().__init__(title)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        print("SELF_ORIGIN drag enter %s" % playing_field_label.origin)
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            print("dropEvent")

            print("origin object %s" % playing_field_label.origin)
            if playing_field_label.origin == None:
                startPos = (0, 0, 0)
            else:
                startPos = tuple(map(int, playing_field_label.origin.split("_")[1]))

            playing_field_label.target = self.objectName()
            print("target object %s" % self.objectName())
            endpos = tuple(map(int, playing_field_label.target.split("_")[1]))

            print("Origin object: %s | as tuple: %s" % (playing_field_label.origin, startPos))
            print("Target object: %s | as tuple: %s" % (playing_field_label.target, endpos))

            # origin pos: startPos
            # target pos: endpos
            # self.game.move(startPos, endpos)

            self.disableDrops()
            # in Spiellogik: update_token_position()
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
        else:
            pass  # MyDialog.wrong_setting(event.pos().x, event.pos().y, event.mimeData().imageData())

    def mousePressEvent(self, event):
        print("\nPressed")
        playing_field_label.origin = self.objectName()
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
            print("source object: %s" % self.objectName())

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        self.clear()
        self.setText("o")
        print("Moving")
        drag.exec_(Qt.MoveAction)

    def getObjectName(self):
        return self.objectName()

    def getPosition(self):
        return self.pos()

    def disableDrops(self):
        self.setAcceptDrops(False)

    def enableDrops(self):
        self.setAcceptDrops(True)
