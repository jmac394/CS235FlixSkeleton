from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from datafilereaders.tv_show_file_csv_reader import TVShowFileCSVReader
from domainmodel.user import User, Review, Movie

def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

    filename = 'datafiles/Data1000TVShows.csv'
    tv_show_file_reader = TVShowFileCSVReader(filename)
    tv_show_file_reader.read_csv_file()

    print(f'number of unique tv shows: {len(tv_show_file_reader.dataset_of_tv_shows)}')
    print(f'number of unique actors: {len(tv_show_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(tv_show_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(tv_show_file_reader.dataset_of_genres)}')


if __name__ == "__main__":
    main()