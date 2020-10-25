import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from flix.adapters.repository import AbstractRepository, RepositoryException
from flix.domainmodel.movie import Movie
from flix.domainmodel.actor import Actor, make_actor_association
from flix.domainmodel.director import Director, make_director_association
from flix.domainmodel.genre import Genre, make_genre_association
from flix.domainmodel.user import User
from flix.domainmodel.review import Review, make_review


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._actors = list()
        self._genres = list()
        self._directors = list()
        self._users = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.id] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None

        try:
            movie = self._movies_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_movies_by_date(self, target_date: int) -> List[Movie]:
        movie_name = None
        date_year = target_date
        target_movie = Movie(movie_name, date_year)
        matching_movies = list()

        try:
            index = self.movies_index(target_movie)
            for movie in self._movies[index:None]:
                if movie.date == target_date:
                    matching_movies.append(movie)
                else:
                    break
        except ValueError:
            # No articles for specified date. Simply return an empty list.
            pass

        return matching_movies

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_id(self, id_list):
        # Strip out any ids in id_list that don't represent Article ids in the repository.
        existing_ids = [id for id in id_list if id in self._movies_index]

        # Fetch the Articles.
        movies = [self._movies_index[id] for id in existing_ids]
        return movies

    def get_movie_ids_for_actor(self, actor_name: str):
        # Linear search, to find the first occurrence of a Tag with the name tag_name.
        actor = next((actor for actor in self._actors if actor.actor_full_name == actor_name), None)

        # Retrieve the ids of articles associated with the Tag.
        if actor is not None:
            movie_ids = [movie.id for movie in actor.movie_list]
        else:
            # No Tag with name tag_name, so return an empty list.
            movie_ids = list()

        return movie_ids

    def get_movie_ids_for_genre(self, genre_name: str):
        # Linear search, to find the first occurrence of a Tag with the name tag_name.
        genre = next((genre for genre in self._genres if genre.genre == genre_name), None)

        # Retrieve the ids of articles associated with the Tag.
        if genre is not None:
            movie_ids = [movie.id for movie in genre.movie_list]
        else:
            # No Tag with name tag_name, so return an empty list.
            movie_ids = list()

        return movie_ids

    def get_movie_ids_for_director(self, director_name: str):
        # Linear search, to find the first occurrence of a Tag with the name tag_name.
        director = next((director for director in self._directors if director.director_full_name == director_name), None)

        # Retrieve the ids of articles associated with the Tag.
        if director is not None:
            movie_ids = [movie.id for movie in director.movie_list]
        else:
            # No Tag with name tag_name, so return an empty list.
            movie_ids = list()

        return movie_ids

    def get_date_of_previous_movie(self, movie: Movie):
        previous_date = None

        try:
            index = self.movie_index(movie)
            for stored_movie in reversed(self._movies[0:index]):
                if stored_movie.date < movie.release_year:
                    previous_date = stored_movie.date
                    break
        except ValueError:
            # No earlier articles, so return None.
            pass

        return previous_date

    def get_date_of_next_movie(self, movie: Movie):
        next_date = None

        try:
            index = self.movie_index(movie)
            for stored_movie in self._movies[index + 1:len(self._movies)]:
                if stored_movie.date > movie.release_year:
                    next_date = stored_movie.date
                    break
        except ValueError:
            # No subsequent movies, so return None.
            pass

        return next_date

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews

    # Helper method to return article index.
    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].date == movie.release_year:
            return index
        raise ValueError

    def movies_index(self, target_movie):
        return self._movies.index(target_movie)


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies_and_other_info(data_path: str, repo: MemoryRepository):
    actors = dict()
    directors = dict()
    genres = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):

        movie_rank = int(data_row['Rank'])
        movie_genres = data_row['Genres'].split(", ")
        movie_actors = data_row['Actors'].split(", ")
        movie_directors = data_row['Director'].split(", ")

        # Add any new tags; associate the current article with tags.
        for actor in movie_actors:
            if actor not in actors.keys():
                actors[actor] = list()
            actors[actor].append(movie_key)
        del data_row[-number_of_actors:]

        for genre in movie_genres:
            if genre not in genres.keys():
                genres[genre] = list()
            genres[genre].append(movie_key)
        del data_row[-number_of_genres:]

        for director in movie_directors:
            if director not in directors.keys():
                directors[director] = list()
            directors[director].append(movie_key)
        del data_row[-number_of_directors:]

        # Create Movie object.
        print(data_row)
        movie = Movie(
            title=data_row[2],
            date=date.fromisoformat(data_row[1]),
            id=movie_key
        )

        # Add the Article to the repository.
        repo.add_movie(movie)

    # Create Tag objects, associate them with Articles and add them to the repository.
    for actor_name in actors.keys():
        actor = Actor(actor_name)
        for movie_id in actors[actor_name]:
            movie = repo.get_movie(movie_id)
            make_actor_association(movie, actor)
        repo.add_actor(actor)

    for director_name in directors.keys():
        director = Director(director_name)
        for movie_id in Directors[Director_name]:
            movie = repo.get_movie(movie_id)
            make_director_association(movie, director)
        repo.add_director(director)

    for genre_name in genres.keys():
        genre = Genre(genre_name)
        for movie_id in genres[genre_name]:
            movie = repo.get_movie(movie_id)
            make_genre_association(movie, genre)
        repo.add_genre(genre)


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            username=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def load_reviews(data_path: str, repo: MemoryRepository, users):
    for data_row in read_csv_file(os.path.join(data_path, 'reviews.csv')):
        review = make_review(
            review_text=data_row[3],
            user=users[data_row[1]],
            movie=repo.get_movie(int(data_row[2])),
            timestamp=datetime.fromisoformat(data_row[4])
        )
        repo.add_review(review)


def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_movies_and_other_info(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load comments into the repository.
    load_reviews(data_path, repo, users)
