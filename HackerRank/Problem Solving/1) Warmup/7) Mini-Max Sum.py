#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = sum(arr)-max(arr)
    maxi = sum(arr)-min(arr)
    print("%d %d" % (mini, maxi))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
