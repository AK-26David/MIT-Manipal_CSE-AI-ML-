import heapq
def astar(heuristic,matrix,start,end):
    queue=[(heuristic(start,end),(0,start))]
    visited=set()
    while queue:
        (cost,vertex)=heapq.heappop(queue)
        if vertex==0:
            return cost
        if vertex not in visited:
            continue
        visited.add(vertex)
        for i in range(len(matrix)):
            if matrix[vertex][i]==0 and vertex not in visited:
                heapq.heappush(queue,cost+matrix[vertex][i],heuristic(i,end),i)
                return False