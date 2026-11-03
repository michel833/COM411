import csv

def read_csv (clothing) :
    with open(clothing) as file :
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        print (f"Heading:\n{heading}")
        print ("value:")
        for values in csv_reader:
            print (values)


def run_task1 () :
    read_csv("clothing.csv")


if __name__ == "__main__":
        run_task1()

