def likelihood():
    likelihoods = (50,38,27, 99, 4)
    return  min(likelihoods)
def run_task_1():
    num = likelihood()
    print(f"minimum likelihood of falling: {num}%")
if __name__ == "__main__":
   run_task_1()