from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.tv_show import TV_Show
from domainmodel.tv_show_review import TV_Show_Review

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
