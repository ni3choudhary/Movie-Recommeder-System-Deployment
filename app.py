import pickle
import streamlit as st
import requests
from os import environ
from dotenv import load_dotenv
load_dotenv()

API_KEY = environ['API_KEY']

def fetch_poster(movie_id,api_key):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommended_movies(movie_name):
    index = movies_df[movies_df['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id,API_KEY))
        recommended_movie_names.append(movies_df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies_df = pickle.load(open('model/movie_df.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movies_list = movies_df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommended_movies(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





