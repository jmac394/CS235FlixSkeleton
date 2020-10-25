import pytest


class Genre:
    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre = None
            self.__movie_list = []
        else:
            self.__genre = genre.strip()
            self.__movie_list = []

    @property
    def genre(self) -> str:
        return self.__genre

    def __repr__(self):
        return f"<Genre {self.__genre}>"

    def __eq__(self, other):
        if self.__genre == other.genre:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__genre < other.genre:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__genre)

    def is_applied_to(self, movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie):
        self.__movie_list.append(movie)

    def movie_list(self):
        return self.__movie_list

def make_genre_association(movie, genre: Genre):
    if genre.is_applied_to(movie):
        raise ModelException(f'Tag {genre.genre} already applied to Movie "{movie.title}"')

    movie.genres(genre)
    genre.add_movie(movie)
