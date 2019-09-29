from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtWidgets import QLabel, QApplication


class token_label(QLabel):
    def __init__(self, parent):
        super(QLabel, self).__init__(parent)
        self.show()
        
    def saveDialog(self, dialog):
        self.dialog = dialog

    def mousePressEvent(self, event):
        print("Pressed")
        if event.button() == Qt.LeftButton:
            for name in range(1, 10):
                if self == getattr(self.dialog, "blau_{}".format(name)):
                    self.dialog.start_label = "001"

            for name in range(1, 10):
                if self == getattr(self.dialog, "gelb_{}".format(name)):
                    self.dialog.start_label = "002"
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.dialog.removable:
            return

        if not (event.buttons() & Qt.LeftButton):
            return

        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())

        if self.pixmap() is None:
            return

        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        self.image = pixmap
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        print("Moving")
        drag.exec_(Qt.MoveAction)
       
       