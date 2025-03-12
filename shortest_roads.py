def shortest_path(spatial_network, source, target, max_bound):
    '''
    Takes information from the network of locations and their supply/demand,
    the starting location and the expected finishing location and the maximum
    distance that would want to be travelled. Then looks through each neighbour 
    node and repeats that process from the intial location until the source
    location is found. All of the possible paths are saved then only the path
    with the shortest distance is returned given it is in the maximum distance.
    In the case there is 2 paths from the intial location to the final with the
    same shortest distance the path withthe most locations along the way is 
    chosen
    '''
    
    # changes variables to a data structure which is easier to work with
    spatial_network = dict(spatial_network)
    distances = {node: float('inf') for node in spatial_network}
    distances[source] = 0
    
    # initalise variables to check later about locations that have been checked
    nodes_reached = []
    paths = {node: [] for node in spatial_network}
    paths[source] = [(source, 0)]
    

    # will run until every possible location has been checked for a path
    while nodes_reached != spatial_network:
        # retrieves all possible locations in the network
        network_nodes = [node for node in spatial_network]
        # if source not in network there is no shortest path from it
        if source not in network_nodes:
            return (None, None)
        # if target not in network there is not shortest path to it
        if target not in network_nodes:
            return (None, None)
        
        current_node = min([node for node in spatial_network
                           if node not in nodes_reached],
                           key=lambda node: distances[node])
        nodes_reached.append(current_node)

        for neighbour_node, distance in spatial_network[current_node]:
            new_distance = distances[current_node] + distance
            
            # update shortest path if new shortest is found
            if new_distance <= distances[neighbour_node]:
                distances[neighbour_node] = new_distance
                new_path = list(paths[current_node])
                new_path.append((neighbour_node, new_distance))
                
                # only add path if its alpanumerically smaller in tie
                if neighbour_node in paths and paths[neighbour_node]:
                    paths[neighbour_node] = min(
                        paths[neighbour_node], new_path)
                else:
                    paths[neighbour_node] = new_path
        
        # if we found the target location break the loop and start backtracking
        if current_node == target:
            break
    
    # if any paths were actually saved on way to the target
    if paths[target]:
        shortest_distance = paths[target][-1][1]
        shortest_paths = [path for path in paths.values()
                          if (path and path[-1][1] == shortest_distance)]
        
        # in case shortest path is tie sort by path with most locations passed
        longest_path_length = max([len(path) for path in shortest_paths])
        longest_paths = [path for path in shortest_paths
                         if len(path) == longest_path_length]
        
        # creating path string and distance for return statement
        path_string_nodes = []
        for path in longest_paths:
            for node_tuple in path:
                path_string_nodes.append(str(node_tuple[0]))
        distance = longest_paths[-1][-1][-1]
        
        # checking if max_bound dist gone over, no shortest path if this occurs
        if max_bound or max_bound == 0:
            # if source and target location is the same return with distance 0
            if len(path_string_nodes) == 1:
                return (path_string_nodes[0], 0)
            if distance > max_bound:
                return (None, None)
        
        return ("-".join(path_string_nodes), distance)
    else:
        return (None, None)
    
#### TEST CODE ####
# spatial_network = [('L1', [('L4', 15), ('L2', 20)]), ('L2', [('L3', 10), ('L1', 20)]), ('L3', [('L2', 10)]), ('L4', [('L5', 5), ('L1', 15), ('L8', 20)]), ('L5', [('L4', 5), ('L6', 6), ('L8', 22)]), ('L6', [('L5', 6), ('L7', 20)]), ('L7', [('L6', 20)]), ('L8', [('L4', 20), ('L5', 22)])]
# print(shortest_path(spatial_network, 'L1', 'L3', 50))
# print(shortest_path(spatial_network, 'L1', 'L3', 0))
# print(shortest_path(spatial_network, 'L1', 'L3', 10))
# print(shortest_path(spatial_network, 'L1', 'L3', None))