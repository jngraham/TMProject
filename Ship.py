#James Graham

class Ship:

    # To help the move calculations; i.e. "what is my new orientation if I start with N and turn Left?"
    # By how much does my x coordinate change if I move N?
    turnleft = {"N":"W","W":"S","S":"E","E":"N"};
    turnright = {"N":"E","E":"S","S":"W","W":"N"};
    xmove = {"N":0,"E":1,"S":0,"W":-1};
    ymove = {"N":1,"E":0,"S":-1,"W":0};

    def __init__(self, xpos, ypos, orientation):
        self.__xcoord = xpos;
        self.__ycoord = ypos;
        self.__direction = orientation;
        self.__floating = True

    def getx(self):
        return self.__xcoord;

    def gety(self):
        return self.__ycoord;

    def getdirection(self):
        return self.__direction;

    def afloat(self):
        return self.__floating;

    def sink(self):
        self.__floating = False;
