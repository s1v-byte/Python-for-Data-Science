#Application Program Interface aka API
"""
Outline
- What is an API
- API Libraries
- Rest API
    - Rest and Response

ANALOGY:
API = a waiter between you and the kitchen
You = your Python code
Kitchen = complex software / database / website
Menu = API
Order = request
Food = response

| Term     | Meaning                              |
| -------- | ------------------------------------ |
| Client   | Your Python script                   |
| Resource | The data (games, users, sales, etc.) |
| Endpoint | The URL                              |
| Request  | What you ask                         |
| Response | What you get back                    |

FOCUS ON 2:
| Method | Meaning                   |
| ------ | ------------------------- |
| GET    | Get data                  |
| POST   | Send parameters / filters |

FACT
-Many APIs block you if you:
-Send too many requests (rate limits)
-Dont include headers (User-Agent, API Key)

#GOAL
- Work with REst APi
- turn json response into a python DataFrame
- automated data collection 

#FLOW
API (source)
   ↓
JSON
   ↓
Pandas DataFrame
   ↓
Cleaning
   ↓
Analysis
   ↓
Insights

"""
import pandas as pd

# Sample API

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
}
df = pd.DataFrame(data)
#The data in dict_ is pass onto Pandas API
# Display the first 3 rows
df.head(3)
#Default output for .head() is 5 columns/rows
"""
Output:
      Name  Age
0    Alice   24
1      Bob   27
2  Charlie   22
"""


#REST API
#REpresentational State Transfer (REST)
"""
- Api throught the internet
- Your program is the client and API is the webservice
Rules:
    - Communication
    - Input or Request
    - Output or Response
"""

#Sports Data are great for learning because endpoint is always changing
#To make a request for a specific team, we dont need to request a json file
    #All we need is an ID

"""
5 NBA API example (why this is powerful)
Why sports APIs are great for learning:
-Real-time data
-Clean structure
-Time-series friendly

What's happening under the hood:
-You pass a team ID
-API builds an HTTP request
-NBA.com responds
-Python turns it into a DataFrame
-You analyze + visualize

This is EXACTLY what analysts do at work
Replace NBA with:
-Sales
-Marketing
-Finance
-User behavior
-Same workflow.

-------

Must-know additions
-requests library (standard for APIs)
-Pagination (data comes in pages)
-Authentication (API keys, tokens)
-Rate limits
-Error handling (status_code != 200)
-Async requests (nice bonus)

Analyst-level mindset
-Dont just fetch data:
-Validate it
-Handle missing values
-Log failures
-Automate pulls
"""
#===============================================
#-----------------------------------------------
#===============================================

#API PART 2

#Random User Generator API
    #Data is from randomuser (python library)
from randomuser import RandomUser
import pandas as pd

"""r = RandomUser()
some_list = r.generate_users(10)
name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())"""

#Exercise#1

"""from randomuser import RandomUser
import pandas as pd
def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        user_dict = {
            "Name": user.get_full_name(),
            "Gender": user.get_gender(),
            "City": user.get_city(),
            "State": user.get_state(),
            "Email": user.get_email(),
            "DOB": user.get_dob(),
            "Picture": user.get_picture()
        }
        users.append(user_dict)
        print(user_dict)  # prints each appended record
    return pd.DataFrame(users)
df = get_users()
#print(df)"""""

#Another, more common way to use APIs, is through requests library. 
#The next lab, Requests and HTTP, will contain more information about requests.

import requests
import pandas as pd
url = "https://fruityvice.com/api/fruit/all"
response = requests.get(url, timeout=10)
response.raise_for_status()  # fails fast if network error
data = response.json()
df = pd.json_normalize(data)

cherry = df[df["name"] == "Cherry"]
print("Family:", cherry.iloc[0]["family"])
print("Genus:", cherry.iloc[0]["genus"])

#Other way to Call out Columns in API:
banana = df[df["name"] == "Banana"]
calories = banana.iloc[0]["nutritions.calories"]
print(f"Banana Calories: {calories}")

#Output: Family: Musaceae | Genus: Musa

   #Using Dataframe
import requests
import pandas as pd
# Fetch data from API
url = "https://fruityvice.com/api/fruit/all"
response = requests.get(url, timeout=10)
response.raise_for_status()
data = response.json()
df = pd.json_normalize(data)
slice_df = df.loc[1:4, ['name', 'family', 'genus']]

print(slice_df)
#===============================================
#-----------------------------------------------
#===============================================
"""
OUTLINE:
- API KEYS AND ENDPOINTS
- WATSON SPEECH TO TEXT
- WATSON TRANSLATE
"""
   #API THAT USES AI
#GOAL:
   #transcibing audio file using Watson Text to Speech API
   #Then translate the text to a new language using Watson Language-Translator API

#PROCESS:
#Transcribing Audio file into text
#In the API CALL, you will send a copy of the audio file, <-- This is called POST REQUEST
   #Then the API will send the text transcription of what the audio is saying <-- in the background, the API is making a GET REQUEST

#Translating the Text into new language
#We Then send the text we would like to translate into a second language to a second API
#The API will translate the text and send the translation back to you, 


"""
Before doing the outline, Quick review of API KEYS and endpoints <-- this will give u access to the API
- endpoint is the location of the service. its used to find the API on the Internet. just like web address
- Many API will charge you for each call 
"""