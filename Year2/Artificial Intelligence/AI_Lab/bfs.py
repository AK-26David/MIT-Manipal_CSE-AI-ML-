def create_adj_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    return matrix

def input_graph_adj_matrix():
    n = int(input("Enter the number of vertices: "))
    matrix = create_adj_matrix(n)

    for i in range(n):
        print(f"Enter edges for vertex {i}:")
        edge_input = list(map(int, input().split()))
        for j in range(0, len(edge_input), 2):
            if j+1 < len(edge_input):
                matrix[i][edge_input[j]] = 1
                matrix[edge_input[j]][i] = 1

    return matrix

def bfs(matrix, visited, queue, vertex):
    visited[vertex] = 1
    queue.append(vertex)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        for i in range(len(matrix)):
            if matrix[current][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

def bfs_traversal(matrix):
    visited = [0 for _ in range(len(matrix))]
    queue = []

    for i in range(len(matrix)):
        if visited[i] == 0:
            bfs(matrix, visited, queue, i)
            
matrix = input_graph_adj_matrix()
print("Adjacency Matrix:")
for row in matrix:
    print(row)

bfs_traversal(matrix)

