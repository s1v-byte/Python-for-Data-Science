"""
Learning Objectives
In this lesson you will learn about:
Reading files with open
Writing files with open
Loading data with Pandas
Working with and Saving data with Pandas
"""

#Reading Files with Open

#Printing but index are continuing when called again 
"""
text file:
this is line 1
line 2 
line 3
"""
with open("testing.txt", "r") as File1:
    
    file_stuff = File1.readline(5)
    type(file_stuff)
   

#Output:
"""
this 
is line
 1
"""
