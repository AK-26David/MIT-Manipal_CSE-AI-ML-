def bfs(matrix, start):
    visited = [False] * len(matrix)
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            print(vertex)
            visited[vertex] = True

        for i in range(len(matrix)):
            if matrix[vertex][i] == 1 and not visited[i]:
                queue.append(i)

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

matrix = input_graph_adj_matrix()
print("Adjacency Matrix:")
for row in matrix:
    print(row)

bfs(matrix, 0)