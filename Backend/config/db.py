from pymongo import MongoClient
from pymongo.server_api import ServerApi
conn=MongoClient("mongodb://localhost:27017/test")

# conn = MongoClient("mongodb+srv://shagun:shagun123@cluster0.70i8n.mongodb.net/?retryWrites=true&w=majority")
# print(conn)
# # db = client.test

# conn = MongoClient("mongodb+srv://shagun:WucMiA4AWKldlleg@cluster0.70i8n.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.test
