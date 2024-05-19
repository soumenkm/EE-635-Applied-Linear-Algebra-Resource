import numpy as np
import math

A = np.array([[66,5,0],[94,7,0],[121,8,1]])
b = np.array([-953,-1355,-1730])

c = np.dot(np.linalg.inv(A),b)
print(c)