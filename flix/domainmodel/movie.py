from flix.domainmodel.genre import Genre
from flix.domainmodel.actor import Actor
from flix.domainmodel.director import Director
from flix.domainmodel.review import Review


class Movie:
    def __init__(self, movie_name: str = None, release_year: int = None, anid : int = None):
        self.id = None
        if movie_name == "" or type(movie_name) is not str:
            self.__movie_name = None
        else:
            self.__movie_name = movie_name.strip()
        if isinstance(release_year, int):
            if release_year >= 1900:
                self.__release_year = release_year
            else:
                self.__release_year = None
        else:
            self.__release_year = None
        self.__actor_list = []
        self.__genre_list = []
        self.__description = None
        self.__director = None
        self.__runtime = None
        self.__review_list = []
        self.__id: int = anid

    @property
    def id(self) -> int:
        return self.__id

    @property
    def movie_name(self) -> str:
        return self.__movie_name

    def __repr__(self):
        return f"<Movie {self.__movie_name}, {str(self.__release_year)}>"

    def __eq__(self, other):
        if repr(self) == repr(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if repr(self) < repr(other):
            return True
        else:
            return False

    def __hash__(self):
        return hash(repr(self))

    def add_actor(self, actor):
        if actor not in self.__actor_list and isinstance(actor, Actor):
            self.__actor_list.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actor_list:
            self.__actor_list.remove(actor)

    def add_genre(self, genre):
        if genre not in self.__genre_list and isinstance(genre, Genre):
            self.__genre_list.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genre_list:
            self.__genre_list.remove(genre)

    def return_actor(self):
        return self.__actor_list

    def return_genre(self):
        return self.__genre_list

    @property
    def title(self):
        return self.__movie_name

    @title.setter
    def title(self, new_name):
        if isinstance(new_name, str):
            self.__movie_name = new_name.strip()
        else:
            pass

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            if new_description != "":
                self.__description = new_description.strip()
        else:
            pass

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, new_director: Director):
        self.__director = new_director

    @property
    def review(self):
        return self.__review_list

    @review.setter
    def review(self, new_review: Review):
        self.__review_list.append(new_review)

    @property
    def actors(self):
        return self.__actor_list

    @actors.setter
    def actors(self, new_actor: Actor):
        self.__actor_list.append(new_actor)

    @property
    def genres(self):
        return self.__genre_list

    @genres.setter
    def genres(self, new_genre: Genre):
        self.__genre_list.append(new_genre)

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, new_release_year: int):
        self.__release_year = new_release_year

    @property
    def runtime_minutes(self):
        return self.__runtime

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if isinstance(runtime, int):
            if runtime > 0:
                self.__runtime = runtime
            else:
                raise ValueError()
        else:
            pass
