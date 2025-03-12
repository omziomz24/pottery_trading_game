def create_spatial_network(itineraries):
    '''
    Takes a list of tuples (L#1, L#2, distance) and returns a dictionary
    associating each possible location to a list of tuples each of their
    adjacent locations in the network and the distance between the original
    location and the adjacent location
    '''
    
    # list sorted alphanumerically of all of the possible locations
    unique_locations = sorted(list(set([location for location_tuple in
                                        itineraries for location in
                                        location_tuple if
                                        ((isinstance(location, str) and not
                                          location.isnumeric()) or (not
                                         isinstance(location, int)))])))
    unique_locations_connection_and_distance = []

    # assign each location a tuple with distance from another adjacent location
    for location in unique_locations:
        temp_locations_connection_and_distance = []
        for location_tuple in itineraries:
            if location in location_tuple:
                adjacent_location_and_distance = tuple(value for value in
                                                       location_tuple if
                                                       value != location)
                temp_locations_connection_and_distance.append(
                    adjacent_location_and_distance)
                
        # firstly, sorts connections alphanumerically
        temp_locations_connection_sorted_alphanumeric = sorted(
            temp_locations_connection_and_distance, key=lambda x: x[0])
        # secondly, sorts connections by distance in ascending order
        temp_locations_connection_and_distance_sorted = sorted(
            temp_locations_connection_sorted_alphanumeric, key=lambda x: x[1])
        unique_locations_connection_and_distance.append(
            temp_locations_connection_and_distance_sorted)

    return list(dict(zip(
        unique_locations, unique_locations_connection_and_distance)).items())

#### TEST CODE ####
# itineraries1 = [('L1', 'L2', 20), ('L2', 'L3', 10), ('L1', 'L4', 15), ('L4', 'L5', 5), ('L4', 'L8', 20), ('L5', 'L8', 22), ('L5', 'L6', 6), ('L6', 'L7', 20)]
# print("Test 1 ", create_spatial_network(itineraries1))

# itineraries2 = [('L4', 'L1', 2), ('L3', 'L1', 5), ('L1', 'L5', 5), ('L2', 'L5', 1)]
# print("Test 2 ", create_spatial_network(itineraries2))
