"""
In this lesson you will learn about:
Explain the use of the HTTP protocol using the Requests Library method
Describe how the URL Request Response HTTP protocol works
Learn to apply simple, open-source APIs
Perform basic webscraping using Python
Work with different file formats using Python
Explain the difference between APIs and REST APIs
Summarize how APIs receive and send information
"""

"""
FACTS:
1. Array starts at 0 and the END index it NOT INCLUDED
2. It does math on entire arrays at once, NO LOOPS NEEDED
3. Numpy is faster than pandas

"""

import numpy as np
#TYPES:
arr = np.array([1, 2, 3, 4]) #This is an array

mat = np.array([[1, 2], [3, 4]]) #D array

np.array([1, 2, 3])                # 1-D array
np.array([[1, 2], [3, 4]])         # 2-D array

np.zeros((3, 3))                   # 3x3 zeros
np.ones((2, 4))                    # 2x4 ones
np.full((2, 2), 5)                 # filled with 5

np.arange(0, 10, 2)                # [0,2,4,6,8]
np.linspace(0, 1, 5)               # 5 numbers 0→1


#CHANGING VALUES

    #USING INDEX
a = np.array([10, 20, 30])
a[1] = 99
#result : [10, 99, 30]

    #USING SLICING
a = np.array([10, 20, 30])
a [0:2] = [7,8]
#result : [7, 8, 30]


#Basic NumPy OPERATIONS:

    #Addition
x = np.array([1, 2, 3])
y = x + 5
#result : [6 7 8]

    #Addition between two arrays
u = np.array([1, 2])
v = np.array([3, 4])
sum = u + v
#result : [4 6]


#Universal Function (ufuncs)
    #
a = np.array([1,4,9])
c = np.sqrt(a)
#result: [1. 2. 3.]

    #
np.sin(np.array([0, np.pi/2, np.pi]))
#result: [0. 1. 0.]

w = np.array([0, 1, 2])
pe = np.square(w)
print(pe)