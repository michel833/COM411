import os


def cwd ():
    path = os.getcwd()
    print (f"the current working directory path  is {path}")
    print ("the directory containing the following files:")
    for file in os.listdir(path):
        print(file)


def run () :
    print ("processing ....")
    cwd () # this means calling the function def cwd()


if __name__ == "__main__" :
    run ()