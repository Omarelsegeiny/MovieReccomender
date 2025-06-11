# DataSet3.py - script to extract data from third party IMDb API and load into ADLS.
# Dataset/API Link: https://imdb-api.com/api

#%%
print("IMDb top 250 API ingestion")

import os
import csv
import pandas as pd
import requests
import json
#%%
#Open API with key
with open("IMDb_key.config") as f:
    IMDb_key=f.readline()

#%%
#Parameters:
request_params = {"api_key" : IMDb_key,
                  
                   }

api_response = requests.get(
    "https://imdb-api.com/en/API/Top250Movies/"+IMDb_key,
    params = request_params
)

print(api_response.content)
#%%
# Parse the result into a Pandas dataframe to save to a .csv file.
json_data = json.loads(api_response.content)

response_json = json_data['items']  
df = pd.DataFrame(response_json)

df.to_csv('Top250Movies.csv', index=False)
# %%

