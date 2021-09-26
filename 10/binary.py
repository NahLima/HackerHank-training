#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    count = 0
    while n:
        n &= n << 1  # bit a bit indo para a esquerda
        count += 1

    print(count)
