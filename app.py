import streamlit as st
import pickle
import pandas as pd
import requests
from urllib3.util.retry import Retry

# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c801abc5eb3c52de83e28f9ea47a53d1&language=en-US'.format(movie_id)
    retry = Retry(connect=3, backoff_factor=0.5)
    data = requests.get(url)
    data = data.json()
    poster_path =  data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetch the index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        # print(i[0]) # but we need movies and not indexes
        # fetch poster from API
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

st.title('Movies Recommender System')

selected_movie = st.selectbox('Type or select a movie from the dropdown', movies['title'].values)


if(st.button('Show Recommendations')):
    name, poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])
