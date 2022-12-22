import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle


filename = 'nlp.pkl'
clf = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('transform.pkl','rb'))

def create_similarity():
    data = pd.read_csv('main_data.csv')

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])

    similarity = cosine_similarity(count_matrix)
    return data,similarity

def recommend_movie(movie):
    movie = movie.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if movie not in data['movie_title'].unique():
        return('The movie is not available')
    else:
        i = data.loc[data['movie_title']==movie].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11]
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l
    


def list_converter(arr):
    arr = arr.split('","')
    arr[0] = arr[0].replace('["','')
    arr[-1] = arr[-1].replace('"]','')
    return arr


def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())




