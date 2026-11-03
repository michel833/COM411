import csv


def extract (clothing) :
    print("Extracting...")
    with open(clothing) as file :
        csv_reader = csv.reader(file)
        names = ""
        for values in csv_reader:
            names += f"{values [1]}\n"
            # to add and extracted names with a new line character
            print ("Done!")
    print(f"the extracted items are:\n {names}")


def run_task2 () :
    extract("week/clothing.csv")

if __name__ == "__main__":
        run_task2()
