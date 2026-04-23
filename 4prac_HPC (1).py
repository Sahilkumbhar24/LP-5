# HPC Practical: AI/ML Application using Parallel Computing
# Example: Parallel Linear Regression (finding slope)

from multiprocessing import Pool

# Function to compute partial sums
def partial_compute(data):
    sum_xy = 0
    sum_xx = 0

    for x, y in data:
        sum_xy += x * y
        sum_xx += x * x

    return (sum_xy, sum_xx)


def parallel_linear_regression(X, Y):
    # Combine data
    data = list(zip(X, Y))

    # Split into 2 parts
    mid = len(data)//2
    parts = [data[:mid], data[mid:]]

    # Parallel computation
    with Pool(2) as p:
        results = p.map(partial_compute, parts)

    # Combine results
    total_xy = sum(r[0] for r in results)
    total_xx = sum(r[1] for r in results)

    # Calculate slope (m)
    slope = total_xy / total_xx

    print("Slope (Model Parameter):", slope)


# -------- Main --------
if __name__ == "__main__":
    # Sample dataset (y = 2x)
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    parallel_linear_regression(X, Y)