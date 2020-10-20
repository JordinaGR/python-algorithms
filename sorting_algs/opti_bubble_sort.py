#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def opti_bubble(data):

        n = len(data)
        update = True
        j = 0
        while (update==True and n > 1):
            update = False
            for i in range(len(data)-j -1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    update = True
                else:
                    i += 1
            n -= 1
            j += 1

        return data

print(opti_bubble([4, 2, 3, 1, 5, 2, 5, 6, 7, 3, 5, 7, 8, 4]))