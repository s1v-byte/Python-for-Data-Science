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
print(df.mean())
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

