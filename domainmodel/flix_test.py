from datetime import datetime

import pytest
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User
from domainmodel.tv_show import TV_Show
from domainmodel.tv_show_review import TV_Show_Review
from domainmodel.tv_show_watchlist import TV_Show_WatchList
from datafilereaders import movie_file_csv_reader

# Director class
def test_director_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None


def test_director_eq_function():
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert director1.__eq__(director2) is True


def test_director_false_eq_function():
    director1 = Director("Taika Waititi")
    director2 = Director(" ")
    assert director1.__eq__(director2) is False


def test_director_lt_function():
    director1 = Director("Taika Waititi")
    director2 = Director("Hayao Miyazaki")
    assert director2.__lt__(director1) is True


def test_director_false_lt_function():
    director1 = Director("Taika Waititi")
    director2 = Director("Hayao Miyazaki")
    assert director1.__lt__(director2) is False


# Genre class


def test_genre_init():
    genre1 = Genre("Comedy")
    assert repr(genre1) == "<Genre Comedy>"
    genre2 = Genre("")
    assert genre2.genre is None
    genre3 = Genre(42)
    assert genre3.genre is None


def test_genre_eq_function():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert genre1.__eq__(genre2) is True


def test_genre_false_eq_function():
    genre1 = Genre("Comedy")
    genre2 = Genre(" ")
    assert genre1.__eq__(genre2) is False


def test_genre_lt_function():
    genre1 = Genre("Comedy")
    genre2 = Genre("Action")
    assert genre2.__lt__(genre1) is True


def test_genre_false_lt_function():
    genre1 = Genre("Comedy")
    genre2 = Genre("Action")
    assert genre1.__lt__(genre2) is False


# Actor class


def test_actor_init():
    actor1 = Actor("Steve Carell")
    assert repr(actor1) == "<Actor Steve Carell>"
    actor2 = Actor("")
    assert actor2.actor_full_name is None
    actor3 = Actor(42)
    assert actor3.actor_full_name is None


def test_actor_eq_function():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Steve Carell")
    assert actor1.__eq__(actor2) is True


def test_actor_false_eq_function():
    actor1 = Actor("Steve Carell")
    actor2 = Actor(" ")
    assert actor1.__eq__(actor2) is False


def test_actor_lt_function():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    assert actor2.__lt__(actor1) is True


def test_actor_false_lt_function():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    assert actor1.__lt__(actor2) is False

def test_add_actor_colleague():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    actor1.add_actor_colleague(actor2)
    assert actor1.return_actor_colleague() == [actor2]

def test_check_if_this_actor_worked_with():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2) is True

def test_false_check_if_this_actor_worked_with():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    assert actor1.check_if_this_actor_worked_with(actor2) is False

def test_false_2_check_if_this_actor_worked_with():
    actor1 = Actor("Steve Carell")
    actor2 = Actor("Amy Adams")
    actor3 = Actor("Jack Black")
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor3) is False


# Movie class

def test_movie_init():
    movie1 = Movie("Princess and The Frog", 2009)
    assert repr(movie1) == "<Movie Princess and The Frog, 2009>"
    movie2 = Movie("", 0)
    assert movie2.movie_name is None
    movie3 = Movie(42, "")
    assert movie3.movie_name is None


def test_movie_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie("Princess and The Frog", 2009)
    assert movie1.__eq__(movie2) is True


def test_movie_false_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie(" ", 11)
    assert movie1.__eq__(movie2) is False


def test_movie_lt_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie("Spirited Away", 2001)
    assert movie1.__lt__(movie2) is True


def test_movie_false_lt_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie("Spirited Away", 2001)
    assert movie2.__lt__(movie1) is False

def test_movie_add_actor():
    movie1 = Movie("Princess and The Frog", 2009)
    actor1 = Actor("Anika Noni Rose")
    movie1.add_actor(actor1)
    assert movie1.return_actor() == [actor1]

