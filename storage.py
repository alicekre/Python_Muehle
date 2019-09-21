#
# @author Christian Birker
#
# storage module for the board game mill
# saves and loads games
#

import mill
import time
import json
import logging

# create logger for module
module_log = logging.getLogger('application.storage')


class Storage:
    """
    The Storage class

    Attributes:
        filename (str): the path to the file
    """

    def __init__(self, filename):
        """the constructor for Storage class"""
        self.logger = logging.getLogger('application.storage.Storage')
        self.filename = filename


class Loader(Storage):
    """
    The Loader class represents loading a game from a file

    Attributes:
        __content (dict): the converted file content
    """
    def __init__(self, filename):
        """the constructor for Loader class"""
        super().__init__(filename)

        with open(self.filename, 'r') as f:
            self.__content = json.load(f)

        self.__convert_from_json()
        self.logger.debug("created Loader instance")

    def reload_file(self):
        """reloads the content from the file"""
        with open(self.filename, 'r') as f:
            self.__content = json.load(f)

        self.__convert_from_json()
        self.logger.debug("{} reloaded".format(self.filename))

    def load_game(self):
        """
        builds and returns a Game instance of the file content

        :return: the initialized game as instance of Game class
        :rtype: Game
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

        self.logger.debug("create Game instance from file {}".format(self.filename))
        return mill.Game(player_1, player_2, field, turn, history, mill_bool)

    def __build_player(self, number):
        """
        builds a Player instance of file content

        :param number: the number of the player (1, 2)
        :return: player as instance of Player
        :rtype: Player
        :raise: ValueError if number is not 1 or 2
        """
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
        """
        builds and returns a History instance from the content of the file

        :return: the stored history as History instance
        :rtype: History
        """
        move_counter = self.__content["move_counter"]

        history = self.__content["history"]
        fields = []
        for field in history:
            field_instance = mill.Field(field)
            fields.append(field_instance)

        return mill.History(fields, move_counter)

    def __convert_from_json(self):
        """converts the content from file into dct"""
        # convert field
        self.__content["field"] = mill.Field.convert_field_from_json(self.__content["field"])

        # convert history
        converted_history = []
        for field in self.__content["history"]:
            converted_history.append(mill.Field.convert_field_from_json(field))

        self.__content["history"] = converted_history

    def print_content(self):
        # DEBUG
        print(self.__content)


class Saver(Storage):
    """
    The Saver class represents saving a game into a file

    Attributes:
        game (Game): the game to save
    """

    def __init__(self, game, filename="savedGames/{}-mill.json".format(time.time())):
        """
        constructor for Saver class

        :param game: the game to save
        :type game: Game
        :param filename: the path of the file
        :type filename: str
        :raise: TypeError if game is not an instance of Game
        """
        super().__init__(filename)
        if isinstance(game, mill.Game):
            self.game = game
        else:
            raise TypeError

        self.logger.debug("created Saver instance")

    def save(self):
        """saves the file"""
        data = self.__convert_into_json()
        # write data into json-file
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

        self.logger.debug("save file into {}".format(self.filename))

    def __convert_into_json(self):
        """
        converts the game (Game) into json format

        :return: the converted game
        :rtype: dict
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
