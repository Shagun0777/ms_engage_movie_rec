from csv_to_data import fetch_csv_to_data_dict
from pymongo import MongoClient
mc=MongoClient()
db=mc['moviesdb']
collection_pdfs=db['movies']
print(db)
def csv_to_mongo():
    url = '/home/shivam/Desktop/Personal/micro_move_rec/tmdb_5000_movies.csv'
    data, data_dict = fetch_csv_to_data_dict(url)
    print (len(data_dict))
    for item in data_dict:
        print(item.keys())
        collection_pdfs.update_one({'m_id':item['id']},{"$set":item},upsert=True)

csv_to_mongo()