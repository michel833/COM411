import json
def read_task2(filename):
    print("reading...", end="")
    with open(filename) as file:
        data = json.load(file)
    print ("done!")
    return data

def save (filename, data) :
    print ("exporting...", end="")
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print ("done!")

def run () :
    json_data = read_task2("futurama.json")
    save ("futurama.json", json_data)

if __name__ == "__main__":

    run()
