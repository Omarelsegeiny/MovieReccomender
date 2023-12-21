# DataSet1.py - script to extract data from Kaggle and load into ADLS.
# Dataset Link - https://www.kaggle.com/datasets/khushipitroda/movie-genre-detection/data


#%%

print("DataSet1 ingestion - Kaggle")

#Import Statements
from kaggle.api.kaggle_api_extended import KaggleApi
import kaggle
import pandas as pd
import os

#%%

# Authentication defaults
api = KaggleApi()
api.authenticate()

#%%
#Get and download the Kaggle Movie Info dataset as a .csv file

movie_data_set = 'khushipitroda/movie-genre-detection'
outpath = 'SupplementaryInfo/IngestionAnalysis/'

api.dataset_download_files(movie_data_set, 'movie_genre_data.csv', outpath, unzip=True)

# %%
