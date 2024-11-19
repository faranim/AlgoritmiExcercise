def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    # Prepare variables.
    # The only discovered vertex is the start vertex
    discovered = {start: None}
    # The only vertex in this level is the start vertex
    level = [start]
    while level:
        # Prepare a variable for the next level
        next_level = []
        # Iterate the vertices in this level
        for u in level:
            # Iterate the adjacents of this vertex
            for v in graph.get_adjacent_vertices(u):
                # If the adjacent is not yet in discovered
                if v not in discovered:
                    # Add the adjacent and the edge between them
                    discovered[v] = u
                    # Add also the adjacent to the next level
                    next_level.append(v)
        # When current level is exhausted, advance to the next level
        level = next_level
    return discovered