def test_movie_remove_actor():
    movie1 = Movie("Princess and The Frog", 2009)
    actor1 = Actor("Anika Noni Rose")
    actor2 = Actor("Keith David")
    movie1.add_actor(actor1)
    movie1.add_actor(actor2)
    movie1.remove_actor(actor1)
    assert movie1.return_actor() == [actor2]

def test_movie_add_genre():
    movie1 = Movie("Princess and The Frog", 2009)
    genre1 = Genre("Animation")
    movie1.add_genre(genre1)
    assert movie1.return_genre() == [genre1]

def test_movie_remove_genre():
    movie1 = Movie("Princess and The Frog", 2009)
    genre1 = Genre("Animation")
    genre2 = Genre("Musical")
    movie1.add_genre(genre1)
    movie1.add_genre(genre2)
    movie1.remove_genre(genre1)
    assert movie1.return_genre() == [genre2]

def test_movie_runtime_property():
    movie1 = Movie("Princess and The Frog", 2009)
    movie1.runtime_minutes = 98
    assert movie1.runtime_minutes is 98

def test_movie_fail_runtime_property():
    movie1 = Movie("Princess and The Frog", 2009)
    with pytest.raises(ValueError):
        movie1.runtime_minutes = -2
    assert movie1.runtime_minutes is None

def test_movie_title_property():
    movie1 = Movie("Princess and The Frog", 2009)
    movie1.title = " Princess and The Frog "
    assert movie1.title == "Princess and The Frog"

def test_movie_description_property():
    movie1 = Movie("Princess and The Frog", 2009)
    movie1.description = "     The famous tale of Princess and The Frog set in New Orleans with Jazz music and Voodoo. "
    assert movie1.description == "The famous tale of Princess and The Frog set in New Orleans with Jazz music and Voodoo."

def test_movie_director_property():
    movie1 = Movie("Princess and The Frog", 2009)
    director1 = Director("John Musker")
    movie1.director = director1
    assert movie1.director is director1

def test_movie_replace_director_property():
    movie1 = Movie("Princess and The Frog", 2009)
    director1 = Director("John Musker")
    director2 = Director("Ron Clements")
    movie1.director = director1
    movie1.director = director2
    assert movie1.director is director2

def test_movie_actor_property():
    movie1 = Movie("Princess and The Frog", 2009)
    actor1 = Actor("Anika Noni Rose")
    actor2 = Actor("Keith David")
    movie1.actors = actor1
    movie1.actors = actor2
    assert movie1.actors == [actor1, actor2]

def test_movie_genre_property():
    movie1 = Movie("Princess and The Frog", 2009)
    genre1 = Genre("Animation")
    genre2 = Genre("Musical")
    movie1.genres = genre1
    movie1.genres = genre2
    assert movie1.genres == [genre1, genre2]


# TV_Show class

def test_tv_show_init():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    assert repr(tv_show1) == "<TV Show Sailor Moon: Crystal, 2014>"
    tv_show2 = TV_Show("", 0)
    assert tv_show2.tv_show_name is None
    tv_show3 = TV_Show(42, "")
    assert tv_show3.tv_show_name is None


def test_tv_show_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = TV_Show("Sailor Moon: Crystal", 2014)
    assert tv_show1.__eq__(tv_show2) is True


def test_tv_show_false_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = Movie(" ", 11)
    assert tv_show1.__eq__(tv_show2) is False


def test_tv_show_lt_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = TV_Show("Lost", 2004)
    assert tv_show2.__lt__(tv_show1) is True


def test_tv_show_false_lt_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = TV_Show("Lost", 2004)
    assert tv_show1.__lt__(tv_show2) is False

def test_tv_show_add_actor():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    actor1 = Actor("Kotono Mitsuishi")
    tv_show1.add_actor(actor1)
    assert tv_show1.return_actor() == [actor1]

