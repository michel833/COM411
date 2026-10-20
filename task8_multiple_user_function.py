def display_ladder(steps) :
    for steps in range(steps) :
        print ("|  |")
        print ("****")
def create_ladder() :
    print ("how many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()

