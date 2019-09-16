import mill
import time
import json


# TODO add logging
class Storage:
    """

    """

    def __init__(self, filename):
        self.filename = filename


class Loader(Storage):
    """

    """
    def __init__(self, filename):
        super().__init__(filename)

        with open(self.filename, 'r') as f:
            self.__content = json.load(f)

    def reload_file(self):
        """reloads the content of the file"""
        with open(self.filename, 'r') as f:
            self.__content = json.load(f)

    def load_game(self):
        """


        :return:
        """
        player_1 = self.__build_player(1)
        player_2 = self.__build_player(2)
        field = mill.Field(self.__content["field"])

        if self.__content["turn"] == 1:
            turn = player_1
        elif self.__content["turn"] == 2:
            turn = player_2
        else:
            raise ValueError

        history = self.__build_history()
        mill_bool = self.__content["mill"]

        return mill.Game(player_1, player_2, field, turn, history, mill_bool)

    def __build_player(self, number):
        """"""
        if number == 1:
            number_chips = self.__content["player_1"]["number_chips"]
            phase = self.__content["player_1"]["phase"]
            player = mill.Player(number, number_chips, phase)
        elif number == 2:
            number_chips = self.__content["player_2"]["number_chips"]
            phase = self.__content["player_2"]["phase"]
            player = mill.Player(number, number_chips, phase)
        else:
            raise ValueError

        return player

    def __build_history(self):
        move_counter = self.__content["move_counter"]

        history = self.__content["history"]
        fields = []
        for field in history:
            field_instance = mill.Field(field)
            fields.append(field_instance)

        return mill.History(fields, move_counter)

    def __convert_from_json(self):
        """


        :return:
        """
        # convert field
        self.__content["field"] = mill.Field.convert_field_from_json(self.__content["field"])

        # convert history
        converted_history = []
        for field in self.__content["history"]:
            converted_history.append(mill.Field.convert_field_from_json(field))

        self.__content["history"] = converted_history

    # DEBUG
    def print_content(self):
        print(self.__content)


class Saver(Storage):
    """

    """

    def __init__(self, game, filename="savedGames/{}-mill.json".format(time.time)):
        """"""
        super().__init__(filename)
        if isinstance(game, mill.Game):
            self.game = game
        else:
            raise TypeError

    def save(self):
        """


        :return:
        """
        data = self.__convert_into_json()
        # write data into json-file
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def __convert_into_json(self):
        """


        :return:
        """

        # convert field in history into json compatible structure, make keys to strings
        converted_history = []
        for field in self.game.get_history().get_fields():
            converted_field = field.get_converted_json()
            converted_history.append(converted_field)

        player_1 = {
            "number_chips": self.game.get_player_1().get_number_chips(),
            "phase": self.game.get_player_1().phase
        }

        player_2 = {
            "number_chips": self.game.get_player_2().get_number_chips(),
            "phase": self.game.get_player_2().phase
        }

        data = {
            "field": self.game.get_field_instance().get_converted_json(),
            "turn": self.game.get_turn(),
            "move_counter": self.game.get_history().get_move_counter(),
            "history": converted_history,
            "player_1": player_1,
            "player_2": player_2,
            "mill": self.game.get_mill()
        }

        return data
