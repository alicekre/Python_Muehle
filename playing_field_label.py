
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtWidgets import QLabel, QApplication


class playing_field_label(QLabel):
    def __init__(self, title):
        super().__init__(title)
        self.setAcceptDrops(True)

    def saveDialog(self, dialog):
        self.dialog = dialog

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            print("dropEvent")

            for name in self.dialog.field_names:
                if self == getattr(self.dialog, "label_{}".format(name)):
                    self.dialog.end_label = name

            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
            self.dialog.turn()

    def mousePressEvent(self, event):
        print("Pressed")
        print("plaing field label")
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

            for name in self.dialog.field_names:
                if self == getattr(self.dialog, "label_{}".format(name)):
                    self.dialog.start_label = name

            if self.dialog.removable:
                self.dialog.remove()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return

        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        if self.dialog.removable:
            return

        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())

        if self.pixmap() is None:
            return

        mimedata.setImageData(self.pixmap().toImage())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())       
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        
        print("Moving")
        drag.exec_(Qt.MoveAction)
