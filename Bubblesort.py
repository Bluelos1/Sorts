import random
import timeit
import sys

sys.setrecursionlimit(1000900)


def bubbleSort(A):
    n = len(A)

    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


data = [random.randint(0, 5000) for x in range(random.randint(10000, 100000))]

start = timeit.default_timer()
bubbleSort(data)
stop = timeit.default_timer()

print(f"Czas sortowania losowych liczb: {stop - start}")
start = timeit.default_timer()
bubbleSort(data)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych liczb: {stop - start}")
data.reverse()
start = timeit.default_timer()
bubbleSort(data)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych odwrotnie liczb: {stop - start}")

