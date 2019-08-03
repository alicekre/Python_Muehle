from PyQt5 import Qt
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtWidgets import QLabel, QApplication


class playing_field_label(QLabel):
    def __init__(self,title):
        super().__init__(title)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()

    def dropEvent(self,event):
        if event.mimeData().hasImage():
            print("dropEvent")
            print(self.pos())
            # in Spiellogik: update_token_position()
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))

    def mousePressEvent(self, event):
        print("Pressed")
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

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
        print("Moving")
        drag.exec_(Qt.MoveAction)