def sort_demand_supply(status):
    '''
    Takes a dictionary of each location and their supply and demand value. 
    Each locations is then sorted in an ascending manner according to their
    respective supply/demand value, returning a dictionary with this sorted
    arrangement
    '''
    
    # first sorts by alphanumeric location name
    status_sorted_names = {location: supplydemand for location, supplydemand
                           in sorted(status.items())}
    
    # second sorts by supply/demand value of each location
    status_sorted_final = {location: supplydemand for location, supplydemand
                           in sorted(status_sorted_names.items(), key=lambda
                           item: item[1])}
    
    return list(status_sorted_final.items())

#### TEST CODE ####
# status1 = {'L1':50, 'L2':-5, 'L4':-40, 'L3':5, 'L5':5, 'L8':10, 'L6':10, 'L7':-30}
# print("Test 1 ", sort_demand_supply(status1))

# status2 = {'L1':30, 'L2':-20, 'L4':100, 'L3':-50, 'L5':-60}
# print("Test 2 ", sort_demand_supply(status2))