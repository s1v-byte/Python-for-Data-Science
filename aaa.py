import pandas as pd
try:
    df = pd.read_excel("File.xlsx", sheet_name="Sheet1")
    fil = df.loc[1:, ["Score", "Name", "Age"]] 
    print("\n Index + Labelers:")
    print(fil,"\n---------------------") 
except KeyError as e:
    print("No column", e)

"""
#SLICING DATA
      Name  Age  Score  Gender     Job    Hair   Pet
0    Alice   23     88  Female  Doctor  Blonde   Dog
1      Bob   21     92    Male  Driver   Black   Cat
2  Charlie   25     79    Male  Police   Black  Fish
"""

