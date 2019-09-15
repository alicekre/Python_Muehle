#
#
#
# Logic of board game mill
#

import logging
import json
import time
from prettytable import PrettyTable  # just used for printing the play board formatted.
from ast import literal_eval as make_tuple

# create logger for module
module_log = logging.getLogger('application.mill')


class Field:
    """
    This class represents the play board as undirected graph.

    Play board is represented as a undirected graph with node states.
    Name of node depends on position on the play board.
    (ring, row, column) so the left upper node in the outmost ring is called (1, 1, 1).
    State = 0: no chip, state = 1: chip of player_1, state = 2: chip of player_2.

    Attributes:
        __field (dict): The graph (play board).
    """

    def __init__(self, states=None):
        """
        The constructor for _Field class

        :param states: the field with states
        :type states: dict
        """
        self.__field = {(1, 1, 1): [frozenset({(1, 2, 1), (1, 1, 2)}), 0],
                        (1, 1, 2): [frozenset({(1, 1, 1), (1, 1, 3), (2, 1, 2)}), 0],
                        (1, 1, 3): [frozenset({(1, 1, 2), (1, 2, 3)}), 0],
                        (1, 2, 1): [frozenset({(1, 1, 1), (1, 3, 1), (2, 2, 1)}), 0],
                        (1, 2, 3): [frozenset({(1, 1, 3), (1, 3, 3), (2, 2, 3)}), 0],
                        (1, 3, 1): [frozenset({(1, 2, 1), (1, 3, 2)}), 0],
                        (1, 3, 2): [frozenset({(1, 3, 1), (1, 3, 3), (2, 3, 2)}), 0],
                        (1, 3, 3): [frozenset({(1, 3, 2), (1, 2, 3)}), 0],
                        (2, 1, 1): [frozenset({(2, 1, 2), (2, 2, 1)}), 0],
                        (2, 1, 2): [frozenset({(2, 1, 1), (2, 1, 3), (3, 1, 2), (1, 1, 2)}), 0],
                        (2, 1, 3): [frozenset({(2, 1, 2), (2, 2, 3)}), 0],
                        (2, 2, 1): [frozenset({(2, 1, 1), (2, 3, 1), (1, 2, 1), (3, 2, 1)}), 0],
                        (2, 2, 3): [frozenset({(2, 1, 3), (2, 3, 3), (3, 2, 3), (1, 2, 3)}), 0],
                        (2, 3, 1): [frozenset({(2, 2, 1), (2, 3, 2)}), 0],
                        (2, 3, 2): [frozenset({(2, 3, 1), (2, 3, 3), (1, 3, 2), (3, 3, 2)}), 0],
                        (2, 3, 3): [frozenset({(2, 3, 2), (2, 2, 3)}), 0],
                        (3, 1, 1): [frozenset({(3, 1, 2), (3, 2, 1)}), 0],
                        (3, 1, 2): [frozenset({(3, 1, 1), (3, 1, 3), (2, 1, 2)}), 0],
                        (3, 1, 3): [frozenset({(3, 1, 2), (3, 2, 3)}), 0],
                        (3, 2, 1): [frozenset({(3, 1, 1), (3, 3, 1), (2, 2, 1)}), 0],
                        (3, 2, 3): [frozenset({(3, 1, 3), (3, 3, 3), (2, 2, 3)}), 0],
                        (3, 3, 1): [frozenset({(3, 2, 1), (3, 3, 2)}), 0],
                        (3, 3, 2): [frozenset({(3, 3, 1), (3, 3, 3), (2, 3, 2)}), 0],
                        (3, 3, 3): [frozenset({(3, 3, 2), (3, 2, 3)}), 0]
                        }

        if states is not None:
            for node in self.__field:
                self.set_node_state(node, states[node])

    def get_nodes(self):
        """
        returns all nodes of the graph as a set

        :return: all nodes of graph
        :rtype: set
        """
        nodes = set()
        for node in self.__field:
            nodes.add(node)
        return nodes

    def get_edges(self, node):
        """
        returns all edges of the node

        :param node: the node in the graph
        :type node: tuple
        :return: all edges of the node
        :rtype: frozenset
        """

        return self.__field[node][0]

    def get_state(self, node):
        """
        returns the state of the node

        :param node: the node of the graph
        :type node: tuple
        :return: state of the node (0, 1, 2)
        :rtype: int
        """

        return self.__field[node][1]

    def set_node_state(self, node, state=0):
        """
        sets the state of the node

        :param node: the node in the graph
        :param state: state of the node (0, 1, 2)
        :type node: tuple
        :type state: int
        :raise: ValueError if state is not 0, 1 or 2
        """

        # state must be 0, 1 or 2
        if state not in (0, 1, 2):
            raise ValueError

        self.__field[node][1] = state

    def deg(self, node):
        """
        returns the degree of the node

        :param node: the node in the graph
        :type node: tuple
        :return: degree of the node
        :rtype: int
        """

        return len(self.get_edges(node))

    def __is_center(self, node):
        """
        returns True if the node is center node

        A node is center if deg(node) > 2.

        :param node: the node in the graph
        :type node: tuple
        :return: True if node is center, else False
        :rtype: bool
        """

        return self.deg(node) > 2

    def is_in_mill(self, node):
        """
        returns True if node is in a mill

        :param node: the node in the graph
        :type node: tuple
        :return: True if node is in mill
        :rtype: bool
        """

        edges = self.get_edges(node)
        state = self.get_state(node)
        deg = self.deg(node)

        # test center node whether it is in mill
        if self.__is_center(node):
            counter = 0
            for i in edges:
                if not self.__is_center(i) and state == self.get_state(i):
                    counter += 1
                    if counter == 2:
                        return True

            # center node is in ring 2
            if deg == 4:
                counter = 0
                for i in edges:
                    if self.__is_center(i) and state == self.get_state(i):
                        counter += 1
                        if counter == 2:
                            return True

            # center node is in ring 1 or 3
            else:
                for i in edges:
                    if self.__is_center(i) and state == self.get_state(i):
                        for j in self.get_edges(i):
                            if self.__is_center(j) and state == self.get_state(j) and node != j:
                                return True

        # test corner node whether it is in mill
        else:
            for i in edges:
                if state == self.get_state(i):
                    for j in self.get_edges(i):
                        if state == self.get_state(j) and not self.__is_center(j) and node != j:
                            return True

        return False

    def get_nodes_by_state(self, state):
        """
        returns all nodes with state

        :param state: state of the nodes, (0,1,2)
        :type state: int
        :return: all nodes with state
        :rtype: frozenset
        :raise: ValueError if state is not 0, 1 or 2
        """

        # state must be 0, 1 or 2
        if state not in (0, 1, 2):
            raise ValueError

        nodes = set()
        for node in self.__field:
            if self.get_state(node) == state:
                nodes.add(node)
        return frozenset(nodes)

    def get_edges_by_state(self, node, state):
        """
        returns all edges with state of a node

        :param node: the node of the graph
        :type node: tuple
        :param state: the state of the edges (0,1,2)
        :type state: int
        :return: all edges with state of the node
        :rtype: frozenset
        :raise: ValueError if state is not 0, 1 or 2
        """

        # state must be 0, 1 or 2
        if state not in (0, 1, 2):
            raise ValueError

        edges = set()
        for edge in self.get_edges(node):
            if self.get_state(edge) == state:
                edges.add(edge)
        return frozenset(edges)

    def get_states(self):
        """
        returns all nodes and their state as dictionary

        :return: all nodes and their state
        :rtype: dict
        """
        graph = {}
        for node in self.__field:
            graph[node] = self.get_state(node)
        return graph

    def print_playboard(self):
        """prints the current graph formatted in a table (play board)"""
        table = PrettyTable(padding_width=3)

        table.add_row(["(1,1,1) " + str(self.get_state((1, 1, 1))),
                       "---",
                       "---",
                       "(1,1,2) " + str(self.get_state((1, 1, 2))),
                       "---",
                       "---",
                       "(1,1,3) " + str(self.get_state((1, 1, 3)))
                       ])

        table.add_row(["|",
                       "(2,1,1) " + str(self.get_state((2, 1, 1))),
                       "---",
                       "(2,1,2) " + str(self.get_state((2, 1, 2))),
                       "---",
                       "(2,1,3) " + str(self.get_state((2, 1, 3))),
                       "|"
                       ])

        table.add_row(["|",
                       "|",
                       "(3,1,1) " + str(self.get_state((3, 1, 1))),
                       "(3,1,2) " + str(self.get_state((3, 1, 2))),
                       "(3,1,3) " + str(self.get_state((3, 1, 3))),
                       "|",
                       "|"
                       ])

        table.add_row(["(1,2,1) " + str(self.get_state((1, 2, 1))),
                       "(2,2,1) " + str(self.get_state((2, 2, 1))),
                       "(3,2,1) " + str(self.get_state((3, 2, 1))),
                       "",
                       "(3,2,3) " + str(self.get_state((3, 2, 3))),
                       "(2,2,3) " + str(self.get_state((2, 2, 3))),
                       "(1,2,3) " + str(self.get_state((1, 2, 3)))
                       ])

        table.add_row(["|",
                       "|",
                       "(3,3,1) " + str(self.get_state((3, 3, 1))),
                       "(3,3,2) " + str(self.get_state((3, 3, 2))),
                       "(3,3,3) " + str(self.get_state((3, 3, 3))),
                       "|",
                       "|"
                       ])

        table.add_row(["|",
                       "(2,3,1) " + str(self.get_state((2, 3, 1))),
                       "---",
                       "(2,3,2) " + str(self.get_state((2, 3, 2))),
                       "---",
                       "(2,3,3) " + str(self.get_state((2, 3, 3))),
                       "|"
                       ])

        table.add_row(["(1,3,1) " + str(self.get_state((1, 3, 1))),
                       "---",
                       "---",
                       "(1,3,2) " + str(self.get_state((1, 3, 2))),
                       "---",
                       "---",
                       "(1,3,3) " + str(self.get_state((1, 3, 3)))
                       ])

        print(table)

    def check_exist_edges_of_state(self, node_state, edge_state):
        """
        returns True if there is a node with node_state with at least one edge with edge_state

        Returns True if a chip of the player exists that can be moved (edge_state=0).

        :param node_state: state of the nodes (0, 1, 2)
        :type node_state: int
        :param edge_state: state of the edges (0, 1, 2)
        :type edge_state: int
        :return: True if at least one edge with state exists
        :rtype: bool
        :raise: ValueError if node_state or edge_state is not 0, 1 or 2
        """

        # states must be 0, 1 or 2
        if node_state not in (0, 1, 2) or edge_state not in (0, 1, 2):
            raise ValueError

        nodes = self.get_nodes_by_state(node_state)
        for node in nodes:
            if len(self.get_edges_by_state(node, edge_state)) > 0:
                return True
        return False

    def get_converted_json(self):
        """


        :return:
        """
        field_converted = {}
        for node in self.__field:
            field_converted[str(node)] = self.__field[node]
        return field_converted

    @staticmethod
    def convert_field_from_json(field):
        """
        converts a field in json format into a dict (keys are tuples)

        :param field: field in json format
        :return: field
        :rtype: dict
        """
        field_converted = {}
        for node in field:
            field_converted[make_tuple(node)] = field[node]
        return field_converted


