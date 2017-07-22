# James Graham

from process import *

# Test create_Ship()
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(1, 2, S)");
    sea.create_Ship("(1, 2, N)");

    print sea.squares;

# Test move_Ship() to move one ship through another ship (allowed)
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(1, 2, S)");
    sea.create_Ship("(4, 2, E)");
    sea.move_Ship("(1,2)","RMMRM");
    print sea.squares;

# Test move_Ship() to put one ship on another ship (verboten)
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(1, 2, S)");
    sea.create_Ship("(2, 2, W)");
    sea.move_Ship("(2,2)","M");
    print sea.squares;

# Test sink_Ship()
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(1, 2, S)");
    sea.create_Ship("(4, 2, E)");
    sea.sink_Ship("(4,2)");

    print sea.squares["(1,2)"].afloat();
    print sea.squares["(4,2)"].afloat();

# Try to move a sunken ship (verboten)
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(3,2,N)")
    sea.sink_Ship("(3,2)")
    sea.move_Ship("(3,2)","M")

    print sea.squares


# Can we handle Ship objects that are not there?
if 1==0:

    sea = Board.Board(5);

    sea.create_Ship("(1, 2, S)");
    sea.move_Ship("(1,3)","RMMRM");

    print sea.squares;

if 1==0:

    sea = Board.Board(5);

    sea.sink_Ship("(3,2)");

    print sea.squares;

# Test initialize()
if 1==0:
    inputs = open("input.txt","r");

    sea = initialize(inputs);

    inputs.close();

    print sea.size;

    for ship in sea.get_Ships():
        print ship.getx(),ship.gety(),ship.getdirection();

#  Test calculate()
if 1==0:
# I have written "test.txt" so that one ship moves onto another ship; the process should be aborted
    inputs = open("test.txt","r");

    sea = initialize(inputs);

    sea = calculate(inputs,sea);

    inputs.close();

    for ship in sea.get_Ships():
        print ship.getx(),ship.gety(),ship.getdirection();

# Test write()
if 1==1:
    sea = Board.Board(5);

    sea.create_Ship("(3,2,N)")
    sea.create_Ship("(4,1,W)")

    sea.move_Ship("(4,1)","MM")
    sea.sink_Ship("(2,1)")

    write("outputtest.txt",sea)
