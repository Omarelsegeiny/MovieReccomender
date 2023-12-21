[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12482756&assignment_repo_type=AssignmentRepo)
# CSCI 422 Project - Omar Elsegeiny

## Project Overview
Have you ever wanted to quickly find the best movies within your preferred genres? This movie recommendation system is here to make that task a breeze. It combines four valuable data sources: one containing detailed genre information about numerous movies, another containing IMDb's top 100 rated movies with genre data, and 2 other sources containing trending movies in theaters! By cross-referencing these sources, we can pinpoint the highest-rated movies within the genres you love.

To answer some business-related questions to define the scope of this project, we have generated a few: 
* What genres of film are most appealing to the general public?
* Does recency bias play a factor: Will movies at the box office after a couple of weeks, for example, die down and receive lower ratings?
* Will movies with sequels/more than a standalone installation receive better ratings?

## How It Works
At its core, our Movie Recommendation System involves the following key steps:

Data Collection: We collect data from four primary sources: the first source provides genre information about a vast number of movies, while the other sources contain IMDb's top-rated movies along with genre details.

Data Integration: We meticulously merge these datasets, creating a comprehensive repository that combines detailed genre information with IMDb's top-rated movies.

Enjoy the Magic: Once you receive the recommendations, it's time to sit back, relax, and enjoy some fantastic movies.


## Ingestion

We have four main data sources: One from Kaggle.com, which contains many data gathering competitions and complex data sets, and an IMDb API that contains many of IMDb's popular data search content; in this case, we will be using an API that shows IMDb's top 100 rated movies across many genres, as well as sources containing some of the box office hits to find some of the most popular movies in some of the most popular genres, to recommend to many common viewers. This data was ingested using Python and pandas, a Python open-source data analysis and manipulation tool that can read data from these sources and store them as comma-separated values (.csv) files, which will then be stored in Azure Data Lake Storage (ADLS), a cloud-based, enterprise data lake solution. The data is then drawn out to Data-Bricks, a data engineering tool, which will be used to mold and siphon the data into a more useful form where we can move on to transformation and serving, the next parts of the product.

## Transformation & Serving

Concluding the project, we arrive at the final step of the data engineering cycle: transformation & serving. After siphoning the data through Databricks and using the .csv files generated to analyze our data, we can now answer some of the questions we have set for ourselves: 
* Some of the top genres of film include: Animation, Drama, Crime, Romance, Adventure
* Movies with sequels generally have higher expectations from the public, but this does not always mean a higher rating yield, most commonly occurring from superhero movies, as they usually stretch out having multiple installations and film universes
* Recency bias is indeed a factor: Saw X for example, a recent release, started as a solid 7.0 on IMDb, then later went down to a 6.6 after some time sitting at the box office.

Databricks was used as a transformation platform, as after the data was siphoned, the results became clear and could be manipulated to answer the three business questions set out. Databricks could also be used to answer more analytical questions such as: What genre of movies will do better in the future? We can find the answer to this one for example by tracking more recent releases related to genre and seeing how many more new releases are made as we progress through time. 

I also created a star schema that was then created using SQL statements in Azure Data Studio, the results of which are uploaded into ADLS. A file is included in this repo that shows the star schema diagram in a text format.

While the scope of this was made for analysis, a machine-learning aspect would work very well for this project as well. This could be turned into an ML-based project that could help, for example, a streaming service recommend movies and other titles to viewers based on their likes, niches, and watch history.

A graph created using PowerBI could be useful in serving, but I believe that this project was best left ending at the transformation standpoint as a mark of its versatility, and its ability to answer other questions through recent movie media. However, there are artifacts of the filtered data left in the repo as evidence of transformation.
