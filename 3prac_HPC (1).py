# HPC Practical: Parallel Reduction (Min, Max, Sum, Average)

import multiprocessing

# Function to compute partial results
def partial_operations(data):
    return (sum(data), min(data), max(data))


def parallel_reduction(arr):
    # Split array into 2 parts (simple)
    mid = len(arr)//2
    parts = [arr[:mid], arr[mid:]]

    # Parallel processing
    with multiprocessing.Pool(2) as p:
        results = p.map(partial_operations, parts)

    # Combine results
    total_sum = sum(r[0] for r in results)
    minimum = min(r[1] for r in results)
    maximum = max(r[2] for r in results)
    average = total_sum / len(arr)

    # Output
    print("Array:", arr)
    print("Sum:", total_sum)
    print("Min:", minimum)
    print("Max:", maximum)
    print("Average:", average)


# -------- Main --------
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12]
    parallel_reduction(arr)





'''
Output :
    python 3prac_HPC.py
    Array: [2, 4, 6, 8, 10, 12]
    Sum: 42
    Min: 2
    Max: 12
    Average: 7.0
'''