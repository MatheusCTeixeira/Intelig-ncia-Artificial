import math
import random

vector = [random.random() * 10000 for  i in range(0, 100) ].sort()

#[2, 4]
#inserir 3

def bissection(val, vec, cmp_less_func):
    left = 0
    right = len(vec) #2
    mid = 0
    
    while (left < right):
        mid = math.floor((left + right)/2)#1
        if (cmp_less_func(vec[mid], val) == True):#False
            right = mid
        else:
            left = mid #left = 1
    
    vec.insert(mid, val)

    return mid



