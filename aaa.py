    # Filter
import pandas as pd
xlsx_path = "File.xlsx" 
df = pd.read_excel(xlsx_path) 
fil = df.filter(like="Score")      
print("\n Index + Labelers:")
print(fil,"\n---------------------") 