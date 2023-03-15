#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score_x_weight = list(map(lambda tup: tup[0] * tup[1], my_list))
    weight = list(map(lambda tup: tup[1], my_list))

    total_score_x_weight = 0
    total_weight = 0

    index = 0
    for x in score_x_weight:
        total_score_x_weight = total_score_x_weight + x
        total_weight = total_weight + weight[index]
        index = index + 1
    return total_score_x_weight/total_weight
