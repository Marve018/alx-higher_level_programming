#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    uniq_set = set()

    for num in my_list:
        if num not in uniq_set:
            uniq_set.add(num)
            uniq_sum += num
    return uniq_sum
