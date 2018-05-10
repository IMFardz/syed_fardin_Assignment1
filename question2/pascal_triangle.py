#!/usr/local/bin/python
"""This python script contains the first routine, and outputs the first twenty
lines of Pascal's Triangle"""

import math as m

def get_binomial_coefficient(n, k):
    return m.factorial(n)/(m.factorial(k) * m.factorial(n - k))

if __name__ == "__main__":
    for i in range (20):
        for j in range (i+1):
            print (get_binomial_coefficient(i,j)),
        print

