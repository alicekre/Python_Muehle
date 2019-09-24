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
            self.drag_start_position = event.pos()
            self.dialog.start_label=None

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
        self.image = pixmap
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        self.clear()
        print("Moving")
        drag.exec_(Qt.MoveAction)
       
       