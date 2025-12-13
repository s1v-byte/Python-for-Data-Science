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
4. Numpy is the basis of pandas
5. Numpy is a library for scientific computing

-----------------------------------------
DIFFERENCE BETWEEN FUNCTIONS AND METHODS
- A function is like a stand-alone tool.
- A method is the same kind of tool, but it's attached to an object.

# Function
import numpy as np
result = np.dot(np.array([1, -1]), np.array([1, 1]))  

# Method
import numpy as np
vec1 = np.array([1, -1])
vec2 = np.array([1, 1])
result = vec1.dot(vec2)

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


            #1D ARRAY#
#CHANGING VALUES

    #USING INDEX
a = np.array([10, 20, 30])
a[1] = 99
#result : [10, 99, 30]


    #USING SLICING
a = np.array([10, 20, 30])
a [0:2] = [7,8]
#result : [7, 8, 30]

#Boolean Indexing:

a = np.array([3, 5, 2, 8, 20])
b = a [ a > 5]
#result: [8, 20]

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

    #LINESPACE
a = np.linspace(-2,4,num=5)
#process "-2" starting number | "2" is end | 5 is the total number
#result: [-2. -1.  0.  1.  2.]

    #SQUARE ROOT
a = np.array([1,4,9])
c = np.sqrt(a)
#result: [1. 2. 3.]

    #SQUARED ^2
w = np.array([0, 1, 2])
pe = np.square(w)

    #SIN COS
np.sin(np.array([0, np.pi/2, np.pi]))
#result: [0. 1. 0.]

#DOT PRODUCTION

u = np.array([1, 2]) 
v = np.array([3, 4])
r = np.dot(u, v) 
#process: 1*3 + 2*4 = 11 #this is vector math
#result: 11

    #Same purpose from above, but for loop. np.dot is still faster and efficient
u = ([1, 2]) 
v = ([3, 4])
z = []
for n, m in zip(u,v):
    z.append(n*m)
#process: 1*3 + 2*4
#result: [3,4]

        # ,
r = np.dot(np.array([1,-1]),np.array([1,1]))
#process: [1x-1] = -1. | [1x1] = 1 | 1 - 1 = 0
#result: 0

    # random append
y = [1,2]
z = []
for i in y:
    z.append(2*i)
#result: [2,4]


#Adding constant value to a numpy Array aka, broadcasting
u = np.array([1,2,3,-1])
z = u+1 #1 is the constant value
#result: [2 3 4 0]


#DATA TYPE
import numpy as np            
invin = np.array([3, 3.4, 4.5, 3.3])
cibler = type(invin)
#result: <class 'numpy.ndarray'> 
    #nd → N-dimensional (it can have 1D, 2D, 3D, or more dimensions)
    #array → a collection of values stored together
"""
Not required, but very useful functions:

.pi 
.sum()
.mean()
.min()
.max()
.argmax() (index of max)
.sort()
.size #count all the index
.ndim #represents the rank of the array, rank 1 is index 1
"""

            #2D ARRAY



