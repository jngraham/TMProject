# James Graham

import Board
import re

# Open the input file and read the instructions

intext = open("input.txt","r");

# We are guaranteed in the statement of the assignment that this file contains at least two lines
# The first line contains a number and the second line contains tuples of coordinates and orientations.

# Create a board with the specified size
size = intext.readline().rstrip();
sea = Board.Board(int(size));

# Remove whitespace and pick up, create only ships with valid orientations
ships = intext.readline().replace(" ","").rstrip();
list_of_ships = re.findall("\([0-9],[0-9],[NESW]\)",ships);

# The create_Ship() method is written to forbid the creation of superimposed Ship objects.
for cotup in list_of_ships:
    sea.create_Ship(cotup)

# Read each line, which is either a set of coordinates or a set of coordinates and characters to instruct the movement of a ship, e.g. MMRRRMLM
# We are guaranteed that each line has only one command so we can get rid of whitespace from the tuple and split at the " "; if the second string is emty, we know the command is a sink command.

for line in intext.readlines():
    line.replace(", ",",").rstrip();
    ctup,characters = line.split(" ")

# i.e. if we have a move command
    if characters != "":
        sea.move_Ship(ctup, characters);
    else:
        sea.sink(ctup);

intext.close()

# Open the output file and print the final state of the board.

outtext = open("output.txt","w");

for ship in sea.get_Ships():
    line = "("+str(ship.getx())+", "+str(ship.gety())+", "#+ship.getdirection()+")";

# i.e. if the ship is sunken
    # if !(ship.afloat()):
        # line += " SUNK";

    line += "\n"

    outtext.write(line)

outtext.close()
