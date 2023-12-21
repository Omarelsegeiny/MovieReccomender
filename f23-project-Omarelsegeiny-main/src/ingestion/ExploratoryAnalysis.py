# Databricks notebook source
# MAGIC %md # Connect to Azure

# COMMAND ----------

# Set Spark context for the storage account and the base URI.
storage_end_point = "moviereccomenderstore.dfs.core.windows.net" 
my_scope = "Movie_Key_Secret"
my_key = "Movie-Secret"

spark.conf.set(
    "fs.azure.account.key." + storage_end_point,
    dbutils.secrets.get(scope=my_scope, key=my_key))

# Replace the container name (movie-reccomender-container) and storage account name (moviereccomenderstore) in the #uri.
uri = "abfss://movie-reccomender-container@moviereccomenderstore.dfs.core.windows.net/"

# COMMAND ----------

# MAGIC %md # Read files

# COMMAND ----------


top_df = spark.read.csv(uri+"Movies and Ratings/TopMovies.csv", header=True)

genre_df = spark.read.csv(uri+"Movies and Ratings/movies_genre.csv", header=True)

top_250_df = spark.read.csv(uri+"Movies and Ratings/Top250Movies.csv", header=True)

most_popular_df = spark.read.csv(uri+"Movies and Ratings/MostPopularMovies.csv", header=True)

# COMMAND ----------

display(top_df)
display(genre_df)
display(top_250_df)

most_popular_df = most_popular_df.withColumnRenamed('id', 'pop_id')
most_popular_df = most_popular_df.withColumnRenamed('rank', 'pop_rank')
most_popular_df = most_popular_df.withColumnRenamed('rankUpDown' , 'pop_rankUpDown')
most_popular_df = most_popular_df.withColumnRenamed('title', 'pop_title')
most_popular_df = most_popular_df.withColumnRenamed('fullTitle', 'pop_fullTitle')
most_popular_df = most_popular_df.withColumnRenamed('year', 'pop_year')
most_popular_df = most_popular_df.drop('image', 'crew')
# most_popular_df = most_popular_df.withColumnRenamed('imDbRating', 'pop_imDbRating')
# most_popular_df = most_popular_df.withColumnRenamed('imDbRatingCount', 'pop_imDbRatingCount')





display(most_popular_df)

# COMMAND ----------

# MAGIC %md #Display file info

# COMMAND ----------

print(top_df.dtypes)  
print('\n')

print("Total columns:  ", len(top_df.columns))
print("Total rows:  ", top_df.count())

# COMMAND ----------

print(genre_df.dtypes)  
print('\n')

print("Total columns:  ", len(genre_df.columns))
print("Total rows:  ", genre_df.count())

# COMMAND ----------

print(top_250_df.dtypes)  
print('\n')

print("Total columns:  ", len(top_250_df.columns))
print("Total rows:  ", top_250_df.count())

# COMMAND ----------

print(most_popular_df.dtypes)  
print('\n')

print("Total columns:  ", len(most_popular_df.columns))
print("Total rows:  ", most_popular_df.count())

# COMMAND ----------

# MAGIC %md #Display recency bias dataframe

# COMMAND ----------

recenency_df = top_df.join(top_df, on=most_popular_df.columns[6:7], how='inner')
recenency_df = recenency_df.drop('crew', 'id', 'image', 'title')

display(recenency_df)

# COMMAND ----------

recenency_df.coalesce(1).write.option('header',True).mode('overwrite').csv(uri+"Deliverables")
