def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task_2():
    num = likelihood_min_max()
    print(f"minimum likelihood of falling {num[0]}%")
    print(f"maximum likelihood of falling {num[1]}%")


if __name__ == "__main__":
    run_task_2()
