#
# @author: Christian Birker
#
# console playable mill board game
#


import logging
import time
from mill import *
import storage
from ast import literal_eval as make_tuple

# create logger
logger = logging.getLogger('application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages and another which logs even info messages
fh_1 = logging.FileHandler('debug.log')
fh_2 = logging.FileHandler('info.log')
fh_1.setLevel(logging.DEBUG)
fh_2.setLevel(logging.INFO)
# create formatters and add it to the handlers
formatter_1 = logging.Formatter('%(asctime)s - %(name)30s : %(funcName)30s, ln %(lineno)4s - %(levelname)8s - '
                                '%(message)s')
formatter_2 = logging.Formatter('%(asctime)s - %(name)30s : %(levelname)8s - %(message)s')
fh_1.setFormatter(formatter_1)
fh_2.setFormatter(formatter_2)

# add the handlers to the logger
logger.addHandler(fh_1)
logger.addHandler(fh_2)


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


def main():
    logger.info("start new game")
    print("Do you want to load a saved Game? (y/n):", end="")
    if input() == "y":
        filename = input("Enter path to file: ")
        loader = storage.Loader(filename)
        game = loader.load_game()
    else:
        game = Game()

    try:
        while True:
            print("Player {} in turn.".format(game.get_turn()))
            start_pos = read_node("Choose chip to move: ")
            end_pos = read_node("Choose new position: ")
            try:
                game.move(start_pos, end_pos)
                if game.check_on_mill(end_pos):
                    print("{} is in a mill.".format(end_pos))
                    while True:
                        try:
                            game.remove_chip(read_node("Chip to remove: "))
                            break
                        except MoveException:
                            print("Choose valid chip to remove.")

                # DEBUG
                # saver = storage.Saver(game, "savedGames/{}-mill.json".format(time.time()))
                # saver.save()

            except ValueError:
                print("Invalid node. Try again: ")
            except MoveException:
                print("Invalid move. Try again: ")

    except WinException as e:
        reason = e.reason
        if reason == 1:
            reason = "less than 3 chips"
        elif reason == 2:
            reason = "can not move a chip"

        print("Player {} wins, player {} looses".format(e.number_winner, e.number_looser))
        print("Reason: ", reason)
        quit()

    except RemisException as e:
        print("Remis! Nobody wins.")
        if e.reason == 1:
            print("More than 50 moves between two mills.")
        elif e.reason == 2:
            print("Three times in the play same position.")
        quit()

    except KeyboardInterrupt:
        print("Do you want to save the game? (y/n):", end="")
        if input() == "y":
            saver = storage.Saver(game)
            saver.save()
            quit()
        print("Quit without saving? (y/n):", end="")
        if input() == "y":
            quit()


if __name__ == "__main__":
    main()
