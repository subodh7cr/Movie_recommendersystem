


import streamlit as st
import pickle
import pandas as pd


#logic to give top 5 movie list
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances= sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies=[]
    
    for i in distances:
      recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
      

movies_dict=pickle.load(open('movie_dict.pkl','rb'))

#creating new dataframe from the dataframe that we used from original file

movies=pd.DataFrame(movies_dict)


similarity=pickle.load(open('similarity.pkl','rb'))


#movie_list = movie_list['title'].values

#create data frame here in case of dict

#the title we want to show in webpage
st.title('Movie Recommender System')

#to have a select box
selected_movie_name=st.selectbox(
'how would you like to be contacted',
movies['title'].values)

#add button recommend
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
