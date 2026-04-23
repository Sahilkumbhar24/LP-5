# HPC Practical: Parallel Bubble Sort & Merge Sort with Performance

import multiprocessing
import time
import random

# -------- Bubble Sort (Sequential) --------
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# -------- Parallel Bubble Sort --------
def parallel_bubble(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    with multiprocessing.Pool(2) as p:
        left, right = p.map(bubble_sort, [left, right])

    return sorted(left + right)


# -------- Merge Sort (Sequential) --------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)


# -------- Parallel Merge Sort --------
def parallel_merge(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    with multiprocessing.Pool(2) as p:
        left, right = p.map(merge_sort, [left, right])

    return sorted(left + right)


# -------- Main --------
if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(5000)]

    # Sequential Bubble
    start = time.time()
    bubble_sort(arr.copy())
    print("Sequential Bubble Time:", time.time() - start)

    # Parallel Bubble
    start = time.time()
    parallel_bubble(arr.copy())
    print("Parallel Bubble Time:", time.time() - start)

    # Sequential Merge
    start = time.time()
    merge_sort(arr.copy())
    print("Sequential Merge Time:", time.time() - start)

    # Parallel Merge
    start = time.time()
    parallel_merge(arr.copy())
    print("Parallel Merge Time:", time.time() - start)




'''
Output : 
    python 2prac_HPC.py
    Sequential Bubble Time: 1.8568294048309326
    Parallel Bubble Time: 0.6362156867980957
    Sequential Merge Time: 0.004082918167114258
    Parallel Merge Time: 0.11247920989990234
'''