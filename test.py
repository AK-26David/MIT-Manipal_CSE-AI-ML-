def input_graph():
    graph = {}

    vertices = int(input("Enter the number of vertices: "))

    for vertex in range(1, vertices + 1):
        neighbors = list(map(int, input(f"Enter neighbors for vertex {vertex} (space-separated): ").split()))
        graph[vertex] = neighbors

    return graph

if __name__ == "__main__":
    input_graph_data = input_graph()

    start_vertex = int(input("Enter the start vertex for DFS: "))

    visited_vertices = set()