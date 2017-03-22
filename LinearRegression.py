import os
import csv
import numpy as np

def readData(filename):
    result = []
    f = open(filename)
    f_csv = csv.DictReader(f)

    for row in f_csv:
        result.append([row['sqft_living'], row['price']])
    return result    

def linearFun(x, theta):
    return np.dot(x, theta)

def GradientDescent(x, t, theta):
    for i in range(0, len(theta)):
        y = linearFun(x, theta)

