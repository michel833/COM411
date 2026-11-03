def search (library):
    print ("searching....")
    with open ("library.txt") as file:
        for location in file:
            print (f"looked in {location.strip()}")
            print ("...Done!")

# to read a text file line by line.

def run_task_3 () :
    search("library.txt")


if __name__ == "__main__":
        run_task_3()

