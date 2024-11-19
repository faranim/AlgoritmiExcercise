def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    """
    Calculate the shortest past (in distance value) between given vertices

    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question

    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    # Create a dict table with the discovered shortest distances and paths
    shortest_path_table = { vertex: {'shortest': float('inf'), 'previous': None } for vertex in graph.get_vertices()}
    # Initialize the source vertex path distance as 0.
    shortest_path_table[source_vertex]['shortest'] = 0
    # Get all vertices
    unvisited_vertices = { k: v['shortest'] for k,v in shortest_path_table.items() }

    # Loop while there are untested vertices
    while unvisited_vertices:
        # Get the vertex with the minimum path distance until now
        current_vertex = min(unvisited_vertices, key=unvisited_vertices.get)
        # Get its distance
        distance_from_source = shortest_path_table[current_vertex]['shortest']

        # Iterate over the adjacent vertices of this vertex that are still unvisited
        unvisited_adjacent_vertices = (v for v in graph.get_adjacent_vertices(current_vertex) if v in unvisited_vertices)
        for adjacent_vertex in unvisited_adjacent_vertices:
            # Get incident edge between the vertices (current and adjacent)
            edge = graph.get_edge(current_vertex, adjacent_vertex)
            # Calculate what would be the distance to adjacent vertex through this current vertex: Distance to current vertex + distance between these two vertice's (edge's value)
            tentative_distance = distance_from_source + edge.value()
            # If the tentative distance is shorter than the already calculated, update the table
            if tentative_distance < shortest_path_table[adjacent_vertex]['shortest']:
                shortest_path_table[adjacent_vertex]['shortest'] = tentative_distance
                shortest_path_table[adjacent_vertex]['previous'] = current_vertex
                unvisited_vertices[adjacent_vertex] = tentative_distance

        # Remove the current vertex from the list of available vertices (as it is now visited)
        del unvisited_vertices[current_vertex]

    # Retrieve the path (in reverse order)
    path = []
    current = destination_vertex
    while current:
        path.append(current)
        current = shortest_path_table[current]['previous']

    # Return shortest distance and minimum distance path from source vertex to destination vertex
    return (shortest_path_table[destination_vertex]['shortest'], path[::-1])