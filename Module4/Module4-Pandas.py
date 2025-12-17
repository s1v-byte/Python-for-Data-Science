            #LOADING DATA WITH PANDA

#Reading csv files using panda

import pandas 
csv_path = "File.xlsx"
df = pandas.read_excel(csv_path)

#Finding Unique Characters:

    #in Columns:
import pandas as pd

df = pd.read_excel("ABC.xlsx", sheet_name="Sheet1")
df_slice = df["Name"].unique() 
print("\n Column slice:")
print(df_slice,"\n---------------------")

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
    #CONDITIONAL >
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df[df["Age"] > 22]
print(df_slice,"\n---------------------")

    #CONDITIONAL == 
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df.loc[df["Gender"] == "Male"]
print(df_slice,"\n---------------------")

        #CONDITIONAL == But print specifics only if MALE
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df.loc[df["Gender"] == "Male", ["Name", "Gender", "Job"]]
print(df_slice,"\n---------------------")
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

"""
    #CHANGE COLUMN NAME BUT SAVED IN EXCEL
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df.columns = ["ID", "Name", "Age", "Subject", "Grade", "Dave", "ETS"]
df.to_excel("Try.xlsx", index=False) #index = False prevents the code from creating unnecessary index
"""

#OTHERS:

    # Filter
import pandas as pd
df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
fil = df.filter(like="Score")      
print("\n Index + Labelers:")
print(fil,"\n---------------------") 

    #Try except no Column Found:
try:
    df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
    df_slice = df.loc[0:3, ["Name","Job","Pet","Ages"]]
    print("\n Index + Label:")
    print(df_slice,"\n---------------------") 
except KeyError as e:
    print("No Column were found")
    print("Details", e)

    #SAVING THE FILE
import pandas as pd
df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")
slice_loc = df.loc[1:3, ["Name", "Score"]]
slice_loc.to_excel("Book1.xlsx", sheet_name="Sheet2", index=False)

    #SAVING TO SAME FILE, BUT APPENDING NEW SHEET
import pandas as pd
df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")
slice_loc = df.loc[1:3, ["Name", "Score"]]
# Write slice to another sheet in the SAME file
with pd.ExcelWriter("Book1.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    slice_loc.to_excel(writer, sheet_name="Sheet2", index=False)   

    #EXPORTING
import pandas as pd
df = pd.read_excel("example_data.xlsx", sheet_name="Sheet1")

slice_rows = df[:3]
slice_columns = df[["Name", "Occupation"]]
filtered = df[df["Age"] > 25]
filtered_multi = df[(df["Age"] > 25) & (df["Score"] >= 85)]
slice_loc = df.loc[1:3, ["Name", "Score"]]
slice_iloc = df.iloc[0:4, 1:3]

    #to_excel() export file will only remain and OVERWRITES the rest of the contents
slice_rows.to_excel("output_first3.xlsx", index=False)
filtered.to_excel("output_filtered.xlsx", index=False)
slice_loc.to_excel("output_loc.xlsx",sheet_name="Name+Age", index=False) 

    #EXPORTING WITHOUT AFFECTING EXISTING SHEETS   
import pandas as pd
def process_and_append(input_file, output_file=None):
    # If no output file is given, overwrite the original (while keeping all sheets)
    output_file = output_file or input_file
    all_sheets = pd.read_excel(input_file, sheet_name=None)
    df = all_sheets["Sheet1"]

    slice_rows = df[:3]
    filtered = df[df["Age"] > 25]
    filtered_multi = df[(df["Age"] > 25) & (df["Score"] >= 85)]
    slice_loc = df.loc[1:3, ["Name", "Score"]]

    all_sheets["Slice_Rows_First3"] = slice_rows
    all_sheets["Filtered_Age>25"] = filtered
    all_sheets["Loc_Slice"] = slice_loc
    all_sheets["FILTERED MULTI"] = filtered_multi
    
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for sheet_name, sheet_df in all_sheets.items():
            sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Excel saved successfully to: {output_file}")
# If no file in the export. then it will overwrite the current file
process_and_append("example_data.xlsx","example_data_output.xlsx") 

