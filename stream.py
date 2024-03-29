import streamlit as st
import pickle
import pandas as pd
movies_dict= pickle.load(open('D:\Recommender-System-Project\movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index= movies[movies['title']==movie].index[0]
    distances= similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:6]
    recommend_movies= []
    for i in movies_list:
        #fetch poster from API
        
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Bleh bleh',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)