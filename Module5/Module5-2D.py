#2D ARRAY
"""
FACTS
1. 1D array → data in a line (like a single column)
2. 2D array → data in a table (like Excel / CSV)
3. Data analysts use 2D arrays because real data is tabular.
4. A 2D array is just a list of lists

----
1. A[row, column]
2. unlike lists, [:] <-- this dont print out all value
    it doesnt print anything and just selects it


CONCEPT
Row 0 →  [1  2  3]
Row 1 →  [4  5  6]
Row 2 →  [7  8  9]

| NumPy     | Pandas         |
| --------- | -------------- |
| 2D array  | DataFrame      |
| Rows      | Records        |
| Columns   | Variables      |
| `A[:, 1]` | `df['column']` |
| `A.shape` | `df.shape`     |

"""
import numpy as np

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]])
#Output: A[row, col]
    #A[1,:] <-- [3,4]
    #A[:,0] <-- [1,3,5]

#print(np.shape(A))


#2D SLICING
B = np.array([
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32]])
print(B[0:2, :])
# 0:2(Select rows 0-1) : (and print all columns)

print("Last column",B[1:3, 2]) # row 1-2 and column 2
print("NEG",B[-1,-1]) #Last row, Last column


#2D OPERATION
    #ADDITION
X = np.array([
    [1, 2],
    [3, 4]])
Y = np.array([
    [5, 10],
    [15, 20]])
sums = X + Y
#output: [[ 6 12] [18 24]]

    #MULTIPLICATION
X = np.array([
    [1, 2],
    [3, 4]])
Y = np.array([
    [5, 10],
    [15, 20]])
mul = X * Y
#output: [[ 5 20] [45 80]]

    #SCALAR
scalar = X * 2
#output:[[2 4] [6 8]]


    #MATRIX MULTIPLICATION
"""
RULE:
A.shape = (m, n)
B.shape = (n, p)
A @ B → shape (m, p)
ex. 
A.shape = (3, 4)
B.shape = (4, 2)
#output: (3,2)

- The @ operator is matrix multiplication
- Matrix multiplication requires another array (matrix or vector), not a scalar (A @ 2) 

#size counts all the index
#ndim counts all the rows and columns
#shape
"""
    # @ 
A = np.array([
    [1, 2], 
    [3, 4]])
B = np.array([
    [5, 6], 
    [7, 8]
    ])

C = A @ B
#Process:
#First Row, First Column | (1×5)+(2×7)=5+14=19
#First Row, Second Column | (1×6)+(2×8)=6+16=22
#Second Row, First Column | =(3×5)+(4×7)=15+28=43
#Second Row, Second Column | (3×6)+(4×8)=18+32=50

#Output: [19, 22], [43,50]

    #Scalar
A = np.array([[2,4], [6,3]])

B = A * 2
print(B)

#Boolean indexing
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])
AB = A[A > 50]
#Output: [60 70 80 90]

#Axis Awareness
"""
axis=0  ↓  (down)
axis=1  →  (across)
"""
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])

A.sum(axis=0)  # column-wise
#result: [120 150 180]
A.sum(axis=1)  # row-wise
#result: [60 150 240]


#Broadcasting in 2D
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])

A + np.array([1, 2, 3]) #Adds [1,2,3] at column "0,1,2"
#result: [[11 22 33] [40 52 63] [70 82 93]]

#RESHAPE
"""
Used constantly when:
cleaning data
preparing ML features
fixing CSV imports
"""
A = np.array([10, 20, 30,40, 50, 60,70, 80, 90])
b = A.reshape(3,3,3)
#output: [[10 20 30][40 50 60][70 80 90]]

#NDIM
