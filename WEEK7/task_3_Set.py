from operator import truediv


def observed_items() :
    observations = []
    for count in range (5):
        observations = input ("please enter an observations: ")
        observations.append (input())
    return observations


def remove_observations (observations) :
    removing = True
    while removing :
        print ("Do you wish to remove an observation? (yes/no)")
        response = input ()
        if response == "yes" :
            print ("please enter the  observation you wish to remove")
            observations = input ()
            observations.remove(observations)
        else :
            removing = False


def run_task3 () :
    observations = observed_items()
    remove_observations (observations)
    #populate set
    observations_set = set()
    for observations in observations:
        data = (observations, observations.count(observations))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"(data[0], observed {data[1]}, times")

run_task3()



