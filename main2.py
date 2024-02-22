import random
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

def show_time():

    list1 = [random.random() for _ in range(1000000)]
    list2 = [random.random() for _ in range(1000000)]
    array1 = np.array(list1)
    array2 = np.array(list2)


    start_time = time.perf_counter()
    result_list = [list1[i] * list2[i] for i in range(len(list1))]
    end_time = time.perf_counter()
    print("Время выполнения перемножения списков:", end_time - start_time)

    start_time = time.perf_counter()
    result_array = np.multiply(array1, array2)
    end_time = time.perf_counter()
    print("Время выполнения перемножения массивов NumPy:", end_time - start_time)

##########################################

def histograms():

    data = pd.read_csv("data2.csv")
    plt.hist(data["ph"], bins=50, label="histogram for task 2", )
    plt.show()

################################


def plot3d():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x) * np.cos(x)
    z = np.sin(x) * np.cos(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot')
    plt.show()


if __name__ == "__main__":
    show_time()
    histograms()
    plot3d()