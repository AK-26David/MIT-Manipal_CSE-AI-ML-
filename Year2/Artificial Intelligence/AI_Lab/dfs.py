def input_graph():
    graph = {}

    vertices = int(input("Enter the number of vertices: "))

    for vertex in range(1, vertices + 1):
        neighbors = list(map(int, input(f"Enter neighbors for vertex {vertex} (space-separated): ").split()))
        graph[vertex] = neighbors

    return graph

def dfs(graph, current, visited):
    if current not in visited:
        print(current, end=" ")
        visited.add(current)

        for neighbor in graph[current]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    input_graph_data = input_graph()

    start_vertex = int(input("Enter the start vertex for DFS: "))

    visited_vertices = set()
    print("\nDepth-First Search:")
    dfs(input_graph_data, start_vertex, visited_vertices)
