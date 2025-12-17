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

