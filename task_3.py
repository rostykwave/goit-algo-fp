import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest paths in a graph.
    
    Arguments:
    graph -- adjacency dictionary where keys are vertices, values are dictionaries of neighbors and edge weights
    start -- starting vertex
    
    Returns:
    distances -- dictionary of shortest distances from the starting vertex to all others
    previous -- dictionary of previous vertices for path reconstruction
    """
    # Initialize distances and previous vertices
    distances = {vertex: float('infinity') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    
    # Create a priority queue (binary heap)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Remove the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if the current distance is greater than the already found one
        if current_distance > distances[current_vertex]:
            continue
        
        # Check all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous

def get_path(previous, target):
    """
    Reconstructs the path from the starting vertex to the target vertex.
    
    Arguments:
    previous -- dictionary of previous vertices
    target -- target vertex
    
    Returns:
    path -- list of vertices forming the shortest path
    """
    path = []
    current = target
    
    # Move from the target vertex to the starting vertex
    while current is not None:
        path.append(current)
        current = previous[current]
    
    # Reverse the path to go from the starting vertex to the target vertex
    return path[::-1]

def main():
    # Create an example graph
    graph = {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'B': 2, 'C': 5, 'D': 1}
    }
    
    # Visualize the graph
    print("Graph:")
    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            print(f"{vertex} --({weight})--> {neighbor}")
    print()
    
    # Run Dijkstra's algorithm
    start_vertex = 'A'
    distances, previous = dijkstra(graph, start_vertex)
    
    # Output the results
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex in sorted(graph.keys()):
        if vertex != start_vertex:
            path = get_path(previous, vertex)
            print(f"To {vertex}: distance = {distances[vertex]}, path = {' -> '.join(path)}")

if __name__ == "__main__":
    main()
