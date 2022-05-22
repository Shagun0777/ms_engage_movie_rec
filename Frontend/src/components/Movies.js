

const Movies = ({ list_movies }) => {
  let position = 0;
  console.log(list_movies)
  return (
    <div>
      {list_movies.map((movie) => (
        <div id="row">
          {movie}
        </div>
      ))}
    </div>
  );
};

export default Movies;