class Player:
    """
    The class Player represents a player in the game

    Attributes:
        number_chips (int): the number of chips that the player has but not on the board
        phase (int): the phase in which the player is 1 = set chips, 2 = move on the play board, 3 = jumping
        number (int):
    """

    def __init__(self, number, number_chips=9, phase=1):
        """The constructor for Player class"""
        if number not in (1, 2) or number_chips not in range(0, 10) or phase not in (1, 2, 3):
            raise ValueError
        self.__number = number
        self.__number_chips = number_chips
        self.phase = phase

    def get_number(self):
        """
        returns the number of the player

        :return: number of player
        :rtype: int
        """
        return self.__number

    def get_number_chips(self):
        """
        returns number of chips which are left to set

        :return: number of chips
        :rtype: int
        """
        return self.__number_chips

    def put_chip(self):
        """
        reduce number_chips if the player has chips

        :raise: PlayerException if player has less than 1 chip
        """

        if self.__number_chips <= 0:
            raise PlayerException
        else:
            self.__number_chips -= 1


class PlayerException(Exception):
    """The class PlayerException is a Exception class for the class Player"""
    def __init__(self):
        """The constructor for the PlayerException class"""
        pass


class History:
    """
    The History class

    Attributes:
        __fields (list): list of Field with fields in history
        __move_counter (int): number of moves since last mill
        __fields_counter (dict): hashtable to count equal field states
    """

    def __init__(self, fields=None, move_counter=0):
        """
        The constructor for History class

        :param fields: the list of fields
        :type fields: list of Field
        :param move_counter: counter of moves since last mill
        :type move_counter: int
        """
        if fields is None:
            self.__fields = []
            self.__fields_counter = {}
        else:
            self.__fields = fields

            # built fields_counter with fields
            for field in self.__fields:
                # It is enough to compare states of fields
                field = field.get_states()
                # dict is not hashable so do workaround
                hashable = frozenset(field.items())
                if hashable in self.__fields_counter:
                    self.__fields_counter[hashable] += 1
                else:
                    self.__fields_counter[hashable] = 1

        self.__move_counter = move_counter

    def get_fields(self):
        """"""
        return self.__fields

    def get_move_counter(self):
        """
        returns the value of move_counter

        :return: move_counter
        :rtype: int
        """
        return self.__move_counter

    def add(self, field):
        """
        adds a field to history

        :param field: the field to add in history
        :type field: Field
        """
        # add field in history
        self.__fields.append(field)

        # compare just the states
        field = field.get_states()

        # add field to counting hashtable
        # dict in not hashable so do workaround
        hashable = frozenset(field.items())
        if hashable in self.__fields_counter:
            self.__fields_counter[hashable] += 1
        else:
            self.__fields_counter[hashable] = 1

    def increase_move_counter(self):
        """increases move_counter"""
        self.__move_counter += self.__move_counter + 1

    def decrease_move_counter(self):
        """decreases move_counter to 0"""
        self.__move_counter = 0

    def get_highest_fields_counter(self):
        """
        returns highest value in fields_counter

        :return: highest value in fields_counter
        :rtype: int
        """
        return max(self.__fields_counter)


