import matplotlib.pyplot as plt

def display_line (X_values, Y_values):
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot (X_values, Y_values)
    plt.show()



def run_task1() :
    X_values = [1,2,3,4,5]
    Y_values = [1,4,9,16,25]
    display_line(X_values, Y_values)

run_task1()