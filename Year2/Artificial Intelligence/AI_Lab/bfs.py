def bfs(G, start):
    frontier = [start]
    reached = {start}

    while frontier:
        current = frontier.pop(0)
        print(f"Visiting {current}")
        for neighbor, edge_w in G[current]:
            if neighbor not in reached:
                frontier.append(neighbor)
                reached.add(neighbor)

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

# Call the BFS function and print the visiting order
print("BFS Visiting Order:")
bfs(G, start_node)
