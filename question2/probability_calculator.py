#!/usr/local/bin/python
import pascal_triangle as pt


def get_probability(t, n, p):
    coefficient = pt.get_binomial_coefficient(t,n)
    return coefficient * (p**n)* ((1-p)**(t - n))


def get_probability_atleast(t, n, p):
    counter = 0
    for i in range(n):
        counter += get_probability(t, i, p)
    return 1 - counter


if __name__=="__main__":
    one_hit = get_probability_atleast(4, 1, 0.25)
    print("The probability of the batter getting at least one hit is:", one_hit)
