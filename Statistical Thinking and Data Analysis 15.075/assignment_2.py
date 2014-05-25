# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:44:33 2013

@author: joshua
"""

import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
# 
# In this exercise, we demonstrat the Central Limit Theorem, where each X_i is
# exopential.
#
# a. Generate 100 random numbers from the expoential distribution where
# lambda=6. Plot them in a histogram. This should give you an idea of what the
# exponential distribution looks like.

exponential_pop = np.array([np.random.exponential(1/6.) for i in range(1000)])
# plt.hist(exponential_pop)

# b - e have been combined since they all go together in practice.
#
# b. For n = 2 generate a thousand n sized-samples from the previously cited 
# distribution.  Compute the sample mean of the n numbers and standardize it 
# using the true mean and standard deviation of the distribution. Repeat for 
# n = 10, 20, and 100. Put all four in plots.

true_mean = 1/6.
true_std = 1 / 6.**2

def standardize(number):
    return (number - true_mean) / true_std

for sample_size  in [10, 20, 100]:
    sample_means = []
    for i in range(1000):
        sample = [np.random.exponential(1/6.) for i in range(sample_size)]
        sample_avg = np.mean(sample)
        standardized_avg = standardize(sample_avg)
        sample_means.append(standardized_avg)
        
    plt.hist(sample_means)
