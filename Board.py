# James Graham

from Ship import Ship;

class Board:

    def __init__(self):
        self.size = 1;
        self.squares = {};

    def __init__(self, number):
        self.size = number;
        self.squares = {};

# This takes in a coordinate-and-orientation tuple and creates a ship with those parameters
# The ship is added to the dictionary squares
# The coordinates are taken modulo the size of the board
# The regex to find strings of form (x, y, o) takes place in main

    def get_Ships(self):
        return self.squares.values();

    def create_Ship(self, cotup):

# Remove all whitespace
        cotup = cotup.replace(" ","");

# Remove parentheses
        cotup = cotup.replace("(","");
        cotup = cotup.replace(")","");

# Split at commas
        x,y,o = cotup.split(",");

        coords = "("+x+","+y+")";

# Don't create two ships in the same place
        if coords in self.squares:
            print "Invalid Coordinates to Create Ship";
        else:
            self.squares[coords] = Ship(int(x)%self.size,int(y)%self.size,o);


# This takes in a coordinate tuple and a list of characters including M, L, R
# Following the steps from the initial coordinate we calculate the final coordinate (modulo the size of the board)
# If there is a ship in the final location we do not allow the move to occur.
# Any whitespace in the coordinate tuples is dealt with in main.

    def move_Ship(self, ctup, characters):

        move = True;

# Can only move a ship from a square if there is a ship there
        if ctup in self.squares:

            temp = self.squares[ctup];

            x = temp.getx();
            y = temp.gety();
            o = temp.getdirection();

# Calculate the new location step by step.
            while characters != "":

                step = characters[0];
                characters = characters[1:];

                # print step;

                if step == "M":
                    x += Ship.xmove[o];
                    y += Ship.ymove[o];

                elif step == "L":
                    o = Ship.turnleft[o];

                elif step == "R":
                    o = Ship.turnright[o];

                else:
                    # If we got here there was a problem; abort entire move procedure
                    print "Invalid Move Command";
                    move = False;

            x %= self.size;
            y %= self.size;

            newctup = "("+str(x)+","+str(y)+")";

# Can only move a ship if the destination has no ship; if there is a ship at the destination cancel the move
# Can only move a ship that has not sunk! But a sunken ship could prevent another ship from moving to its location

            if newctup in self.squares:
                print "Invalid Destination";
                move = False;
            if self.squares[ctup].afloat() == False:
                print "Attempted to Move Sunken Ship";
                move = False;

# If our ship is afloat, won't end up on another ship and the move command is valid, move the ship.
# In which case create a new ship with the new coordinates and orientation and pop the old ship
            if move:
                self.squares[newctup]=Ship(x,y,o);
                self.squares.pop(ctup);

    def sink_Ship(self, ctup):

# Can only sink a ship if it is there
        if ctup in self.squares:
            self.squares[ctup].sink();
