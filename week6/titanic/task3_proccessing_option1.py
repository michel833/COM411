
name_records = []

def display_passenger_names () :
    print ("passenger names are ...")
    for records in name_records :
        passenger_names = records
        print (passenger_names)


def run() :
    choice = int(input())
    if choice == 1 :
        display_passenger_names()
    elif choice != 1 :
        print ( "Error! Option not recognised!")


if __name__ == "__main__":
    run()