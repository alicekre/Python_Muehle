#
#
#
# Board game mill
#

from ast import literal_eval as make_tuple
from prettytable import PrettyTable  # just used for printing the play board formatted.


class Field:
    """
    This class represents the play board as undirected graph.

    Play board is represented as a undirected graph with node states.
    Name of node depends on position on the play board.
    (ring, row, column) so the left upper node in the outmost ring is called (1, 1, 1).
    State = 0: no chip, state = 1: chip of player_1, state = 2: chip of player_2.

    Attributes:
        field (dictionary): The graph (play board).

    """

    def __init__(self):
        """The constructor for Field class"""
        self.field = {(1, 1, 1): [frozenset({(1, 2, 1), (1, 1, 2)}), 0],
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

    def get_edges(self, node):
        """
        returns all edges of the node

        :param node: the node in the graph
        :type node: tuple
        :return: all edges of the node
        :rtype: frozenset
        """

        return self.field[node][0]

    def get_state(self, node):
        """
        returns the state of the node

        :param node: the node of the graph
        :type node: tuple
        :return: state of the node (0, 1, 2)
        :rtype: int
        """

        return self.field[node][1]

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

        self.field[node][1] = state

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
        for node in self.field:
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


class Player:
    # TODO implement names of players
    """
    The class Player represents a player in the game

    Attributes:
        number_chips (int): the number of chips that the player has but not on the board
        phase (int): the phase in which the player is 1 = set chips, 2 = move on the play board, 3 = jumping
    """
    def __init__(self, number_chips=9, phase=1):
        """The constructor for Player class"""
        self.number_chips = number_chips
        self.phase = phase

    def put_chip(self):
        """reduce number_chips if the player has chips"""
        if self.number_chips <= 0:
            raise PlayerException
        else:
            self.number_chips -= 1


class PlayerException(Exception):
    """The class PlayerException is a Exception class for the class Player"""
    def __init__(self):
        """The constructor for the PlayerException class"""
        pass


class Game:
    """
    The class Game represents the board game mill

    Attributes:
        player_1 (Player): the first player
        player_2 (Player): the second player
        field (Field): the play board
        turn (int): indicates which player is in turn (1, 2)
        move_counter (int): counts the moves between to mills
        history (list): list of class Field, Play board after every move
    """

    def __init__(self):
        """The constructor for Game class"""
        self.player_1 = Player()
        self.player_2 = Player()
        self.field = Field()
        # turn = 1: turn of player_1, turn = 2: turn of player_2
        self.turn = 1
        self.move_counter = 0
        self.history = [self.field]

    def __change_turn(self):
        """
        changes the turn

        Changes turn into 2 if turn=1. Changes turn into 1 if turn=2.

        :raise: ValueError if turn is not 1 or 2
        """

        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
        else:
            raise ValueError

    def __get_number_of_opponent(self):
        """
        returns the number of the player who is not in turn

        :return: number of the player who is not in turn (1, 2)
        :rtype: int
        :raise: ValueError if turn is not 1 or 2
        """

        if self.turn == 1:
            return 2
        elif self.turn == 2:
            return 1
        else:
            raise ValueError

    def __get_player_by_number(self, number):
        """
        returns the player by number

        Returns player_1 if number=1. Returns player_2 if number=2.

        :param number: the number of the player (1, 2)
        :type: int
        :return: the player
        :rtype: Player
        :raise: ValueError if number is not 1 or 2
        """

        if number == 1:
            return self.player_1
        elif number == 2:
            return self.player_2
        else:
            raise ValueError

    def __read_node(self, valid_set):
        """
        reads a node from the console and checks whether node is valid until input is valid and returns this node

        :param valid_set: the set of valid notes
        :type: set
        :return: the read-in node
        :rtype: tuple
        """

        while True:
            try:
                node = input()
                node = make_tuple(node)

                if node in valid_set:
                    return node
                else:
                    # raise ValueError if node is not in valid_set
                    raise ValueError
            # SyntaxError is raised by make_tuple if String is not a tuple
            except (ValueError, SyntaxError):
                print("Input is not a valid node! Try again:")

    # remove a chip of the opponent from the play board
    def __remove_chip(self):
        """reads in a node and removes this chip of the opponent from the play board"""

        # all chips of the opponent are candidates to remove
        possible_nodes_candidates = self.field.get_nodes_by_state(self.__get_number_of_opponent())

        # chips in a mill are not removeable
        possible_nodes = set()
        for i in possible_nodes_candidates:
            if not self.field.is_in_mill(i):
                possible_nodes.add(i)
        frozenset(possible_nodes)

        # If there is no node which is not in a mill to remove allow removing nodes in mills
        if possible_nodes == frozenset({}):
            possible_nodes = possible_nodes_candidates

        print("Which chip would you like to remove?:")
        node = self.__read_node(possible_nodes)
        self.field.set_node_state(node, 0)

    def __check_on_mill(self, node):
        """
        checks if node is in mill, if it is in mill remove one chip

        :param node: the node in the graph to check
        """
        if self.field.is_in_mill(node):
            # remove a chip of the opponent
            self.__remove_chip()
            # decrease move_counter bcause move_counter is increased in every move. The move after a mill is the first
            # not second move.
            self.move_counter = -1

    def __check_history(self):
        """returns True if current field is not more than 2 times in history"""
        duplicates = {}
        for field in self.history:
            if field in duplicates:
                duplicates[field] += 1
                if duplicates[field] >= 3:
                    return False
            else:
                duplicates[field] = 1
        return True

    def __change_to_phase_2(self):
        """changes phase of player to 2 if player have no chips"""
        player = self.__get_player_by_number(self.turn)
        if player.number_chips == 0:
            player.phase = 2

    def __change_to_phase_3(self):
        """changes phase of player to 3 if player have less than 3 chips on the play board"""
        opponent_number = self.__get_number_of_opponent()
        opponent = self.__get_player_by_number(opponent_number)

        if len(self.field.get_nodes_by_state(opponent_number)) < 4 and opponent.number_chips == 0:
            opponent.phase = 3

    def __phase_1(self):
        """move in phase=1"""
        player = self.__get_player_by_number(self.turn)

        # a chip can be placed on every empty node on the play board
        possible_nodes = self.field.get_nodes_by_state(0)

        # read node from the console
        print("Set chip on position:")
        node = self.__read_node(possible_nodes)

        # put chip on play board
        self.field.set_node_state(node, self.turn)
        player.put_chip()

        # check node on mill
        self.__check_on_mill(node)

        # change to phase_2
        self.__change_to_phase_2()

        # change to phase_3
        self.__change_to_phase_3()

    def __phase_2(self):
        """move in phase=2"""
        # try as long as the input is a valid move
        while True:
            try:
                # player loose if there is not any chip he can move
                # if the player looses Game exception is thrown
                if not self.field.check_exist_edges_of_state(self.turn, 0):
                    raise GameException(False, self.turn, self.__get_number_of_opponent())

                # the player can move only his own chips
                possible_nodes = self.field.get_nodes_by_state(self.turn)

                # read the node from the console
                print("Choose the chip you want to move:")
                node = self.__read_node(possible_nodes)

                # the player can move the chip only to a node that is empty
                possible_edges = self.field.get_edges_by_state(node, 0)

                # if the set of possible edges is empty, the chip can not be move -> invalid move
                if len(possible_edges) == 0:
                    raise ValueError

                # read the edge node from the console and check if it is valid
                print("Choose position where you want to put your chip:")
                edge = self.__read_node(possible_edges)

                break
            except ValueError:
                print("Invalid move! Try again:")

        # update graph (play board)
        self.field.set_node_state(node, 0)
        self.field.set_node_state(edge, self.turn)

        # check if the node on the new position is in a mill
        self.__check_on_mill(edge)

        # change to phase_3
        self.__change_to_phase_3()

    def __phase_3(self):
        """move in phase=3"""
        # the player can move only his own chips
        possible_nodes = self.field.get_nodes_by_state(self.turn)

        # the player looses if he has less than 3 chips on the play board
        if len(possible_nodes) < 3:
            raise GameException(False, self.turn, self.__get_number_of_opponent())

        # read the node from the console and check if it is valid
        print("Choose chip you want to jump with:")
        node = self.__read_node(possible_nodes)

        # possible_edges are all nodes with state 0 not only edges because player can jump
        # the player can jump on every empty node
        possible_edges = self.field.get_nodes_by_state(0)

        # read the edge node from the console and check if it is valid
        print("Choose position where you want to put your chip:")
        edge = self.__read_node(possible_edges)

        # update graph (play board)
        self.field.set_node_state(node, 0)
        self.field.set_node_state(edge, self.turn)

        # change to phase_3
        self.__change_to_phase_3()

        # check if chip is on new position in mill
        self.__check_on_mill(edge)

    def move(self):
        """one move in the game"""
        player = self.__get_player_by_number(self.turn)
        phase = player.phase

        # print play board
        self.field.print_playboard()

        # print which player is in turn
        print("Turn: Player ", self.turn)

        try:
            if phase == 1:
                self.__phase_1()
            elif phase == 2:
                self.__phase_2()
            elif phase == 3:
                self.__phase_3()

            # check on remis
            if self.move_counter >= 50 or not self.__check_history():
                raise GameException(True)

        # GameException is raised if one player wins
        # if GameException is raised show which player won and quit game
        except GameException as e:
            print(e.text)
            quit()

        # change the turn after every valid move, increase move_counter, save state of play board in history
        else:
            self.__change_turn()
            self.move_counter += 1
            self.history.append(self.field)


class GameException(Exception):
    """
    The class GameException is a Exception class for the class Game

    Attributes:
        turn (int): the number of the player who is in turn (1, 2)
        opponent (int): the number of the opponent of the player who is in turn
        remis (bool): true if remis
        text (String): text that can be given out
    """

    def __init__(self, remis, turn=None, opponent=None, text=None):
        """The constructor for GameException class"""
        self.remis = remis
        self.turn = turn
        self.opponent = opponent
        if text is None:
            if remis:
                self.text = "Remis!!!"
            else:
                self.text = "Game over! Player {} won!".format(self.opponent)
        else:
            self.text = text


if __name__ == "__main__":
    game = Game()
    while True:
        try:
            game.move()
        except KeyboardInterrupt:
            print("Quit? (y/n):", end="")
            if input() == "y":
                quit()
