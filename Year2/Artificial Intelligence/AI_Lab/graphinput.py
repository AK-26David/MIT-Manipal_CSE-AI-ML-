def input_graph():
    graph = {}

    vertices = int(input("Enter the number of vertices: "))

    for vertex in range(1, vertices + 1):
        neighbors = list(map(int, input(f"Enter neighbors for vertex {vertex} (space-separated): ").split()))
        graph[vertex] = neighbors

    return graph

def print_graph(graph):
    print("\nGraph:")
    for vertex, neighbors in graph.items():
        print(f"{vertex} -> {', '.join(map(str, neighbors))}")

if __name__ == "__main__":
    input_graph_data = input_graph()
    print_graph(input_graph_data)
