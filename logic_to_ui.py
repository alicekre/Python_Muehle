from playing_field import MyDialog


class Field_UI():
    def __init__(self, parent=None):
        super().__init__(parent)
        self.oneNode = MyDialog.field_label.label
        self.oneTokenBlue = MyDialog.blue_token.blau
        self.oneTokenYellow = MyDialog.yellow_token.gelb

    def oneNode(self):
        pass

        # self.player_on_turn = 1
        # self.phase = [1, 1]
        # self.remis_3 = False
        # self.remis_50 = False
        # self.player1_lose_2token_left = False
        # self.player1_lose_no_moves_any_more = False
        # self.player2_lose_2token_left = False
        # self.player2_lose_no_moves_any_more = False
        # self.player1_mill_completed = False
        # self.player2_mill_completed = False

    # def oneNode(self):
    #   pass

    # def on_turn(self):
    #   player_on_turn = game.__get_opponent
    #  self.update()

    # def change_to_phase2(self, player):
    #   self.phase[player - 1] = 2
    #  self.update()

    # def change_to_phase3(self, player):
    #   self.phase[player - 1] = 3
    #  self.update()

    # def new_mill(self):
    #   pass
