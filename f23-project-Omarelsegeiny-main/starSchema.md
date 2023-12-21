# Star Schema Diagram
## Fact Table: 

##### movie_ratings
* movie_id (int, foreign key referencing all movie tables)
* imdb_rating (decimal)
* imdb_rating_count (decimal)


## Dimension Tables:

mostPopularMovies_dim
* movie_id (int, primary key)
* rank (int)
* title (string)
* year (int)

movies_genre_dim
* movie_id (int, foreign key referencing all movie tables)
* genre (string)

top250Movies_dim
* movie_id (int, primary key)
* rank (string)
* title (string)

allMovies_dim

* movie_id (int, primary key)
* rank (string)
* title (string)
* year (int)