def test_tv_show_remove_actor():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    actor1 = Actor("Kotono Mitsuishi")
    actor2 = Actor("Amanda Celine Miller")
    tv_show1.add_actor(actor1)
    tv_show1.add_actor(actor2)
    tv_show1.remove_actor(actor1)
    assert tv_show1.return_actor() == [actor2]

def test_tv_show_add_genre():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    genre1 = Genre("Animation")
    tv_show1.add_genre(genre1)
    assert tv_show1.return_genre() == [genre1]

def test_tv_show_remove_genre():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    genre1 = Genre("Animation")
    genre2 = Genre("Action")
    tv_show1.add_genre(genre1)
    tv_show1.add_genre(genre2)
    tv_show1.remove_genre(genre1)
    assert tv_show1.return_genre() == [genre2]

def test_tv_show_runtime_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.number_of_episode = 30
    tv_show1.runtime_minutes = 23
    assert tv_show1.runtime_minutes == 690

def test_tv_show_fail_runtime_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.number_of_episode = 30
    with pytest.raises(ValueError):
        tv_show1.runtime_minutes = -2
    assert tv_show1.runtime_minutes is None

def test_tv_show_title_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.title = " Sailor Moon "
    assert tv_show1.title == "Sailor Moon"

def test_tv_show_description_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.description = "     Crime fighting sailor guardians out to protect the legendary silver crystal. "
    assert tv_show1.description == "Crime fighting sailor guardians out to protect the legendary silver crystal."

def test_tv_show_director_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    director1 = Director("Munehisa Sakai")
    tv_show1.director = director1
    assert tv_show1.director is director1

def test_tv_show_replace_director_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    director1 = Director("John Musker")
    director2 = Director("Ron Clements")
    tv_show1.director = director1
    tv_show1.director = director2
    assert tv_show1.director is director2

def test_tv_show_actor_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    actor1 = Actor("Anika Noni Rose")
    actor2 = Actor("Keith David")
    tv_show1.actors = actor1
    tv_show1.actors = actor2
    assert tv_show1.actors == [actor1, actor2]

def test_tv_show_genre_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    genre1 = Genre("Animation")
    genre2 = Genre("Action")
    tv_show1.genres = genre1
    tv_show1.genres = genre2
    assert tv_show1.genres == [genre1, genre2]


#Review

def test_review_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    review2 = Review(movie2, "I really liked it", 9)
    assert review1.__eq__(review2) is True

def test_review_1_false_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    movie2 = Movie("A A", 1989)
    review1 = Review(movie1, "I really liked it", 9)
    review2 = Review(movie2, "I really liked it", 9)
    assert review1.__eq__(review2) is False

def test_review_2_false_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    review2 = Review(movie1, "It was okay", 9)
    assert review1.__eq__(review2) is False

def test_review_3_false_eq_function():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    review2 = Review(movie1, "I really liked it", 8)
    assert review1.__eq__(review2) is False

def test_review_movie_property():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    assert review1.movie is movie1

def test_review_review_text_property():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    assert review1.review_text is "I really liked it"

def test_review_rating_property():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    assert review1.rating is 9

def test_review_timestamp_property():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    assert review1.timestamp == datetime.time

def test_tv_show_review_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    review2 = TV_Show_Review(tv_show2, "I really liked it", 9)
    assert review1.__eq__(review2) is True

def test_tv_show_review_1_false_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show2 = TV_Show("A A", 1989)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    review2 = TV_Show_Review(tv_show2, "I really liked it", 9)
    assert review1.__eq__(review2) is False

def test_tv_show_review_2_false_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    review2 = TV_Show_Review(tv_show1, "It was okay", 9)
    assert review1.__eq__(review2) is False

def test_tv_show_review_3_false_eq_function():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    review2 = TV_Show_Review(tv_show1, "I really liked it", 8)
    assert review1.__eq__(review2) is False

def test_review_tv_show_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    assert review1.tv_show is tv_show1

def test_tv_show_review_review_text_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    assert review1.review_text is "I really liked it"

