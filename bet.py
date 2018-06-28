#!/usr/bin/env python


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
            returns.append(float("{0:.2f}".format(s * r * 1.0)))
        min_return = min(returns)
        min_win = (min_return - stake_cost) * 1.0
        if min_win >= possible_min_win:
            possible_min_win = min_win
            possible_min_win_rate = min_win / stake_cost
            possible_min_win_stakes = stakes
            possible_min_win_return = returns
    return possible_min_win_stakes, possible_min_win_return, possible_min_win


def find_best_roi(events,return_rates,Total_stake):
    if type(return_rates[0]) == list:
        rr = return_rates
    else:
        rr = [return_rates]
    for rs in rr:
        print("=start====================")
        s,r,w = find_best_rate(Total_stake,rs)
        if w <= 0:
            print("!! No way to win in these Odds: ", rs)
        else:
            print("For Opts:  " , events, "   Best ROT found for stake: ", Total_stake)
            print("with Odds: ", rs)
            print("!!Stakes:  ", s , ' may win: ' , float("{0:.2f}".format(w)), ' ROI: ', float("{0:.2f}".format(100*w/Total_stake)),'%')
            print("Bet Return: ", r)
        print("=end====================")

#-------------------------

Total_stake = 50
events = ['a_win1orwin2','draw/draw','b_win1orwin2'] # for display only
return_rates = [4.1,4.2,4.5]
find_best_roi(events,return_rates,Total_stake)
