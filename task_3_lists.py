def directions():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps
def menu ():
    print("please select the direction:")
    choice= directions()
    for index in range(len(choice)):
        print (f"[index]: {{choice[index]}}")
def run_task_3():
    menu()
if __name__ == "__main__":
        run_task_3()
