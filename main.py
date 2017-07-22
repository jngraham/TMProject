# James Graham

from process import *

# Open the input file and read the instructions

inputs = open("input.txt","r");

sea = initialize(inputs)

sea = calculate(inputs, sea);

inputs.close()

# Open the output file and print the final state of the board.

write("output.txt",sea);
