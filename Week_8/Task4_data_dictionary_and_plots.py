import matplotlib.pyplot as plt
import random as rnd

def data () :
    paths = {}
    print ("what type of line they would like(:--or-)?")
    line = input()
    print ("what colour would you like(r,g,b)?")
    colour = input()
    print ("what style of maker they would like(o,s or ^)?")
    style = input()
    paths["line"] = line
    paths["colour"] = colour
    paths["style"] = style
    return paths

def generate () :
    print ("How many lines would you like to display?")
    line = int(input())
    for line  in range(line):
        values =data ()
        x = rnd.sample(range (1,10),5)
        y = rnd.sample(range (1,10),5)
        format = (f"{values["colour"]},{values["line"]},{values["style"]}")
        plt.plot(x,y,format)
        plt.show()

def run () :
    print ("Running...")
    generate()
    print ("Done")