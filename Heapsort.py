import random
import timeit
import sys
sys.setrecursionlimit(1000900)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def Max_Heapify(A,N,i):
    l = left(i)
    r = right(i)
    if l< N and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r < N and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A,N,largest)

def Build_max_heap(A):
    N = len(A)
    for i in range(N//2-1,-1,-1):
        Max_Heapify(A,N,i)
    for i in range(N-1,0,-1):
        A[i],A[0] = A[0], A[i]
        Max_Heapify(A,i,0)

data = [random.randint(0, 5000) for x in range(random.randint(100000,1000000))]

start = timeit.default_timer()
Build_max_heap(data)
stop = timeit.default_timer()

print(f"Czas sortowania losowych liczb: {stop - start}")
start = timeit.default_timer()
Build_max_heap(data)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych liczb: {stop - start}")
data.reverse()
start = timeit.default_timer()
Build_max_heap(data)
stop = timeit.default_timer()

print(f"Czas sortowania posortowanych odwrotnie liczb: {stop - start}")
