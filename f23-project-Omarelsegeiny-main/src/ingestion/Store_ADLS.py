#Write .csv files to ADLS

#%%
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient

print("Imports complete")  
#%%

# Method to connect to a storage account with an account key.
def initialize_storage_account(storage_account_name, storage_account_key):
    
    try:  
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)


#%%
#Link to ADLS account
storage_account_name = "moviereccomenderstore"
with open("ADLS_Key.config") as f:
    storage_account_key=f.readline()

initialize_storage_account(storage_account_name, storage_account_key)

print(service_client)

#%%
# Create a container and a directory.
file_system_client = service_client.create_file_system(file_system="movie-reccomender-container")    

directory_client=file_system_client.create_directory("Movies and Ratings")


#%%

# Upload the TopMovies file into ADLS.
directory_client = file_system_client.get_directory_client("Movies and Ratings")
        
file_client = directory_client.create_file("TopMovies.csv")

TopMovies_file = open("SupplementaryInfo/IngestionAnalysis/TopMovies.csv",'r')

file_contents = TopMovies_file.read()

file_client.upload_data(file_contents, overwrite=True)
#%%
# Upload the movies_genre file into ADLS.
directory_client = file_system_client.get_directory_client("Movies and Ratings")
        
file_client = directory_client.create_file("movies_genre.csv")

TopMovies_file = open("SupplementaryInfo/IngestionAnalysis/movies_genre.csv",'r')

file_contents = TopMovies_file.read()

file_client.upload_data(file_contents, overwrite=True)
# %%
# Upload the Top250Movies file into ADLS.
directory_client = file_system_client.get_directory_client("Movies and Ratings")
        
file_client = directory_client.create_file("Top250Movies.csv")

TopMovies_file = open("SupplementaryInfo/IngestionAnalysis/Top250Movies.csv",'r')

file_contents = TopMovies_file.read()

file_client.upload_data(file_contents, overwrite=True)
# %%
# Upload the MostPopularMovies file into ADLS.
directory_client = file_system_client.get_directory_client("Movies and Ratings")
        
file_client = directory_client.create_file("MostPopularMovies.csv")

TopMovies_file = open("SupplementaryInfo/IngestionAnalysis/MostPopularMovies.csv",'r')

file_contents = TopMovies_file.read()

file_client.upload_data(file_contents, overwrite=True)
