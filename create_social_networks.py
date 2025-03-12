def create_social_network(traders):
    '''
    Takes list of tuples of traders and their connection, this function takes
    those connections and sorts each traders possible connections in the
    network into a dictionary where the items are the traders and the 
    values is a list of all of that traders possible connections
    '''
    
    # extract all unique traders from "traders" sorted alphanumerically
    unique_traders = sorted(list(set([trader for connection in traders
                                      for trader in connection])))
    unique_traders_connections = []

    # iterate over all traders making lists of each adjacent trader connection
    for trader in unique_traders:
        temp_connections = []
        
        # save each traders connection to temp_connections to
        for connection in traders:
            '''check if first or second trader in connection is the current
            trader in the loop, if it is then add to temp_connections the other
            trader in the tuple because that is a connection of the current 
            trader'''
            if connection[0] == trader and connection[-1] != trader:
                temp_connections.append(connection[-1])
            elif connection[-1] == trader and connection[0] != trader:
                temp_connections.append(connection[0])
        
        # sort connections alphanumerically again and add to unique connections
        temp_connections_sorted = sorted(temp_connections)
        unique_traders_connections.append(temp_connections_sorted)

    return list(dict(zip(unique_traders, unique_traders_connections)).items())

#### TEST CODE ####
# traders1 = [('T1','T2'), ('T2', 'T5'), ('T3', 'T1'), ('T3', 'T5'), ('T3', 'T6')]
# print("Test 1 ", create_social_network(traders1))

# traders2 = [('T1', 'T5'), ('T2', 'T6'), ('T3', 'T7'), ('T4', 'T8'), ('T1', 'T6'), ('T2', 'T7'), ('T3', 'T8'), ('T4', 'T5'), ('T1', 'T7'), ('T2', 'T8'), ('T3', 'T5'), ('T4', 'T6')]
# print("Test 2 ", create_social_network(traders2))