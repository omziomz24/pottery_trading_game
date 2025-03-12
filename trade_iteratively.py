from logic.trade import trade
from logic.sort_demand_supply import sort_demand_supply

def trade_iteratively(num_iter, spatial_network, status, trader_locations,
                     trader_network, max_dist_per_unit=3):
    '''
    Take number of desired trades then information regarding trader location,
    location demand/supply, trader network and maximum distance a trader will
    travel per unit. Finds possible trades for the number of desired trades and
    given trades exist and hold under maximum distance per unit rule then the
    trade will occur and it will update the status of the locations and their 
    respective supply and demands. Note that if number of desired trades is
    'None' then the maximum number of possible trades for the locations given
    in 'status' wil' occur
    '''
    
    # assign trades to append successful trades to later
    trades = []
    # intialise count variable for while loop
    trade_count = 0
    # checker if same trade is being made then terminate while loop
    last_trade = None
    
    # trade until the num_iter is reached
    while num_iter is None or trade_count < num_iter:
        
        # sort status for trade() to function and update every loop
        status_sorted = sort_demand_supply(status)
        
        # Find the next trade to make
        trade_made = trade(spatial_network, status_sorted, trader_locations,
                           trader_network, max_dist_per_unit)
        
        # for the case if num_iter = None if the last trade made is the current
        # trade being made then it has reached the end of trades so it should
        # stop itself
        
        if trade_made == last_trade:
            break
        
        last_trade = trade_made
        
        # check if no possible trade if not then just break this loop
        if trade_made == (None, None, None):
            break
        
        # if there is trade then update status
        supplier_location, consumer_location, trade_amount = trade_made
        status[supplier_location] -= trade_amount
        status[consumer_location] += trade_amount
        
        # add new trade to list trades
        trades.append(trade_made)
        trade_count += 1
        
    # sort status by alphanumeric and by supply/demand
    final_supply_sorted = sorted(status.items(), key=lambda x: (x[1], x[0]))
    return (final_supply_sorted, trades)

#### TEST CODE ####
# spatial_network = [('L1', [('L4', 15), ('L2', 20)]), ('L2', [('L3', 10), ('L1', 20)]), ('L3', [('L2', 10)]), ('L4', [('L5', 5), ('L1', 15), ('L8', 20)]), ('L5', [('L4', 5), ('L6', 6), ('L8', 22)]), ('L6', [('L5', 6), ('L7', 20)]), ('L7', [('L6', 20)]), ('L8', [('L4', 20), ('L5', 22)])]
# status = {'L1': 50, 'L2': -5, 'L4': -40, 'L3': 5, 'L5': 5, 'L8': 10, 'L6': 10, 'L7': -30}
# trader_locations = {'T1': 'L1', 'T2': 'L3', 'T3': 'L4', 'T4': 'L8', 'T5': 'L7', 'T6': 'L5'}
# trader_network = [('T1', ['T2', 'T3']), ('T2', ['T1', 'T5']), ('T3', ['T1', 'T5', 'T6']), ('T5', ['T2', 'T3']),('T6', ['T3'])]
# print("Test 1 ", trade_iteratively(1, spatial_network, status, trader_locations, trader_network))
# print("Test 2 ", trade_iteratively(None, spatial_network, status, trader_locations, trader_network))