 <p align="center">
<img src="https://media4.giphy.com/media/7zMsa4CDcXY7PEDNGN/giphy.gif">

</p>
<p align="center">A web-based movie app (Demo only)</p>
 <p align="center">
<img src="./images/Screenshot%20(763).png"width="800">

</p>

## About

The app will search for movies and render the results to the user. <br/>

In this application we have created our own API that fetches the data from the database. We have used MongoDB as database . The information present in the database is imported from the csv file from tmdb . Here, each user will be having their unique profile with their Personal watched list and movie Recommendation section .

## How to use this application

### _To use this application go to the link beloww and follow these steps_-

[https://movie-rec-fe.web.app](https://movie-rec-fe.web.app)

- _Application name_: Movie Hunt
- _Homepage URL_: `https://movie-rec-fe.web.app`
- _Create new user URL_: `https://movie-rec-fe.web.app/login/New_user_id`
- _Adding new movie to user watched list URL_: `https://movie-rec-fe.web.app/login/New_user_id/Movie_name`
- _Recommendation of a movie URL_: `https://movie-rec-fe.web.app/recommend/Movie_name `

### _For local setup_:

Need to have python3 and Node.Js installed.

#### Backend Command

```bash
cd Backend
```

```bash
pip install -r requirements.txt
```

```bash
python -m uvicorn index:app --reload
```

In new terminal/cmd

#### Frontend Command

```bash
cd Frontend
```

```bash
npm install
```

```bash
npm start
```

## Functional Features

- _Log-In_ - This feature will help the user in logging in to a database of the application
- _WatchList_ - This feature will give the list of all the movies that are watched by a particular user .
- _Exact Movies_ -This feature will recommend the exact set of movies that are watched by a particular user .

- _Final Recommendation_ - This feature will recommend the set of movies based on the movies that are watched by a particular user .

- _Recommendation by name_ - This feature will give recommendation based on the names of the movies that are present in the watchlist of a particular user .
- _Recommendation by cast_ - This feature will give recommendation based on the cast of the movies that are present in the watchlist of a particular user .

- _Recommendation by genre_ - This feature will give recommendation based on the different genre of the movies that are present in the watchlist of a particular user .

- _API Fetch_ - Here , we have created our own API that fetches the data from the database. The information present in the database is imported from the csv file .
- _Loading_ - Loading text here is to inform users about the wait time, reason and expectation on the status of ongoing processes in the background, such as loading user information or adding a new movie to user watchlist .
- _Sort by lambda_ - We are using one parameter in the sort function, which is the key parameter. It is allowing us to create our very own sorting order. We are using the lambda functions in this parameter, which is enabling us to create our own single-line function.It is string the list of the basis of popularity so the most popular movie will be shown at top .

- _Sort by year_ - This function will sort all the recommendation list be it be by genre , by names , by cast etc on the basis of year in ascending and descending order .

- _Sort by name_ - This function will sort all the recommendation list be it be by genre , by names , by cast etc on the basis of name From A-Z or Z-A.
- _Link for movies_ - Clicking on each movie title will lead you to information page of that movie .
- _Hosted_ -This application is hosted so it is accessible on the internet. For remote database I have used `MongoDB Atlas` , for Backend hosting I have used `Heroku` and I have deployed my server there . For frontend I have used `Firebase` .
- _Flexible for every device_ - This app is available on both mobile and desktop . They are not native to a particular type of system.
- _Sorting the user Watched list_ - Clicking on each movie title will lead you to information page of that movie .
