from config.db import conn
from schemas.fns import serializeDict,serializeList
import json
from pymongo import MongoClient
mc=MongoClient()
db=mc['moviesdb']
collection = db['users']
class User():
    def __init__(self, user_id):  
        self.user_id = user_id
        user_exists = self.check_user_exists()
        if user_exists:
            print (user_exists)
            self.watched = user_exists['watched']
            print('self.watched= ', self.watched)
        else:
            self.watched = []
    def create_new_user(self):
        if not self.check_user_exists():
            collection.update_one({'user_id':self.user_id },{"$set":{'user_id':self.user_id, 'watched':self.watched}},upsert=True)
    def check_user_exists(self):
        found_user =  conn.moviesdb.users.find_one({'user_id':self.user_id})
        return found_user
        return True
    def update_user_watched(self, mname):
        print(mname)
        if self.check_user_exists():
            self.watched.append(mname)
            user_dict = {'user_id':self.user_id, 'watched':self.watched}
            print(user_dict)
            collection.update_one({'user_id':self.user_id },{"$set":user_dict},upsert=True)
            return True
