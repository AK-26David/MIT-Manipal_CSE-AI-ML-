import heapq

def heuristic(node, goal):
    # Define your heuristic function here (e.g., Euclidean distance, Manhattan distance)
    # For demonstration purposes, let's use the absolute difference of node and goal
    return abs(node - goal)

def astar(G, start, goal):
    frontier = [(0, start)]
    prev = {start: None}
    g_score = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for next_node, weight in G[current]:
            tentative_g_score = g_score[current] + weight

            if next_node not in g_score or tentative_g_score < g_score[next_node]:
                g_score[next_node] = tentative_g_score
                f_score = tentative_g_score + heuristic(next_node, goal)
                heapq.heappush(frontier, (f_score, next_node))
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

# Call the A* function and print the result
result_path = astar(G, start_node, goal_node)
print("A* Path:", result_path)
