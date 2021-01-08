#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list) - 1
    if (idx < 0 or idx > n):
        return (my_list)
    else:
        new = my_list[:]
        new[idx] = element
        return (new)
