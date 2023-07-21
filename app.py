import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetch the index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        # print(i[0]) # but we need movies and not indexes
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

st.title('Movies Recommender System')

selected_movie_name = st.selectbox('What recommendations do you need?', movies['title'].values)


if(st.button('Recommend')):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


# For movie posters: in recommend dedf ..fetch the index
def fetch_poster(movie_id):
