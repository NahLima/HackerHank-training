
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    if N % 2 == 0:
        if N in list(range(2,6)):
            print("Not Weird")
        elif N in list(range(5,21)):
            print("Weird")
        else:
             print("Not Weird")
    else:
        print("Weird")
        
        
        
        
        
        
        
   