def test_tv_show_review_rating_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    assert review1.rating is 9

def test_tv_show_review_timestamp_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    assert review1.timestamp == datetime.time


#User

def test_user_init():
    user1 = User("Jenna da Cruz", "testing123")
    assert repr(user1) == "<User jenna da cruz>"
    user2 = User("", " ")
    assert user2.user_name is None
    user3 = User(42, "")
    assert user3.user_name is None


def test_user_eq_function():
    user1 = User("Jenna da Cruz", "testing123")
    user2 = User("Jenna da Cruz", "testing 123")
    assert user1.__eq__(user2) is True


def test_user_false_eq_function():
    user1 = User("Jenna da Cruz", "testing123")
    user2 = User("Jessica da Cruz", "testing1234")
    assert user1.__eq__(user2) is False


def test_user_lt_function():
    user1 = User("Jenna da Cruz", "testing123")
    user2 = User("Jessica da Cruz", "testing1234")
    assert user1.__lt__(user2) is True


def test_user_false_lt_function():
    user1 = User("Jenna da Cruz", "testing123")
    user2 = User("Jessica da Cruz", "testing1234")
    assert user2.__lt__(user1) is False

def test_user_watch_movie():
    movie1 = Movie("Princess and The Frog", 2009)
    movie1.runtime_minutes = 98
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_movie(movie1)
    assert user1.watched_movies == [movie1]
    assert user1.time_spent_watching_movies_minutes is 98

def test_user_add_review():
    movie1 = Movie("Princess and The Frog", 2009)
    review1 = Review(movie1, "I really liked it", 9)
    user1 = User("Jenna da Cruz", "testing123")
    user1.add_review(review1)
    assert user1.reviews == [review1]

def test_user_user_name_property():
    user1 = User("Jenna da Cruz", "testing123")
    assert user1.user_name == "jenna da cruz"

def test_user_password_property():
    user1 = User("Jenna da Cruz", "testing123")
    assert user1.password == "testing123"

def test_user_watched_movies_property():
    movie1 = Movie("Princess and The Frog", 2009)
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_movie(movie1)
    assert user1.watched_movies == [movie1]

def test_user_time_spent_watching_movies_property():
    movie1 = Movie("Princess and The Frog", 2009)
    movie1.runtime_minutes = 98
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_movie(movie1)
    assert user1.time_spent_watching_movies_minutes is 98

def test_user_review_property():
    movie1 = Movie("Princess and The Frog", 2009)
    user1 = User("Jenna da Cruz", "testing123")
    review1 = Review(movie1, "I loved it", 10)
    user1.add_review(review1)
    assert user1.reviews == [review1]

def test_user_watch_tv_show():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.number_of_episode = 30
    tv_show1.runtime_minutes = 23
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_tv_show(tv_show1)
    assert user1.watched_tv_shows == [tv_show1]
    assert user1.time_spent_watching_tv_shows_minutes is 690

def test_user_tv_show_add_review():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    review1 = TV_Show_Review(tv_show1, "I really liked it", 9)
    user1 = User("Jenna da Cruz", "testing123")
    user1.add_tv_review(review1)
    assert user1.tv_show_reviews == [review1]

def test_user_watched_tv_shows_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_tv_show(tv_show1)
    assert user1.watched_tv_shows == [tv_show1]

def test_user_time_spent_watching_tv_shows_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    tv_show1.number_of_episode = 30
    tv_show1.runtime_minutes = 23
    user1 = User("Jenna da Cruz", "testing123")
    user1.watch_tv_show(tv_show1)
    assert user1.time_spent_watching_tv_shows_minutes is 690

def test_user_tv_show_review_property():
    tv_show1 = TV_Show("Sailor Moon: Crystal", 2014)
    user1 = User("Jenna da Cruz", "testing123")
    review1 = TV_Show_Review(tv_show1, "I loved it", 10)
    user1.add_tv_review(review1)
    assert user1.tv_show_reviews == [review1]
