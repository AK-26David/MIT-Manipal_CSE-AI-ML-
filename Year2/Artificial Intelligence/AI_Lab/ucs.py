import heapq

def input_weighted_graph():
    graph = {}

    vertices = int(input("Enter the number of vertices: "))

    for vertex in range(1, vertices + 1):
        neighbors = {}
        num_neighbors = int(input(f"Enter the number of neighbors for vertex {vertex}: "))
        
        for _ in range(num_neighbors):
            neighbor, cost = map(int, input(f"Enter neighbor and cost for vertex {vertex} (space-separated): ").split())
            neighbors[neighbor] = cost
        
        graph[vertex] = neighbors

    return graph

def uniform_cost_search(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current, path) = heapq.heappop(heap)

        if current not in visited:
            visited.add(current)
            path = path + [current]

            if current == goal:
                return path, cost

            for neighbor, neighbor_cost in graph[current].items():
                heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))

    return None

if __name__ == "__main__":
    input_graph_data = input_weighted_graph()

    start_vertex = int(input("Enter the start vertex: "))
    goal_vertex = int(input("Enter the goal vertex: "))

    result = uniform_cost_search(input_graph_data, start_vertex, goal_vertex)

    if result:
        path, cost = result
        print(f"\nUniform Cost Search Path from {start_vertex} to {goal_vertex}:")
        print(" -> ".join(map(str, path)))
        print(f"Total Cost: {cost}")
    else:
        print(f"\nNo path found from {start_vertex} to {goal_vertex}.")
