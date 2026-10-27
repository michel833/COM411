def steps():
    likelihoods = [("step1", 50),("step2, 38"), ("step3", 27),("step4", 99),("step5",4)]
    return likelihoods


def run_task_3():
    likelihoods = steps()
    good_steps = []
    bad_steps = []
    for step in likelihoods:
        if step[1] >= 50:
            bad_steps.append(likelihoods)
        else:
            good_steps.append(likelihoods)
            print(f"good_steps:{len(good_steps)}, bad_steps{len(bad_steps)}")


if __name__ == "__main__":
    run_task_3()


