class _Field:
    """
    This class represents the play board as undirected graph.

    Play board is represented as a undirected graph with node states.
    Name of node depends on position on the play board.
    (ring, row, column) so the left upper node in the outmost ring is called (1, 1, 1).
    State = 0: no chip, state = 1: chip of player_1, state = 2: chip of player_2.

    Attributes:
        __field (dictionary): The graph (play board).
    """

    def __init__(self):
        """The constructor for _Field class"""
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