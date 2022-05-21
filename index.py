from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import ALL_METHODS
from starlette.responses import Response
from schemas.fns import serializeDict,serializeList
from fastapi.templating import Jinja2Templates
from utils import recommend_movie
# from config.db import conn 
import json
from fastapi_utils.tasks import repeat_every

from config.db import conn

print(22)
origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
template=Jinja2Templates(directory="htmldirectory")
print(22)
@app.get("/")
async def index(request: Request):    
    kk=serializeList(conn.moviesdb.movies.find())
    response_dict = {}
    response = []
    for i in kk:
        ans = {}
        ans['title'] = i['title']
        print(type(i), type(i['title']))
        response.append(ans)
    response_dict['data'] = response
    return response_dict


# @app.on_event("startup")
# @repeat_every(seconds=60 * 60)  # 1 hour
# def printit():

@app.get("/recommend_movie")
async def index(request: Request):
    req_movie = request.query_params['movie']  
    print('shivam')   
    kk=serializeList(conn.moviesdb.movies.find())
    response_dict = {}
    response = []
    for i in kk:
        ans = {}
        ans['title'] = i['title']
        # print(type(i), type(i['title']))
        response.append(ans)
    response_dict['data'] = response
    response_dict['data'] = recommend_movie(req_movie)
    return response_dict


