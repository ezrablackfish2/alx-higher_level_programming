#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    n = len(new)
    for i in range(n):
        if (new[i] == search):
            new[i] = replace
    return new
