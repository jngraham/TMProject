# TMProject

## Introduction

There exists a square board and on each cell of the board we may put a ship, which is characterized by an x-coordinate, a y-coordinate and an orientation (north, south, east, west). We push ships around the board using a sequence of steps: move one space, rotate left and rotate right. We may also sink ships. The size of the board, the initial state of the board (all ships with the parameters specifying each one) and the moves (sailing and sinking) are given as lines of a text file.

## Instructions

The program is run by calling main.py with two arguments, where the first argument is the name of the input text file and the second argument is the name of the file to which the final state of the board will be written. For example, in my command line I write:

`python main.py input.txt output.txt`

The input text file must be formatted as described in the assignment or the program will not work; I took the discussion of the format as a promise and so did not sanitize the input (much; my regex does match only move commands that contain the letters 'M','R','L').

### Ship.py

Ship.py contains the Ship class. The Ship class has four member variables:
* the x- and y-coordinates;
* the orientation;
* and a Boolean to indicate whether the Ship is floating or sunken.

The Ship class has six member functions:
* a constructor that takes x- and y- coordinates and the Ship's orientation;
* a setter function for the Boolean variable;
* getter functions for all the member variables.

### Board.py

Board.py contains the Board class. The Board class has two member variables:
* the size of the Board;
* a dictionary, called "squares", that has values Ship objects and for each key the coordinates of the corresponding Ship, formatted as a string, e.g. "(4,3)".

The Board class has six member functions:
* The constructors make an empty dictionary and set the size of the Board, taken as an argument. The default constructor sets size=1;
* get_Ships(), which returns as a list the Ship objects on the Board;
* create_Ship(), which takes as an argument a coordinate-orientation tuple as a string (from the input text file) and creates a Ship at the specified coordinates on the Board with the specified orientation;
* move_Ship(), which takes as arguments a coordinate ordered pair as a string (as above) and a string consisting of 'M','R','L' (taken from the input text file), calculates the final position of the Ship with the given coordinates following the given sequence of steps, and moves the Ship if it is allowed to (i.e. it is floating, there is no Ship on the destination cell);
* sink_Ship(), which takes an an argument a coordinate ordered pair as a string (as above) (from the input text file) and sets the floating Boolean of the corresponding Ship to False.

### process.py

process.py contains three functions. Two functions parse the input text file and the third writes the state of a given Board to file:
* initialize() takes as an argument the input text file (which is opened by main.py) and reads the first two lines of that file to create a Board of the appropriate size and populate the Board with ships that have the given coordinates and orientations;
* calculate() takes as arguments the input text file (still opened within main.py) and the Board. It reads the remainder of the input text file, determines whether a given line is a move command or a sink command, and instructs the Board to move or sink the appropriate Ship;
* write() takes as an argument the output text filename, opens the file, and writes the coordinates and orientations of each Ship on the Board on a new line, noting if the Ship is sunken with a note "SUNK".

### main.py

main.py merely opens the input text file and calls the three functions in process.py.

## Judgment calls

I chose to make the Board periodic. If an invalid move command is submitted, the corresponding Ship does not move at all. I chose not to make invalid commands end the computation of the moves.
