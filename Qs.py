import random
import timeit
import sys
sys.setrecursionlimit(1000900)


def Partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller += 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller


def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)


data = [random.randint(0, 1000) for x in range(random.randint(100000,1000000))]

start = timeit.default_timer()
Quicksort(data, 0, len(data) - 1)
stop = timeit.default_timer()

print(f"Czas sortowania losowych liczb: {stop - start}")
start = timeit.default_timer()
Quicksort(data, 0, len(data) - 1)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych liczb: {stop - start}")
data.reverse()
start = timeit.default_timer()
Quicksort(data, 0, len(data) - 1)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych odwrotnie liczb: {stop - start}")
