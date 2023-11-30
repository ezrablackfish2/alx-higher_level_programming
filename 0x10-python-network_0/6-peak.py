#!/usr/bin/python3
""" peak finder """

def find_peak(list_of_integers):
    i = 0
    maxim = None
    l = len(list_of_integers) - 1
    arr = list_of_integers
    
    while l > 0:
        if (arr[i]):
            if arr[i] > arr[i - 1]:
                maxim = arr[i]
            else:
                maxim = arr[i - 1]
        i = i + 1
        l = l - 1
    return maxim
