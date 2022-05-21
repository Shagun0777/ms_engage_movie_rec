from config.db import conn
from schemas.fns import serializeDict,serializeList
import json

def extract_movies_list():
    return conn.moviesdb.movies.find()


def fetch_exact_move(all_movies, ip_movie):
    for movie in all_movies:
        if (movie['title'].lower() == ip_movie.lower()):
            return movie
    return ''


def recommend_on_basis_of_name(all_movies, ip_movie, exact_movie_bool, exact_movie):
    ans = []
    for movie in all_movies:
        if (movie['title'].lower() == ip_movie.lower() or movie['title'].lower() in ip_movie.lower() or ip_movie.lower() in movie['title'].lower() 
        and  (not exact_movie_bool or  movie['m_id'] != exact_movie['m_id'])):
            ans.append(movie)
    return ans


def recommend_on_basis_of_genres(all_movies, ip_movie, exact_movie_bool, exact_movie):
    ans = []
    for movie in all_movies:
        genres_dict = json.loads(movie['genres'])
        curr_movie_year = movie['release_date'][0:4]
        ip_genres_dict = json.loads(exact_movie['genres'])
        ip_year = exact_movie['release_date'][0:4]

        print (type(genres_dict), type(ip_genres_dict))
        # break
        genres = set()
        ip_genres = set()
        for gen in genres_dict:
            genres.add(gen['id'])
        for gen in ip_genres_dict:
            ip_genres.add(gen['id'])
        match = ip_genres.intersection(genres)
        if len(match) >2 and abs(int(curr_movie_year) - int(ip_year)) < 1:
            ans.append(movie)
    return ans


def recommend_movie(ip_movie):
    all_movies = serializeList(extract_movies_list())
    ans = []
    fans = {}
    exact_movie = fetch_exact_move(all_movies, ip_movie)
    if exact_movie:
        exact_movie_bool = True
    fans['exact match'] = exact_movie
    fans['recommended_match'] = {}
    fans['recommended_match']['By Name'] = recommend_on_basis_of_name(all_movies, ip_movie, exact_movie_bool, exact_movie)
    fans['recommended_match']['By Genre'] = recommend_on_basis_of_genres(all_movies, ip_movie, exact_movie_bool, exact_movie)
    return fans