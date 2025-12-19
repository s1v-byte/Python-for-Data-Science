import pandas as pd

dict1 = {
    "Team": ["Warriors", "D"],

    "Team1": ["Cleaveland", ""],
    "Points": [100,300]   # ← overwrites the earlier "Points"
}


df = pd.DataFrame(dict1)
print(df[0:2])


    #Successfully converted JSON into DataFrame, using json_normalize()
        #you use json_normalize() for JSON files with nested dictionaries,lists etc
        #json_normalize() is a pandas function that will flatten the JSON file and turns it into a tabular format
import pandas as pd
data = [
    {"team": "Warriors", "points": 110},
    {"team": "Raptors", "points": 105}
]
df1 = pd.DataFrame(data)


import json
import pandas as pd
with open("try.json") as file1:
    data = json.load(file1)

    #Finding how many columns in the json file:
df = pd.json_normalize(data, 
                       record_path="employees",
                       sep = "_")

print(df.columns)

    #Printing the meta from JSON file:
df = pd.json_normalize(
    data,
    record_path="employees",
    meta=["company", ["location", "city"], ["location", "state"]]
)
print(df)
