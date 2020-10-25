import pytest
from datetime import datetime


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
            self.__colleague_list = []
            self.__movie_list = []
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__colleague_list = []
            self.__movie_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleague_list.append(colleague)

    def return_actor_colleague(self):
        return self.__colleague_list

    def movie_list(self):
        return self.__movie_list

    def check_if_this_actor_worked_with(self, colleague):
        if len(self.__colleague_list) > 0:
            for i in self.__colleague_list:
                if i == colleague:
                    return True
            return False
        else:
            return False

    def is_applied_to(self, movie: Movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie: Movie):
        self.__movie_list.append(movie)

def make_actor_association(movie: Movie, actor: Actor):
    if actor.is_applied_to(movie):
        raise ModelException(f'Tag {actor.actor_full_name} already applied to Movie "{movie.title}"')

    movie.add_actor(actor)
    actor.add_movie(movie)

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

    def is_applied_to(self, movie: Movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie: Movie):
        self.__movie_list.append(movie)

    def movie_list(self):
        return self.__movie_list

def make_director_association(movie: Movie, director: Director):
    if director.is_applied_to(movie):
        raise ModelException(f'Tag {director.director_full_name} already applied to Movie "{movie.title}"')

    movie.director(director)
    director.add_movie(movie)


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

    def is_applied_to(self, movie: Movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie: Movie):
        self.__movie_list.append(movie)

    def movie_list(self):
        return self.__movie_list

def make_genre_association(movie: Movie, genre: Genre):
    if genre.is_applied_to(movie):
        raise ModelException(f'Tag {genre.genre} already applied to Movie "{movie.title}"')

    movie.genres(genre)
    genre.add_movie(movie)


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


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if movie == "" or type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if isinstance(rating, int):
            if rating >= 1 and rating <= 10:
                self.__rating = rating
            else:
                self.__rating = None
        else:
            self.__rating = None
        self.__timestamp = datetime.time

    @property
    def movie(self):
        return self.__movie

    def __repr__(self):
        return f"<Review {self.__movie}, {str(self.__rating)}, {str(self.__timestamp)}, {self.__review_text}>"

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            return True
        else:
            return False

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

def make_review(review_text: str, user: User, movie: Movie, timestamp: datetime = datetime.today()):
    review = Review(user, movie, review_text, timestamp)
    user.add_review(review)
    movie.review(review)

    return review


class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0
        self.__watched_tv_shows = []
        self.__tv_show_reviews = []
        self.__time_spent_watching_tv_shows_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__user_name < other.user_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(repr(self))

    def watch_movie(self, movie):
        if isinstance(movie, Movie):
            if movie.runtime_minutes is not None:
                self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__watched_movies.append(movie)
        else:
            pass

    def watch_tv_show(self, tv_show):
        if isinstance(tv_show, TV_Show):
            if tv_show.runtime_minutes is not None:
                self.__time_spent_watching_tv_shows_minutes += tv_show.runtime_minutes
            self.__watched_tv_shows.append(tv_show)
        else:
            pass

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)
        else:
            pass

    def add_tv_review(self, review):
        if isinstance(review, TV_Show_Review):
            self.__tv_show_reviews.append(review)
        else:
            pass

    @property
    def password(self):
        return self.__password

    @property
    def username(self):
        return self.__user_name

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def watched_tv_shows(self):
        return self.__watched_tv_shows

    @property
    def reviews(self):
        return self.__reviews

    @property
    def tv_show_reviews(self):
        return self.__tv_show_reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @property
    def time_spent_watching_tv_shows_minutes(self):
        return self.__time_spent_watching_tv_shows_minutes
