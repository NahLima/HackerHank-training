import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []
    result = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(1, 5):
        for j in range(1, 5):
            soma = sum(arr[i-1][j-1: j+2] + arr[i+1][j-1: j+2]) + arr[i][j]
            result.append(soma)

    print(max(result))


'''
input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''

'''
max =19
'''
