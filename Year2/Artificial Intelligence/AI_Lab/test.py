def dfs(matrix,visited,vertex):
    visited[vertex]=1
    print(vertex)
    for i in range(len(matrix)):
        if matrix[vertex][i]==1 and visited[i]==0:
            dfs(matrix,visited,i)
            
def dfs_traversal(matrix):
    visited=[0 for _ in range(len(matrix))]
    for i in range(len(matrix)):
        if visited[i]==0:
            dfs(matrix,visited,i)