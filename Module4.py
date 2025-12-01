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
print("\n")
       
#Output:
"""
this 
is line
 1
"""
#
"""
with open("testing2.txt", "w") as File2:
    File2.write("This is line A")
    File2.write("\n This is line B")
"""
#Creating new file if non-existent*
"""
Output: 
This is line A
 This is line B
"""

Lines = ["This is 1\n", "This is 3\n", "This is 3\n"]
with open("testing2.txt", "w") as File2:

    for line in Lines:
        File2.write(line)

#Writing file with list into for loop

with open("testing2.txt", "a")as File2:

    File2.write("This is append")


#Copying existing file into a new file
with open("testing3.txt", "r") as readfile:
    with open("testing4.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)