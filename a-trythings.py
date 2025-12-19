"""from ibm_watson import SpeechToTextV1
url_s2t ="https://www.assemblyai.com/dashboard/activation"
iam_apikey_s2t ="76d32f10b308471d8bfb28977b161010"
s2t = SpeechToTextV1(iam_apikey_s2t, url=url_s2t)"""

"""import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
r.status_code
r.text[0:100]
header=r.headers
print(r)"""

#Random User Generator API
    #Data is from randomuser (python library)
from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())


