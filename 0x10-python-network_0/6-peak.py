#!/usr/bin/python3
"""find peak of list"""
def find_peak(list_of_integers):
    """find peak value"""
    sort_data = sorted(list_of_integers, reverse=True)
    return (sort_data[0])
