import random
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

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



data = pd.read_csv("data2.csv")
plt.hist(data["ph"], bins=50, label="histogram for task 2")
plt.show()

