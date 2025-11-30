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
# Iterate through the lines

with open("testing.txt","r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

#Output:
"""
this 
is line
 1
"""
