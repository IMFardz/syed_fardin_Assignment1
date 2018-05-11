#!/usr/local/bin/python
import random
import matplotlib.pyplot as plt
import numpy as np


def success(p):
    """Given a probability p, the chance of returning True is p and the
    the chance of returning False is (1 - p)"""
    num = random.random()
    return num <= p


def simulation(N, p):
    """For N trials with probability of success p, return
    the number of trials which are successful"""
    counter = 0
    for i in range (N):
        returned_true = success(p)
        if returned_true:
            counter += 1
    return counter


if __name__ == "__main__":
    p = float(input())
    print("N = 10:", simulation(10, p))
    print("N = 100:", simulation(100, p))
    print("N = 1000:", simulation(1000, p))
    x_axis = np.array([10, 100, 1000])
    y_axis = np.array([simulation(10, p), simulation(100, p), simulation(1000, p)])
    plt.figure(figsize=(6, 6))
    plt.clf()
    plt.plot(x_axis, y_axis)
    plt.show()



