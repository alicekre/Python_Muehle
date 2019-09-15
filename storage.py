import mill
import time
import json


def convert_field_from_json(field):
    pass


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
        # open json-file


        # convert field
        self.__content["field"] = mill.Field.convert_field_from_json(self.__content["field"])

        # convert history
        converted_history = []
        for field in self.__content["history"]:
            converted_history.append(mill.Field.convert_field_from_json(field))
        self.__content["history"] = converted_history

        return self.__content

    def __convert_from_json(self):
        """


        :return:
        """
        pass


class Saver(Storage):
    """

    """

    def __init__(self, game, filename="savedGames/{}-mill.json".format(time.time)):
        """"""
        super().__init__(filename)
        if game is isinstance(mill.Game):
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
