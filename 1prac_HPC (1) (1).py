# Parallel BFS and DFS (HPC Practical - Python version)

from multiprocessing import Pool

# -------- Graph (Tree structure) --------
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

# -------- Function for parallel BFS --------
def get_children(node):
    return graph[node]

def parallel_bfs(start):
    visited = [start]
    queue = [start]

    print("Parallel BFS Traversal:")

    # Create pool only once (IMPORTANT)
    with Pool(2) as p:
        while queue:
            print(queue, end=" ")

            children = p.map(get_children, queue)

            next_nodes = []
            for group in children:
                for node in group:
                    if node not in visited:
                        visited.append(node)
                        next_nodes.append(node)

            queue = next_nodes
    print()


# -------- DFS (Sequential) --------
def dfs(node, visited):
    print(node, end=" ")
    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


# -------- Main --------
if __name__ == "__main__":
    # BFS
    parallel_bfs(0)

    # DFS
    print("DFS Traversal:")
    dfs(0, [])



'''
Output:
    python 1prac_HPC.py
    Parallel BFS Traversal:
        [0] [1, 2] [3, 4, 5] 
    DFS Traversal:
        0 1 3 4 2 5 

'''