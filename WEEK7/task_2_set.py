def observed_items () :
    observations= []
    for count in range (7) :
        item = input("please enter an observation: ")
        observations.append (input())
    return observations


def run_task2 () :
    print (" counting observations...")
    observations = observed_items()
    observations_set = set ()
    for observations in observations :
        data = (observations, observations.count(observations))
        observations_set.add(data)

    for data in observations_set :
        print (f"(data[0], observed {data[1]}, times")


run_task2()