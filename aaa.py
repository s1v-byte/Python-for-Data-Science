import pandas as pd
    #CONDITIONAL >

df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
df_slice = df[df["Age"] > 22]
print("\n Index + Label:")
print(df_slice,"\n---------------------") 


"""
#SLICING DATA
      Name  Age  Score  Gender     Job    Hair   Pet
0    Alice   23     88  Female  Doctor  Blonde   Dog
1      Bob   21     92    Male  Driver   Black   Cat
2  Charlie   25     79    Male  Police   Black  Fish
"""

