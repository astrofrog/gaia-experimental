# Fake data for now!

import numpy as np

N = 1e7
X = np.random.uniform(-180., 180, N)
Y = np.random.uniform(-90., 90, N)

def get_data_subset(xmin, xmax, ymin, ymax):
    keep = (X > xmin) & (X < xmax) & (Y > ymin) & (Y < ymax)
    print("Extracting {0} data points".format(np.sum(keep)))
    return X[keep], Y[keep]