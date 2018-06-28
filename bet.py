#!/usr/bin/env python

Total_stake = 100
# display only
events = ['a_win1orwin2','draw/draw','b_win1orwin2']
#return_rates = [[4.35,5.50,1.80],[2.55,5.00,2.80],[2.60,4.50,2.95],[4.30,6.00,1.80]]
return_rates = [[4.1,4.2,4.5,4]]

def split_number(n,amount):
    list_of_tuples = []
    if n == 1:
        return [(amount,)]
    elif n > 1:
        this_layer_amount = []
        new_n = n - 1
        for a in range(1 , amount):
            new_amount = amount - a
            if new_amount > 0 and a > 0 and new_amount >= new_n:
                next_layer_ts = split_number(new_n,new_amount)
                for next_t in next_layer_ts:
                    t = (a,) + next_t
                    this_layer_amount.append(t)
        return this_layer_amount


def find_best_rate(Total_stake,return_rates):
    #stake_range is the relative thing
    stake_range = range(1,Total_stake)
    possible_min_win = 0
    possible_min_win_rate = 0.0
    possible_min_win_stakes = []
    possible_min_win_return = []
    n = len(return_rates)
    all_combinations = split_number(n,Total_stake)

    for s_combination in all_combinations:
        stakes = list(s_combination)
        stake_cost = sum(stakes)
        returns = []
        for s,r in zip(stakes,return_rates):
            returns.append(s*r*1.0)
        min_return = min(returns)
        min_win = (min_return - stake_cost) * 1.0
        if min_win >= possible_min_win:
            possible_min_win = min_win
            possible_min_win_rate = min_win / stake_cost
            possible_min_win_stakes = stakes
            possible_min_win_return = min_return
    return possible_min_win_stakes, returns, possible_min_win

for rs in return_rates:
    print "====================="
    s,r,w = find_best_rate(Total_stake,rs)
    if w <= 0:
        print "!! no way to win in this rates: ", rs
    else:
        print events, "   Best rate found, with total stake: ", Total_stake
        print " odds  ", rs
        print "stakes ", s , '   possible_min_win--->' , w , ' rate: ', (100*w/Total_stake),'%'
        print 'return ', r
