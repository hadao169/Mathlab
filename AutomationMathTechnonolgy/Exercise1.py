import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import randint

# Exercise 1:
# 1) probability to get no 6 is 5/6
p1 = 1-pow((5/6),4)
# 2) Roll 2 times: probability to get one pair of 6s is 1/36 => probability to get no pair of 6s => 35/36
p2 = 1 - pow(35/36, 24)
print("Actual result: ")
print(round(p1,3))
print(round(p2,3))

# Testing:
N = 10000
case1 = 0
case2 = 0
x = math.comb(24,2)
for n in range(N):
  result1 = randint(1,7,4)
  result2= randint(1,7,(24,2))
  different_numbers1=np.unique(result1)
  different_numbers2=np.unique(result2)
  pair = 0
  if 6 in different_numbers1: #size = number of elements
    case1+=1
  pair = np.sum(np.all(result2 == 6, axis=1))
  if pair > 0:  # If there is at least one pair of 6s
        case2 += 1
print("Test simulation: ")
print(case1/N)
print(case2/N)