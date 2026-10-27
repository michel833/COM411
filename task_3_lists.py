def directions():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps
def menu ():
    print("please select the direction:")
    dirs= directions()
    for index in range(len(dirs)):
        print (f"[index]: {{dirs[index]}}")
def run_task_3():
    menu()
if __name__ == "__main__":
        run_task_3()
