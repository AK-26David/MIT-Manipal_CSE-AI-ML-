import heapq

def reconstruct_path(start, goal, prev):
    path = [goal]
    current = goal
    while current != start:
        current = prev[current]
        path.append(current)
    path.reverse()
    return path

def ucs(G, start, goal):
    frontier = [(0, start)]  # Priority queue with (cost, node) tuples
    prev = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        for next_node, weight in G[current]:
            new_cost = cost_so_far[current] + weight

            if next_node not in prev or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                heapq.heappush(frontier, (new_cost, next_node))
                prev[next_node] = current

    return reconstruct_path(start, goal, prev)

# Taking user input for the graph
G = {}
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge_info = input("Enter edge (node1 node2 weight): ").split()
    node1, node2, weight = map(int, edge_info)

    if node1 not in G:
        G[node1] = []
    if node2 not in G:
        G[node2] = []

    G[node1].append((node2, weight))
    G[node2].append((node1, weight))

start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

# Call the UCS function and print the result
result_path = ucs(G, start_node, goal_node)
print("UCS Path:", result_path)
