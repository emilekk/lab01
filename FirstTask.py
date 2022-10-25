import numpy as np
import matplotlib.pyplot as plt

n = int(input("Введите количество чисел Фибоначчи: "))+1
a = np.zeros(n-1)

a[0] = 1
a[1] = 1
a[2] = 2

i = int(3)
m = int(0)

while a[i-1] < n-1:
    a[i] = a[i-1]+a[i-2]
    i = i+1

for j in range(1, i):
    a[j] += m
    j += 1

for j in range(0, n-1):
    print(a[j]," ")

plt.plot(a)
plt.show()
