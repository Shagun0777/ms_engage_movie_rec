from csv_to_data import fetch_csv_to_data_dict
from pymongo import MongoClient
mc=MongoClient()
db=mc['moviesdb']

print(db)
def csv_to_mongo():
    collection_pdfs=db['movies']
    url = r'C:\Users\shagu\Desktop\micro_move_rec\micro_move_rec\tmdb_5000_movies.csv'
    data, data_dict = fetch_csv_to_data_dict(url)
    print (len(data_dict))
    for item in data_dict:
        print(item.keys())
        collection_pdfs.update_one({'m_id':item['id']},{"$set":item},upsert=True)
    collection_pdfs=db['credits']
    url =r'C:\Users\shagu\Desktop\micro_move_rec\micro_move_rec\tmdb_5000_credits.csv'
    data, data_dict = fetch_csv_to_data_dict(url)
    print (len(data_dict))
    for item in data_dict:
        print(item.keys())
        collection_pdfs.update_one({'m_id':item['movie_id']},{"$set":item},upsert=True)

csv_to_mongo()