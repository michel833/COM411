import json
def read (filename):
    with open ("futurama.json") as file :
        data = json.load(file)
        place_name = data["location"]
        print (f"Place Name:{place_name}")
        population_Size = data["population"]
        print (f"Population Size:{population_Size}")
        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print (f"{name} has the following stats:{stats}",)


def run():
    read ("futurama.json")

if __name__ == "__main__":
    run()



