# James Graham

import Board

sea = Board.Board(5);

# Test create_Ship()
if 1==0:
    sea.create_Ship("(1, 2, S)")
    sea.create_Ship("(1, 2, N)")

    print sea.squares;

# Test move_Ship()
if 1==0:
    sea.create_Ship("(1, 2, S)")
    sea.create_Ship("(4, 2, E)")
    sea.move_Ship("(1,2)","RMMRM")
    print sea.squares;

# Test sink_Ship()
if 1==0:
    sea.create_Ship("(1, 2, S)")
    sea.create_Ship("(4, 2, E)")
    sea.sink_Ship("(4,2)")

    print sea.squares["(1,2)"].afloat()
    print sea.squares["(4,2)"].afloat()

# Can we handle Ship objects that are not there?
if 1==0:
    sea.create_Ship("(1, 2, S)")
    sea.move_Ship("(1,3)","RMMRM")

    print sea.squares;

if 1==1:
    sea.sink_Ship("(3,2)")
