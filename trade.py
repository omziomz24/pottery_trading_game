from logic.shortest_roads import shortest_path

def trade(spatial_network, status_sorted, trader_locations,
          trader_network, max_dist_per_unit=3):
    '''
    Take information about locations, their supply/demand, traders and look at
    the location with the highest demand *most negative supply value*. Check if
    there is a trader at this location and if there is check for that traders 
    social network to trade in. If there are valid traders in the network with
    supply at their respective locations then trade with the friend with the 
    highest distance to pottery ratio. If no trades exist at this location
    keep on looking at the locations with higest demand until a trade is found
    '''
    
    for location_status in status_sorted:
        # note in the naming convention _h = "highest demand"
        location_h = location_status[0]
        location_h_demand = location_status[-1]

        # check if location even has demand if not then skip location
        if location_h_demand >= 0:
            continue

        trader_location_h_list = [trader for trader, location in
                                  list(trader_locations.items()) if
                                  location == location_h]
        
        # check if trader at location with highest demand if not skip location
        if not trader_location_h_list:
            continue

        # check if there is demand in market if not return no possible trade
        only_supply = [supply for location, supply in status_sorted if
                      supply < 0]
        if not only_supply:
            return (None, None, None)

        # assign consumer trader location and demand
        trader_location_h = trader_location_h_list[0]
        trader_location_h_connections = dict(trader_network).get(
                                                             trader_location_h)

        # check consumer trader has any connections if not then skip location
        if not trader_location_h_connections:
            continue

        # retrieve all traders connections and put them in tuples with location
        possible_trades_info = []
        for possible_trader in trader_location_h_connections:
            possible_trader_location = [location for trader, location in
                                        trader_locations.items() if
                                        trader == possible_trader][0]
            possible_trader_supply = [supply for location, supply in
                                      status_sorted if
                                      location == possible_trader_location][0]
            
            # add neighbour distance if inspected location has connection
            neighbour_check = [dist for location, dist in
                               trader_location_h_connections if
                              location == possible_trader_location]
            if neighbour_check:
                # if inspected location has trader connection its adjacent
                possible_trader_short_path = neighbour_check[0]
            else:
                # not adjacent so use shortest_path()
                possible_trader_short_path = shortest_path(
                    spatial_network, location_h, possible_trader_location,
                    None)[-1]

            possible_trades_info.append(
                (possible_trader, possible_trader_location,
                 possible_trader_supply, possible_trader_short_path))
            
            # checking each possible trade location has supply
            possible_trades_info = [info for info in possible_trades_info if
                                    info[2] > 0]
            # check distance is worth it for number of units available
            possible_trades_info = [info for info in possible_trades_info if
                                    info[3] <= max_dist_per_unit * info[2]]

            # if there is no possible trade in this group then go to the next
            if not possible_trades_info:
                continue
            
            # filter trades by highest distance to pottery supply ratio
            high_ratio_trade = sorted(possible_trades_info,
                                      key=lambda x: x[3] / x[2])[0]
            trade_amount = min(high_ratio_trade[2], abs(location_h_demand))
            
            return (high_ratio_trade[1], location_h, trade_amount)
    
    return (None, None, None)


#### TEST CODE ####
# spatial_network = [('L1', [('L4', 2), ('L3', 5), ('L5', 5)]), ('L2', [('L5', 1)]), ('L3', [('L1', 5)]), ('L4', [('L1', 2)]), ('L5', [('L2', 1), ('L1', 5)])]
# status = {'L1':30, 'L2':-20, 'L4':100, 'L3':-50, 'L5':-60}
# status_sorted = [('L5', -60), ('L3', -50), ('L2', -20), ('L1', 30), ('L4', 100)]
# trader_locations = {'T1': 'L1', 'T2': 'L2'}
# trader_network = [('T1', ['T2']), ('T2', ['T1'])]
# print("Test 1 ", trade(spatial_network, status_sorted, trader_locations, trader_network))
# print("Test 2 ", trade(spatial_network, status_sorted, trader_locations, trader_network, max_dist_per_unit=0.001))