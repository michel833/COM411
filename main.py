def display_chars(library, num_character) :
    with open (library) as file :
        content = file.read(num_character)
        print (content)
 # to print  specified the number of character.

def display_line(library) :
    with open (library) as file :
        content = file.readline().strip()
        # print the first line of the file out
        print (content)


def display_text (library) :
    with open (library) as file :
        content = file.read()  # To print all the text that contained in the file.
        print (content)


def run_task_2 () :
    display_chars("library.txt" , 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
        run_task_2()
