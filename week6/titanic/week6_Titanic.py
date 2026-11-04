import csv

name_records = []
headings = []
def load_data (titanic) :
    # global heading
    print ("loading data...", end="")
    with open(titanic) as file:
        csv_reader = csv.reader(file) # print the frist line in csv file.
        headings = next(csv_reader)
        for line in csv_reader:
            name_records.append(line)
    print ("Done!")
def run () :
    load_data("titanic.csv")
    num_records = len(name_records)
    print (f"Successfully loaded {num_records} records.")


if __name__ == "__main__":
    run()




