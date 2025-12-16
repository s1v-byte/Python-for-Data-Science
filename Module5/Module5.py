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
#===============================================
#-----------------------------------------------
#===============================================


#Boolean Indexing:

a = np.array([3, 5, 2, 8, 20])
b = a [ a > 5]
#result: [8, 20]
#===============================================
#-----------------------------------------------
#===============================================


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
#===============================================
#-----------------------------------------------
#===============================================


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
#===============================================
#-----------------------------------------------
#===============================================

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


        #
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])          
B = np.array([
    [1, 4],
    [2, 5],
    [3, 6]
])
"""
Process:
A Row 1 * B Column 1 (1x1, 2x2, 3x3) = 1+4+9 = 14
A Row 1 * B Column 2 (1x4, 2x5, 3x6) = 4+10+18 = 32
A Row 2 * B Column 1 (4x1, 5x2, 6x3) = 4+10+18 = 32
A Row 2 * B Column 2 (4x4, 5x5, 6x6) = 16+25+36 = 77
"""

#Output: [[14, 32] [32,77]]
    # random append
y = [1,2]
z = []
for i in y:
    z.append(2*i)
#result: [2,4]
#===============================================
#-----------------------------------------------
#===============================================

#Boolean Filtering 
import numpy as np
arr = np.array([10, 25, 35, 45, 60, 75, 90])
filtered_arr = arr[arr < 50]
# Output: [10 25 35 45]

arr = np.array([10, 20, 30, 40, 50, 60])
mask = arr > 30
# Output: [False False False  True  True  True]
filtered_arr = arr[mask]
# Output: [40 50 60]
#===============================================
#-----------------------------------------------
#===============================================


#Adding constant value to a numpy Array aka, broadcasting
u = np.array([1,2,3,-1])
z = u+1 #1 is the constant value
#result: [2 3 4 0]
#===============================================
#-----------------------------------------------
#===============================================


    #DATA TYPE          
invin = np.array([3, 3.4, 4.5, 3.3])
cibler = type(invin)
#result: <class 'numpy.ndarray'> 
    #nd → N-dimensional (it can have 1D, 2D, 3D, or more dimensions)
    #array → a collection of values stored together

    #dtype
arr1 = np.array([1, 2, 3, 4, 5])
arr1.dtype
#result: int64

arr1 = np.array([1.3, 2.4, 3.5, 4.3, 5,1])
arr1.dtype
#result: float64
#===============================================
#-----------------------------------------------
#===============================================

#OTHERS:
    #SHAPE
        #1D Array:
arr = np.array([10, 20, 10])
arr.shape
#output: (3,)
        # 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2.shape  
# Output: (3, 3)
        # 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr3.shape  
# Output: (2, 2, 2) 
    #the third 2 is because of [3.4]],
    #if u read it in 2D array, it only have 2

    #SUM
arr = np.array([10, 20, 10])
np.sum(arr)
#output: 40

    #MEAN
arr = np.array([10, 20, 30, 40, 50, 60])
np.mean(arr)
#output: 35.0

    #MINIMUM
arr = np.array([10, 20, 30])
np.min(arr)
#output: 10

    #MAXIMUM
arr = np.array([10, 20, 30])
np.min(arr)
#output: 30

    #ARGMAX
arr = np.array([10, 20, 30])
np.min(arr) #finds the index of the max value data
#output: 2

    #SORT
arr = np.array([20, 10, 30])
np.min(arr) #finds the index of the max value data
#output: [20, 10, 30]

    #SIZE (Counts all the index)
arr1 = np.array([1, 2, 3, 4, 5])
arr1.size
#result: 5

    #NDIM (Counts the rank of the index)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
np.ndim(arr2)
#result: (2,) #2 is the number of []

    #PI
arr = np.array([1, 2, 3, 4, 5]) * np.pi
    # or:
pie = [arr * np.pi]
# Output: [ 3.14159265  6.28318531  9.42477796 12.56637061 15.70796327]

#===============================================
#-----------------------------------------------
#===============================================

            #2D ARRAY



