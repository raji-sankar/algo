import sys


def allocate(minimum_trade, increment, available_units, portfolio_order):
    total_order = sum(portfolio_order.values())
    min_trade =  minimum_trade/2
    allocation = {}
    if total_order <= available_units:
        allocation = portfolio_order
    else:
        i = -1
        portfolio_order_sorted_by_value = sorted(zip(portfolio_order.values(), portfolio_order.keys()))
        for portfolio in portfolio_order_sorted_by_value:
            i += 1
            total_order = sum([value[0] for value in portfolio_order_sorted_by_value[i:]])
            proportional_allocation = portfolio[0] * available_units /total_order
            allocated_amt = 0
            if proportional_allocation < min_trade:
                allocation[portfolio[1]] = 0
            else:
                if proportional_allocation >= minimum_trade:
                    if proportional_allocation >= portfolio[0]:
                        allocated_amt = portfolio[0]
                    else:
                        allocated_amt = tradeable_amount(proportional_allocation, minimum_trade, increment)
                    if allocated_amt > available_units:
                        allocated_amt = tradeable_amount(available_units, minimum_trade, increment)
                    remaining_amt = portfolio[0] - allocated_amt
                    if remaining_amt > 0 and remaining_amt < minimum_trade:
                        allocated_amt = 0
                    elif remaining_amt > 0 and remaining_amt != tradeable_amount(remaining_amt, minimum_trade, increment):
                        allocated_amt = 0

            allocation[portfolio[1]] = allocated_amt
            available_units = available_units - allocated_amt


    for portfolio in sorted(zip(allocation.keys(), allocation.values())):
            print '{0:s} {1:d}'.format(portfolio[0], portfolio[1])

def tradeable_amount(prop_alloc, minimum_trade, increment):
    n = (prop_alloc - minimum_trade)/increment
    if n == 0:
        return 0
    else:
        return minimum_trade + (increment*n)





t = int(raw_input().strip())
(minimum_trade, increment, available_units) =  map(int, raw_input().strip().split())
portfolio_order = {}
for i in xrange(t):
    line = raw_input().strip()
    portfolio_order[line.split()[0]] =  int(line.split()[-1])


allocate(minimum_trade, increment, available_units, portfolio_order)
