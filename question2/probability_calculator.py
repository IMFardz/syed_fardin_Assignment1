#!/usr/local/bin/python
import pascals_triangle as pt
"""This script returns the probability of an event with probability p occuring
at least n times over t trials"""


def get_probability(t, n,  p):
    coefficient = pt.get_binomial_coefficient(t,n)
    return coefficient*p^{k}*(1-p)^{n - k}

def get_probability_atleast(t,n,p):
    counter = 0
    for i in range(n):
        counter += get_probability(t, i, p)
    return 1 - counter



if __name__=="__main__":
    pass
