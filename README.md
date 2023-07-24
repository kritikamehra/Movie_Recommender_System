# Movie_Recommender_System


## Aim
This project aims to recommend Movies based on similar preferences, genre, and other elements.

## How to use it?
1. Clone the repository
2. Install the required packages in the "requirements.txt" file.
3. Run the "Movie Recommendation.ipynb" file
4. Run the "app.py" file

And you are good to go.

## Description
### What does this project do?
This project takes the parameters from TMDB Datset of 5000 movies which includes features like Title, Movie id, Casst, Crew, Genres etc. 
It then uses cosine similarity to recommend the top 5 most similar movies to the selected movie.

The data was cleaned and analysed. For example: applying one hot encoder on genres.

Once the model is trained and personalized recommendations are generated, the application uses pickle to save the trained model so that it can be used for future recommendations without the need to retrain it every time.

