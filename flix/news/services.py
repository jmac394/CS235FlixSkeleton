from typing import List, Iterable

from adapters.repository import AbstractRepository
from domainmodel.review import make_review, Review
from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_review(movie_id: int, review_text: str, username: str, repo: AbstractRepository):
    # Check that the article exists.
    movie = repo.get_movie(movie_id)
    if movie is None:
        raise NonExistentArticleException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    review = make_review(review_text, user, movie)

    # Update the repository.
    repo.add_review(review)


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)


def get_movies_by_date(date, repo: AbstractRepository):
    # Returns articles for the target date (empty if no matches), the date of the previous article (might be null), the date of the next article (might be null)

    movies = repo.get_movies_by_date(target_date=date)

    movies_dto = list()
    prev_date = next_date = None

    if len(movies) > 0:
        prev_date = repo.get_date_of_previous_movie(movies[0])
        next_date = repo.get_date_of_next_movie(movies[0])

        # Convert Articles to dictionary form.
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_date, next_date


def get_movie_ids_for_actor(actor_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_actor(actor_name)

    return movie_ids


def get_movie_ids_for_director(director_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_director(director_name)

    return movie_ids


def get_movie_ids_for_director(director_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_director(director_name)

    return movie_ids


def get_movie_by_id(id_list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)

    # Convert Articles to dictionary form.
    movies_as_dict = movies_to_dict(movies)

    return movies_as_dict


def get_reviews_for_movie(movie_id, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return reviews_to_dict(movie.review)


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'id': movie.id,
        'date': movie.release_year,
        'title': movie.title,
        'hyperlink': movie.hyperlink,
        'image_hyperlink': movie.image_hyperlink,
        'reviews': reviews_to_dict(movie.review),
        'actors': actors_to_dict(movie.actors),
        'directors': directors_to_dict(movie.directors),
        'genres': genres_to_dict(movie.genres)
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def review_to_dict(review: Review):
    review_dict = {
        'username': review.user.username,
        'movie_id': review.movie.id,
        'review_text': review.review_text,
        'timestamp': review.timestamp
    }
    return review_dict


def reviews_to_dict(reviews: Iterable[Review]):
    return [review_to_dict(review) for review in reviews]


def actor_to_dict(actor: Actor):
    actor_dict = {
        'name': actor.actor_full_name,
        'acted_in_movies': [movie.id for movie in actor.movie_list()]
    }
    return actor_dict


def actors_to_dict(actors: Iterable[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def director_to_dict(director: Director):
    director_dict = {
        'name': director.director_full_name,
        'directed_movies': [movie.id for movie in director.movie_list()]
    }
    return director_dict


def directors_to_dict(directors: Iterable[Director]):
    return [director_to_dict(director) for director in directors]


def genre_to_dict(genre: Genre):
    genre_dict = {
        'name': genre.genre,
        'genre_of_movies': [movie.id for movie in genre.movie_list()]
    }
    return genre_dict


def genres_to_dict(genres: Iterable[Genre]):
    return [genre_to_dict(genre) for genre in genres]


# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_movie(dict):
    movie = Movie(dict.id, dict.date, dict.title, dict.first_para, dict.hyperlink)
    # Note there's no comments or tags.
    return movie