class Game:
    """
    The Game class

    Attributes:
        __player_1 (Player): The first player
        __player_2 (Player): The second player
        __field (Field): The play board
        __turn (Player): The player who is in turn
        __history (History): history of field
        __mill (bool): indicates if there is a mill and no chip was removed
    """

    def __init__(self, player_1=Player(1), player_2=Player(2), field=Field(), turn=None, history=History(),
                 mill=False):
        """


        :param player_1:
        :param player_2:
        :param field:
        :param turn:
        :param history:
        :param mill:
        """
        # logger for Game class
        self.logger = logging.getLogger('application.mill.Game')

        self.__player_1 = player_1
        self.__player_2 = player_2
        self.__field = field

        if turn is None:
            self.__turn = self.__player_1
        else:
            self.__turn = turn

        self.__history = history
        self.__mill = mill
        self.logger.debug("New Game instance created")

    # TODO delete method
    @staticmethod
    def __convert_from_json(filename):
        """
        converts json file into dict

        :param filename: filename of the json file
        :type filename: str
        :return: a dict with all the data
        :rtype: dict
        """
        # open json-file
        with open(filename, 'r') as f:
            content = json.load(f)

        # convert field
        content["field"] = Field.convert_field_from_json(content["field"])

        # convert history
        converted_history = []
        for field in content["history"]:
            converted_history.append(Field.convert_field_from_json(field))
        content["history"] = converted_history

        return content

    def __change_turn(self):
        """
        changes turn between the two players

        :raise: ValueError if turn is not player_1 or player_2
        """

        if self.__turn is self.__player_1:
            self.__turn = self.__player_2
            self.logger.info("changed turn to 2")
            print("Changed player in turn to player 2")
        elif self.__turn is self.__player_2:
            self.__turn = self.__player_1
            self.logger.info("changed turn to 1")
            print("Changed player in turn to player 1")
        else:
            self.logger.error("raise ValueError")
            raise ValueError

    def __get_opponent(self):
        """
        returns the player who is not in turn

        :return: the player who is not in turn
        :rtype: Player
        :raise: ValueError if Player is not player_1 or player_2
        """

        if self.__turn is self.__player_1:
            return self.__player_2
        elif self.__turn is self.__player_2:
            return self.__player_1
        else:
            self.logger.error("raise ValueError")
            raise ValueError

    def __check_history(self):
        """
        returns True if current field is not more than 2 times in history

        :return: True if current field is not more than 2 times in history
        :rtype: bool
        """
        if self.__history.get_highest_fields_counter() >= 3:
            return False
        return True

    def __change_to_phase_2(self):
        """changes phase of player to 2 if player have no chips"""
        player = self.__turn
        if player.get_number_chips() == 0:
            player.phase = 2
            self.logger.info("changed Player {} into phase 2".format(player.get_number()))
            print("Changed Player {} into move phase".format(player.get_number()))

    def __change_to_phase_3(self):
        """changes phase of player to 3 if player have less than 3 chips on the play board"""
        opponent = self.__get_opponent()
        if len(self.__field.get_nodes_by_state(opponent.get_number())) < 4 and opponent.get_number_chips() == 0:
            opponent.phase = 3
            self.logger.info("changed Player {} into phase 3".format(opponent.get_number()))
            print("Changed Player {} into jump phase".format(opponent.get_number()))

    def __check_phase_1(self, start_pos, end_pos):
        """
        checks if a move in phase 1 is valid

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos:tuple
        :raise: MoveException if move is invalid
        """

        if start_pos is not None:
            self.logger.debug("raise MoveException: player is in phase 1, start_pos must be None")
            raise MoveException("Player is in putting phase.")
        if self.__field.get_state(end_pos) != 0:
            self.logger.debug("raise MoveException: one chip is already on {}".format(end_pos))
            raise MoveException("There is already a chip on this position.")
        if self.__turn.get_number_chips() < 1:
            self.logger.debug("raise MoveException: no chips")
            raise MoveException("Player has no chips to set.")

    def __check_phase_2(self, start_pos, end_pos):
        """
        checks if a move in phase 2 is valid

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos:tuple
        :raise: MoveException if move is invalid
        """

        valid_start = self.__field.get_nodes_by_state(self.__turn.get_number())

        if start_pos not in valid_start:
            self.logger.debug("raise MoveException: chip is not of player in turn")
            raise MoveException("Chip is not of Player {}.".format(self.__turn.get_number()))

        valid_end = self.__field.get_edges_by_state(start_pos, 0)
        if end_pos not in valid_end:
            self.logger.debug("raise MoveException: chip can not be moved")
            raise MoveException("Chip can not be moved to this position.")

    def __check_phase_3(self, start_pos, end_pos):
        """
        checks if a move in phase 3 is valid

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos:tuple
        :raise: MoveException if move is invalid
        """

        valid_start = self.__field.get_nodes_by_state(self.__turn.get_number())
        valid_end = self.__field.get_nodes_by_state(0)
        if start_pos not in valid_start:
            self.logger.debug("raise MoveException: chip not of player in turn")
            raise MoveException("Chip is not of Player {}.".format(self.__turn.get_number()))
        if end_pos not in valid_end:
            self.logger.debug("raise MoveException: chip can not be moved")
            raise MoveException("Chip can not be moved to this position.")

    def __phase_1(self, end_pos):
        """
        move in phase 1

        :param end_pos: new position of the chip
        :type end_pos:tuple
        """

        self.__field.set_node_state(end_pos, self.__turn.get_number())
        self.__turn.put_chip()
        self.logger.info("Put chip of Player {} on {}".format(self.__turn.get_number(), end_pos))
        print("Put chip of Player {} on position {}".format(self.__turn.get_number(), end_pos))
        if self.check_on_mill(end_pos):
            self.__mill = True
            self.logger.info("{} is in mill".format(end_pos))
            # decrease move_counter because move_counter is increased in every move. The move after a mill is the first
            # not second move.
            self.__move_counter = -1
        self.__change_to_phase_2()

    def __phase_2(self, start_pos, end_pos):
        """
        move in phase 2

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos: tuple
        """

        # update graph (play board)
        self.__field.set_node_state(start_pos, 0)
        self.__field.set_node_state(end_pos, self.__turn.get_number())
        self.logger.info("move chip of Player {} from {} to {}".format(self.__field.get_state(start_pos), start_pos,
                                                                       end_pos))

        # check if the node on the new position is in a mill
        if self.check_on_mill(end_pos):
            self.__mill = True
            self.logger.info("{} is in mill".format(end_pos))
            # decrease move_counter because move_counter is increased in every move. The move after a mill is the first
            # not second move.
            self.__move_counter = -1

    def __phase_3(self, start_pos, end_pos):
        """
        move in phase 3

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos: tuple
        """

        # update graph (play board)
        self.__field.set_node_state(start_pos, 0)
        self.__field.set_node_state(end_pos, self.__turn.get_number())
        self.logger.info("move chip of Player {} from {} to {}".format(self.__field.get_state(start_pos), start_pos,
                                                                       end_pos))

        # check if the node on the new position is in a mill
        if self.check_on_mill(end_pos):
            self.__mill = True
            self.logger.info("{} is in mill".format(end_pos))

    def __check_on_win_and_remis(self):
        """
        checks if player wins or the game end because remis

        :raise: WinException if player wins
        :raise: RemisException if game ends in remis
        """

        opponent = self.__get_opponent()
        # the opponent looses if he has less than 3 chips on the play board
        if len(self.__field.get_nodes_by_state(opponent.get_number())) < 3 and opponent.get_number_chips() == 0:
            self.logger.debug("raise WinException: Player {} wins".format(self.__turn.get_number()))
            raise WinException(self.__turn.get_number(), self.__get_opponent().get_number())

        # opponent looses if there is not any chip he can move
        elif not self.__field.check_exist_edges_of_state(opponent.get_number(), 0):
            self.logger.debug("raise WinException: Player {} wins".format(self.__turn.get_number()))
            raise WinException(self.__turn.get_number(), self.__get_opponent().get_number())

        # check on remis
        # 50 moves without mill
        elif self.__history.get_move_counter() >= 50:
            self.logger.debug("raise RemisException: 50 moves no mill")
            raise RemisException(1)

        # 3 times same state of the play board
        elif not self.__check_history():
            self.logger.debug("raise RemisException: 3 times same position")
            raise RemisException(2)

    def __is_valid_move(self, start_pos, end_pos):
        """
        checks if move is valid

        :param start_pos: current position of the chip
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos: tuple
        :raise: ValueError if position is not a valid node
        """

        nodes = self.__field.get_nodes()
        # check whether nodes are valid
        if (start_pos not in nodes or start_pos is None) and end_pos not in nodes:
            self.logger.debug("raise ValueError")
            raise ValueError

        # check whether move is valid for the phase of the player
        if self.__turn.phase == 1:
            self.__check_phase_1(start_pos, end_pos)
        elif self.__turn.phase == 2:
            self.__check_phase_2(start_pos, end_pos)
        elif self.__turn.phase == 3:
            self.__check_phase_3(start_pos, end_pos)
        else:
            self.logger.debug("raise ValueError")
            raise ValueError

    def get_history(self):
        """

        :return:
        """
        return self.__history

    def get_field_instance(self):
        """

        :return:
        """
        return self.__field

    def get_turn(self):
        """
        returns the the number of the player who is in turn

        :return: the number of the player who is in turn
        :rtype: int
        """

        return self.__turn.get_number()

    def get_field(self):
        """
        returns the nodes and states

        :return: the current state of every node
        :rtype: dict
        """

        return self.__field.get_states()

    def get_player_1(self):
        """"""
        return self.__player_1

    def get_player_2(self):
        """"""
        return self.__player_2

    def get_mill(self):
        """"""
        return self.__mill

    def remove_chip(self, node):
        """
        reads in a node and removes this chip of the opponent from the play board

        :param node: the position of the chip to remove
        :type node: tuple
        :raise: MoveException if player has no chip in a mill or if node is not removeable
        """

        # check whether mill really exists
        if not self.__mill:
            self.logger.debug("raise MoveException: no mill")
            raise MoveException("There is no mill.")

        # all chips of the opponent are candidates to remove
        possible_nodes_candidates = self.__field.get_nodes_by_state(self.__get_opponent().get_number())

        # chips in a mill are not removeable
        possible_nodes = set()
        for i in possible_nodes_candidates:
            if not self.__field.is_in_mill(i):
                possible_nodes.add(i)
        frozenset(possible_nodes)

        # If there is no node which is not in a mill to remove allow removing nodes in mills
        if possible_nodes == frozenset({}):
            possible_nodes = possible_nodes_candidates

        if node in possible_nodes:
            self.__field.set_node_state(node, 0)
            self.logger.info("remove chip on {}".format(node))
            print("Remove chip of {}".format(node))
            self.__field.print_playboard()
            self.__mill = False
            # decrease move_counter to 0
            self.__history.decrease_move_counter()
            self.__check_on_win_and_remis()
            self.__change_to_phase_3()
            self.__change_turn()

        else:
            self.logger.debug("raise MoveException: not valid chip of opponent")
            raise MoveException("Chip is not removeable")

    def check_on_mill(self, node):
        """
        checks if node is in mill

        :param node: the node in the graph to check
        :type node: tuple
        :return: True if node is in mill
        :rtype: bool
        """

        return self.__field.is_in_mill(node)

    def move(self, start_pos, end_pos):
        """
        one move in the game

        :param start_pos: current position of the chip, None if you want to put a chip in phase 1
        :type start_pos: tuple
        :param end_pos: new position of the chip
        :type end_pos: tuple
        :raise: MillException if there is a mill and no chip has been removed
        """

        # check whether mill exists
        if self.__mill:
            self.logger.debug("raise MillException: mill exists")
            raise MillException
        else:
            # check whether move is valid
            self.__is_valid_move(start_pos, end_pos)

            if self.__turn.phase == 1:
                self.__phase_1(end_pos)
            elif self.__turn.phase == 2:
                self.__phase_2(start_pos, end_pos)
            elif self.__turn.phase == 3:
                self.__phase_3(start_pos, end_pos)

            # if there is no mill finish move
            if not self.__mill:
                self.__field.print_playboard()
                self.__history.increase_move_counter()
                self.__history.add(self.__field)
                if self.__turn.phase in (2, 3):
                    self.__check_on_win_and_remis()
                self.__change_turn()


class MoveException(Exception):
    """
    The MoveException class

    Attributes:
        msg (str): the message/reason
    """

    def __init__(self, msg):
        """the constructor for MoveException class"""
        self.msg = msg


class MillException(Exception):
    """ The MillException class"""

    def __init__(self):
        """the constructor for MillException class"""
        pass


class WinException(Exception):
    """
    The WinException class

    Attributes:
        number_winner (int): the number of the player who wins
        number_looser (int): the number of the player who looses
    """

    def __init__(self, number_winner, number_looser):
        """the constructor for WinException class"""
        self.number_winner = number_winner
        self.number_looser = number_looser


class RemisException(Exception):
    """
    The RemisException class

    Attributes:
        reason (int): the reason of remis
                        1= more than 50 moves between two mills,
                        2= three times in the play same field status
    """

    def __init__(self, reason):
        """the constructor for RemisException class"""
        self.reason = reason
