#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    
    s1, s2 = 0, 0
    for i in my_list:
        s1 += i[0] * i[1]
        s2 += i[1]

    return (s1 / s2)
