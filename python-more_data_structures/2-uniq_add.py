#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for n in my_list:
        if n not in unique:
            unique.append(n)
            total += n
    return total
