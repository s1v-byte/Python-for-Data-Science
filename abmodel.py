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

#SLICING DATA

      Name  Age  Score
0    Alice   23     88
1      Bob   21     92
2  Charlie   25     79
"""    
import pandas as pd
xlsx_path = "File.xlsx" #XLSX file if may formula/code ung excel file
df = pd.read_excel(xlsx_path) # Read the Excel file into a DataFrame
# Rows 0 to 1
df_slice = df.iloc[2:3] #2 represents the columns first, 3 is the rows
print(df_slice,end="")
#Output: 2  Charlie   25     79

