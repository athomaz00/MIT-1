# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:32:01 2013

@author: joshua
"""
import numpy as np
from scipy.stats import norm
from pylab import boxplot, hist

# Exercise 1
# Write a script that calculates the mean and median of a sample of 100 uniform
# random numbers between 0 and 2 and the percentage of points in the sample 
# that are greater than 1.

random_samples = [np.random.uniform(0, 2) for i in range(100)]

print "mean: ", np.mean(random_samples)
print "median: ", np.median(random_samples)
print "percent: ", len(filter(lambda x: x > 1, random_samples)) / 100.

# Exercise 2
# a) Generate a vector of 1000 random variables with mean 8 and variance 25.

random_vector = np.array([np.random.normal(8.0, 25.0) for i in range(1000)])

# b) Calculate how many elements are greater than or equal to nine.

all_nines = np.array([9] * 1000)
greater_thens = np.greater(random_vector, all_nines)
print "Greater then nine count: ", len(random_vector[greater_thens,])

# c) What is the sample mean and sample std for this vector

print "Sample mean: ", np.mean(random_vector)
print "Sample std: ", np.std(random_vector)

# d) What are the 25th and 75th percentiles

print "The quanitles are: ", np.percentile(random_vector, [25, 75])

# What are the 25th and 75th percentiles ofthe sample of the 100 normal random
# numbers generated in part(a)?

print "The other quanitles are: ", np.percentile(random_samples, [25, 75])

# Find cdf(0.789) and cdf(‐0.543). (Remember cdf is the cumulative density 
# function for the standard normal distribution.)

print "cdf(0.789)", norm.cdf(0.789)
print "cdf(-0.543)", norm.cdf(-0.543)

# Exercise 3
# a) Generate a vector of 1000 poisson variables with lambda=2.

poisson = np.array([np.random.poisson(lam=2.0) for i in range(1000)])

# b) Generate a box plot and a histogram from part a.
# boxplot(poisson)
# hist(poisson)

