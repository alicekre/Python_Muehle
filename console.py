#
#
# console playable mill board game
#


from mill import *
from ast import literal_eval as make_tuple


def read_node(msg):
    """
    reads a node from the console and checks whether node is valid until input is valid and returns this node

    :param msg: the input message
    :type msg: str
    :return: the read-in node
    :rtype: tuple
    """

    while True:
        try:
            return make_tuple(input(msg))

        # SyntaxError is raised by make_tuple if String is not a tuple
        except (ValueError, SyntaxError):
            print("Input is not a valid node! Try again:")

def main_logic():
    game = Game()
    print("Game logic reached")
    try:
        #TODO hier auf Oberfläche anpassen
        pass



        #while True:
        #    print("Player {} in turn.".format(game.get_turn()))
        #    start_pos = read_node("Choose chip to move: ")
        #    end_pos = read_node("Choose new position: ")
        #    try:
        #        game.move(start_pos, end_pos)
        #        if game.check_on_mill(end_pos):
        #            print("{} is in a mill.".format(end_pos))
        #            while True:
        #                try:
        #                    game.remove_chip(read_node("Chip to remove: "))
        #                    break
        #                except MoveException:
        #                    print("Choose valid chip to remove.")
        #    except ValueError:
        #        print("Invalid node. Try again: ")
        #    except MoveException:
        #        print("Invalid move. Try again: ")

    except WinException as e:
        print("Player {} wins, player {} looses".format(e.number_winner, e.number_looser))
        quit()

    except RemisException as e:
        print("Remis! Nobody wins.")
        if e.reason == 1:
            print("More than 50 moves between two mills.")
        elif e.reason == 2:
            print("Three times in the play same position.")
        quit()

    except KeyboardInterrupt:
        print("Quit? (y/n):", end="")
        if input() == "y":
            quit()


if __name__ == "__main__":
    main_logic()
