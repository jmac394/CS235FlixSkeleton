from datetime import datetime

from flix.domainmodel.actor import Actor

class Review:
    def __init__(self, movie, review_text: str, rating: int):
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
        self.__movie = movie
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

def make_review(review_text: str, user, movie, timestamp: datetime = datetime.today()):
    review = Review(user, movie, review_text, timestamp)
    user.add_review(review)
    movie.review(review)

    return review
