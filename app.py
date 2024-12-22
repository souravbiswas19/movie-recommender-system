import streamlit as st
import pickle
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer


# cv = CountVectorizer(max_features=5000, stop_words='english')
# vectors = cv.fit_transform(movies['tags']).toarray()

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recomended_movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recomended_movies = []
    for i in recomended_movies_list:
        recomended_movies.append(movies.iloc[i[0]].title)
    return recomended_movies

movies = pickle.load(open('movie.pkl', 'rb'))
movies_list = list((movies['title'].values).flatten())
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select Movie?",
    movies_list,
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)