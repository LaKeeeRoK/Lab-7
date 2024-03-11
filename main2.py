###  Сибиряков Артемий R3137, 2 вариант, поток 1.2
import random
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation

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
    plt.xlabel("pH")
    plt.ylabel("Плотность")
    plt.title("Гистограмма")

    plt.show()
    
################################


def norm_histograms():
    data = pd.read_csv("data2.csv")
    plt.hist(data["ph"], bins=50, density=True, label="normalized histogram for task 2")
    plt.xlabel("pH")
    plt.ylabel("Плотность")
    plt.title("Нормированная гистограмма")

    plt.show()
    std_dev = data["ph"].std()
    print("Среднеквадратичное отклонение: ", std_dev)

###################################

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
    ax.set_title('y=sin(x)cos(x)\nz=sin(x)cos(x)')
    plt.show()

def sin_gif():
    x = np.linspace(-10, 10, 1000)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_xlim(-10, 10)
    ax.set_ylim(-1.5, 1.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Анимация функции y = sin(x)')

    line, = ax.plot([], [], lw=2)

    def animate(i):
        x_plot = x[:i]
        y_plot = np.sin(x_plot)
        line.set_data(x_plot, y_plot)
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=10, blit=True)

    writer = PillowWriter(fps=30)
    ani.save('sin_animation.gif', writer=writer)

if __name__ == "__main__":
    show_time()
    histograms()
    norm_histograms()
    plot3d()
    sin_gif()
