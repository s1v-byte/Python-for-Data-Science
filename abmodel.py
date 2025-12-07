"""
#Reading csv files using panda
    #Basic Read CSV File
import pandas 
csv_path = "File2.csv"
df = pandas.read_csv(csv_path)
print(df)

    #Basic Read XLSX FILE WITH INSERT
import pandas as pd
xlsx_path = "File.xlsx" #XLSX file if may formula/code ung excel file
df = pd.read_excel(xlsx_path) # Read the Excel file into a DataFrame
df.insert(2, "Occupation", ["Chef", "Police", "Doctor"]) # Insert new column (must match row count)
print("\n With Excel File: \n",df)

#Analyzing first 5 rows of the file:

import pandas as pd
csv_path = "File1.csv"
df = pd.read_csv(csv_path)
df.head() #analyzes the first 5 rows kasama column. Df means DataFrame. Method si head()
###################

#In dataframe, keys in dictionary serve as columns while values are rows.

#Example of local DataFrame:
import pandas as pd
data = {
    'Name': ['Jon', 'Dave', 'kirk', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Convert dictionary to DataFrame
df = pd.DataFrame(data)
df.insert(2, "Occupation", ["Chef", "Police", "Nurse", "Doctor"])
print(df)

    #inserting but with actual xlsx file:
import pandas as pd2
xlsx_path = "File.xlsx"

df = pd2.read_excel(xlsx_path)
df.insert(2, "Occupation", ["Chef", "Police", "Nurse"])
print("With Excel File:\n",df)
"""

        #SLICING ----> df.iloc
#Excel Data Reference:    
"""
#SLICING DATA
      Name  Age  Score  Gender     Job    Hair   Pet
0    Alice   23     88  Female  Doctor  Blonde   Dog
1      Bob   21     92    Male  Driver   Black   Cat
2  Charlie   25     79    Male  Police   Black  Fish
"""

"""
    #ROW SLICING - last index NOT included
import pandas as pd
xlsx_path = "File.xlsx" #XLSX file if may formula/code ung excel file
df = pd.read_excel(xlsx_path) # Read the Excel file into a DataFrame
# Rows 0 to 1
df_slice = df.iloc[0:6] #2 represents the start of row slicing, 3 is the last NOT included
print("\n--------------------------------")
print("Row slices:")
print(df_slice,"\n---------------------")
#Output: 2  Charlie   25     79

    #COLUMN SLICING - last index NOT included
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df.iloc[:, 1:2] #1 represents the start of columns slicing, 
#2 is the last but NOT included
print("\n Column slice:")
print(df_slice,"\n---------------------")

    #ROW + COLUMN SLICING - last index NOT included
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df.iloc[0:3, 3:7 ] #2:3 sliced rows of alice,bob. #2:3 slices the colummn Name and stops at Score(Not included)
print("\n BOTH slice:")
print(df_slice,"\n---------------------")


        #SLICING (LABELS) -----> df.loc

    #ROW + COLUMN - Label + Label   NO LOC
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df[["Name","Pet","Job"] ]
print("\n Label + Label:")
print(df_slice,"\n---------------------") 


    #ROW + COLUMN - Index + Label
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")

df_slice = df.loc[:, ["Pet", "Job", "Name"]]
print("\n Index + Label:")
print(df_slice,"\n---------------------") 

"""
"""
    #Try except no Column Found:
try:
    df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
    df_slice = df.loc[0:3, ["Name","Job","Pet","Ages"]]
    print("\n Index + Label:")
    print(df_slice,"\n---------------------") 
except KeyError as e:
    print("No Column were found")
    print("Details", e)

    
    

    # Filter
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
fil = df.filter(like="Score")      
print("\n Index + Labelers:")
print(fil,"\n---------------------") 
    
"""
"""

"""
    #CHANGE COLUMN NAME BUT NOT SAVED IN EXCEL only in DataFrame
import pandas as pd
xlsx_path = "File.xlsx" 
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df.columns = ["ID", "Name", "Age", "Subject", "Grade", "Dave", "Dave "]
df_slice = df[["Name","Dave","ID"] ]
print("\n Label + Label:")
print(df_slice,"\n---------------------") 

    #CHANGE COLUMN NAME BUT SAVED IN EXCEL
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df.columns = ["ID", "Name", "Age", "Subject", "Grade", "Dave", "ETS"]
df.to_excel("Try.xlsx", index=False) #index = False prevents the code from creating unnecessary index





#OTHERS:
    #For multiple sheets of excel file:
        #df = pd.read_excel("File.xlsx", sheet_name="Sheet1")


    #CONDITIONAL >
import pandas as pd
xlsx_path = "File.xlsx" 
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df[df["Age"] > 22]
print("\n Index + Label:")
print(df_slice,"\n---------------------") 