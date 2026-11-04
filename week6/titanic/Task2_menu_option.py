def display_menu ():
    print ("""

Please select one of the following options: 
[1] Display the names of all passengers 
[2] Display the number of passengers that survived 
[3] Display the number of passengers per gender 
[4] Display the number of passengers per age group 

    
     """)
    choice =int (input()) # return the integer of the variable.
    return choice


def run () :
    selection_option = display_menu() # assign the variable to the function that it has call
    print (f"you have selection options:{selection_option}")


if __name__ == "__main__":
    run()

