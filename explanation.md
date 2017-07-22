# TMProject

## Introduction

There exists a square board and on each cell of the board we may put a ship, which is characterized by an x-coordinate, a y-coordinate and an orientation (north, south, east, west). We push ships around the board using a sequence of steps: move one space, rotate left and rotate right. We may also sink ships. The size of the board, the initial state of the board (all ships with the parameters specifying each one) and the moves (sailing and sinking) are given as lines of a text file of a certain format.

## Approach

To implement the ships on the board I made copious use of dictionaries. One approach could have been to use a doubly-indexed list, each of which has a Ship object or None as the value, but I preferred to keep track of only the cells on the board that contain ships. To that end, the squares member of a Board object is a dictionary: the key is a string containing an ordered pair, for example "(4,3)" and the value is a Ship object.

Each Ship object has four member variables: its x- and y-coordinates, its orientation and a Boolean indicating whether the ship has been sunk, since a sunken ship should not move on the board but can prevent other ships from moving. It is awkward to store each Ship object's coordinates twice (once in the key and once in the object's member variables) but it is essential that those coordinates match. To that end all member variables are private and there is no setter function for the coordinates; when we move a Ship, we make a new entry in the dictionary, a Ship with the new coordinates given by a key with those new coordinates, and we delete the "old" Ship.
