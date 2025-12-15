import numpy as np

"""A = np.array([
  [1, 2, 3],
  [4, 5, 6]
]) 


b = A *2
"""
A = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

C = A @ 2
print(C)