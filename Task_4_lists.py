def directions():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps
def menu_input():
    print("please select the direction")
    choice =directions()
    for index in range(len(choice)):
        print(f"{index}: {choice[index]}")
        index = int(input())
        return choice[index]
def run_task_4():
    route = []
    print("working out escape route...")
    for count in range (5):
     route.append (menu_input())
    print(f"escape route: {route}")
if __name__ == "__main__":
        run_task_4()