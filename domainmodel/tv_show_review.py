from datetime import datetime

from domainmodel.tv_show import TV_Show

class TV_Show_Review:
    def __init__(self, tv_show: TV_Show, review_text: str, rating: int):
        if tv_show == "" or type(tv_show) is not TV_Show:
            self.__tv_show = None
        else:
            self.__tv_show = tv_show
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
    def tv_show(self) -> str:
        return self.__tv_show

    def __repr__(self):
        return f"<Review {self.__tv_show}, {str(self.__rating)}, {str(self.__timestamp)}, {self.__review_text}>"

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
