import pytest
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
            self.__movie_list = []
        else:
            self.__director_full_name = director_full_name.strip()
            self.__movie_list = []

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__director_full_name < other.director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__director_full_name)

    def is_applied_to(self, movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie):
        self.__movie_list.append(movie)

    def movie_list(self):
        return self.__movie_list

def make_director_association(movie, director: Director):
    if director.is_applied_to(movie):
        raise ModelException(f'Tag {director.director_full_name} already applied to Movie "{movie.title}"')

    movie.director(director)
    director.add_movie(movie)
