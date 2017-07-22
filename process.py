# James Graham

import Board
import re

# We are guaranteed in the statement of the assignment that this file contains at least two lines
# The first line contains a number and the second line contains tuples of coordinates and orientations.

def initialize(intext):

    # Create a board with the specified size
    size = intext.readline().rstrip();
    board = Board.Board(int(size));

    # Remove whitespace and pick up, create only ships with valid orientations
    ships = intext.readline().replace(" ","").rstrip();
    list_of_ships = re.findall("\([0-9]+,[0-9]+,[NESW]\)",ships);

    # The create_Ship() method is written to forbid the creation of superimposed Ship objects.
    for cotup in list_of_ships:
        board.create_Ship(cotup);

    return board;

def calculate(intext, board):

    # Read each line, which is either a set of coordinates or a set of coordinates and characters to instruct the movement of a ship, e.g. MMRRRMLM
    # We are guaranteed that each line has only one command so we can get rid of whitespace from the tuple and split at the " "; if the second string is emty, we know the command is a sink command.

    for line in intext.readlines():

        command = line.replace(" ","").rstrip();
        # print command
        # ctup,characters = line.split(" ");
        result = re.match(r"(\([0-9]+,[0-9]+\))?([MLR]+)?",command);

        ctup = result.group(1);
        characters = result.group(2);

    # i.e. if we have a move command
        if characters != None:
            board.move_Ship(ctup, characters);
        else:
            board.sink_Ship(ctup);

    return board;


def write(filename, board):

    outtext = open(filename,"w");

    for ship in board.get_Ships():
        line = "("+str(ship.getx())+", "+str(ship.gety())+", "+ship.getdirection()+")";

    # i.e. if the ship is sunken
        if ship.afloat() == False:
            line += " SUNK";

        line += "\n";

        outtext.write(line);

    outtext.close();
