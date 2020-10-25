from flix.domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watched_movies = []

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            if movie not in self.__watched_movies:
                self.__watched_movies.append(movie)

    def remove_movie(self, movie):
        if isinstance(movie, Movie):
            if movie in self.__watched_movies:
                self.__watched_movies.remove(movie)

    def select_movie_to_watch(self, index):
        if index < len(self.__watched_movies)-1 or index > 0 - len(self.__watched_movies):
            return self.__watched_movies[index]
        else:
            return None

    def size(self):
        return len(self.__watched_movies)

    def first_movie_in_watchlist(self):
        if len(self.__watched_movies) > 0:
            return self.__watched_movies[0]
        else:
            return None

    def __iter__(self):
        iter(self.__watched_movies)

    def __next__(self):
        next(self.__watched_movies)
