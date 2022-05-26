<h1 align="center">Movie Hunt	:movie_camera: </h1>

<p align="center">
<img src="https://media4.giphy.com/media/7zMsa4CDcXY7PEDNGN/giphy.gif">

</p>
<p align="center">A web-based movie app (Demo only)</p>
 <p align="center">
<img src="./images/Screenshot%20(763).png"width="800">

</p>

## About

The app will search for movies and render the results to the user. <br/>

In this application we have created our own API that fetches the data from the database. We have used `MongoDB` as database . The information present in the database is imported from the csv file from tmdb . Here, each user will be having their unique profile with their Personal watched list and movie Recommendation section . <br/>

This application is hosted so it is accessible on the internet. For remote database I have used `MongoDB Atlas` , for Backend hosting I have used `Heroku` and I have deployed my server there . For frontend I have used `Firebase` .

## How to use this application

### _To use this application go to the link beloww and follow these steps_-

[https://movie-rec-fe.web.app](https://movie-rec-fe.web.app)

- _Application name_: Movie Hunt
- _Homepage URL_: `https://movie-rec-fe.web.app`
- _Create new user URL_: `https://movie-rec-fe.web.app/login/New_user_id`
- _Adding new movie to user watched list URL_: `https://movie-rec-fe.web.app/login/New_user_id/Movie_name`
- _Recommendation of a movie URL_: `https://movie-rec-fe.web.app/recommend/Movie_name `

### _For local setup_:

`Need to have python3 and Node.Js installed.`

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

## Algorithms Used In The Application

### Divide and conquer algorithms

**Quicksort** :
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. Quicksort is `O(n logn)` in the best and average case scenarios and `O(n^2)` in the worst case. But since it has the upper hand in the average cases for most inputs, Quicksort is generally considered the “fastest” sorting algorithm. Here , we are using Quick Sort Algorithm to sort the user **watched list** in lexicographical order .

### Dynamic programming algorithms

**Caching** :
Dynamic programming (and memoization) works to optimize the naive recursive solution by caching the results to these subproblems. If there are no overlapping subproblems, there is no point caching these results, since we will never use them again.

### Greedy algorithms :

**Greedy** -
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are best fit for Greedy. I have used this algorithm to recommend final set of movies to the user .

### Branch and bound algorithms

**Optimisation** -
An important advantage of branch-and-bound algorithms is that we can control the quality of the solution to be expected, even if it is not yet found. The cost of an optimal solution is only up to smaller than the cost of the best computed one.

### Randomized algorithms

**Random Pivot Point** -
A randomized algorithm uses a random number at least once during the computation to make a decision . Durinng the implementation of Quicksort Algorithm , Randomized Algorithm is using there a random number to choose a pivot .

## Functional Features

### The functional features in this application are implemented by using different kind of algorithm .

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

### Reason for using MongoDB as databse

Here we have used `MongoDb` because the user class can have empty/single or multiple watched movies so we cannot fix size of it in `SQL DB`.
