from logic.trade_iteratively import trade_iteratively

spatial_network1 = [('L1', [('L4', 15), ('L2', 20)]), ('L2', [('L3', 10), ('L1', 20)]), ('L3', [('L2', 10)]), ('L4', [('L5', 5), ('L1', 15), ('L8', 20)]), ('L5', [('L4', 5), ('L6', 6), ('L8', 22)]), ('L6', [('L5', 6), ('L7', 20)]), ('L7', [('L6', 20)]), ('L8', [('L4', 20), ('L5', 22)])]
status1 = {'L1': 50, 'L2': -5, 'L4': -40, 'L3': 5, 'L5': 5, 'L8': 10, 'L6': 10, 'L7': -30}
trader_locations1 = {'T1': 'L1', 'T2': 'L3', 'T3': 'L4', 'T4': 'L8', 'T5': 'L7', 'T6': 'L5'}
trader_network1 = [('T1', ['T2', 'T3']), ('T2', ['T1', 'T5']), ('T3', ['T1', 'T5', 'T6']), ('T5', ['T2', 'T3']),('T6', ['T3'])]
print("Test 1 ", trade_iteratively(1, spatial_network1, status1, trader_locations1, trader_network1))

spatial_network2 = [('L1', [('L4', 15), ('L2', 20)]), ('L2', [('L3', 10), ('L1', 20)]), ('L3', [('L2', 10)]), ('L4', [('L5', 5), ('L1', 15), ('L8', 20)]), ('L5', [('L4', 5), ('L6', 6), ('L8', 22)]), ('L6', [('L5', 6), ('L7', 20)]), ('L7', [('L6', 20)]), ('L8', [('L4', 20), ('L5', 22)])]
status2 = {'L1': 50, 'L2': -5, 'L4': -40, 'L3': 5, 'L5': 5, 'L8': 10, 'L6': 10, 'L7': -30}
trader_locations2 = {'T1': 'L1', 'T2': 'L3', 'T3': 'L4', 'T4': 'L8', 'T5': 'L7', 'T6': 'L5'}
trader_network2 = [('T1', ['T2', 'T3']), ('T2', ['T1', 'T5']), ('T3', ['T1', 'T5', 'T6']), ('T5', ['T2', 'T3']),('T6', ['T3'])]
print("Test 2 ", trade_iteratively(None, spatial_network2, status2, trader_locations2, trader_network2))