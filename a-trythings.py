import numpy as np

#A = np.array([[10, 20, 30],[40, 50, 60],[23, 23, 23]])

#b = np.array([1, 2, 3])


#C= A.sum(axis=0)
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])          # shape (2, 3)
B = np.array([
    [1, 4],
    [2, 5],
    [3, 6]
])          # shape (3, 2)
print(np.dot(A,B))

#Shape counts the rows and columns
#Size counts all the index
#Dot multiplies both the rows after addition
#ndim counts all the brackets