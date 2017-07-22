# James Graham

import sys
from process import *

# Open the input file and read the instructions

inputs = open(sys.argv[1],"r");

sea = initialize(inputs)

sea = calculate(inputs, sea);

inputs.close()

# Open the output file and print the final state of the board.

write(sys.argv[2],sea);
