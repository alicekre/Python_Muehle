from PyQt5.QtWidgets import QLabel
import playing_field_label
from token_label import token_label


class ResetToStart(token_label):
    def __init__(self, title):
        super().__init__(title)

    def distance(self, x1, y1, x2, y2):
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    def wrong_setting(self, x, y, image):
        for label in playing_field_label.field_label:
            if self.distance(label.pos().x, label.pos().y, x, y) < 30:
                label.setImage(image)


