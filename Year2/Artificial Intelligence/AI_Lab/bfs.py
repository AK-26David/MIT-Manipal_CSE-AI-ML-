def input_graph():
    graph = {}

    vertices = int(input("Enter the number of vertices: "))

    for vertex in range(1, vertices + 1):
        neighbors = list(map(int, input(f"Enter neighbors for vertex {vertex} (space-separated): ").split()))
        graph[vertex] = neighbors

    return graph

def breadth_first_search(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)

        if current not in visited:
            visited.add(current)

            if current == goal:
                return path

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    input_graph_data = input_graph()

    start_vertex = int(input("Enter the start vertex: "))
    goal_vertex = int(input("Enter the goal vertex: "))

    result_path = breadth_first_search(input_graph_data, start_vertex, goal_vertex)

    if result_path:
        print(f"\nBreadth-First Search Path from {start_vertex} to {goal_vertex}:")
        print(" -> ".join(map(str, result_path)))
    else:
        print(f"\nNo path found from {start_vertex} to {goal_vertex}.")
