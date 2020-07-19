import numpy as np


data = np.loadtxt('Graph2.txt', delimiter=',', dtype='Float64', skiprows=1)
readings = data[:,1]
mean = np.sum(readings)/len(readings)
print("mean: ",mean/len(readings))
print("stdev:", np.sqrt(np.sum(np.square(readings-mean))/(len(readings)))  )
print("count:", len(readings) )
print("np mean:", np.mean(readings))
print("np stdev:", np.std(readings)) 
