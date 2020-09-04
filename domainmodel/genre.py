import pytest
class Genre:
    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre = None
        else:
            self.__genre = genre.strip()

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

class TestGenreMethods:

    def test_init():
        genre1 = Genre("Comedy")
        assert repr(genre1) == "<Genre Comedy>"
        genre2 = Genre("")
        assert genre2.genre is None
        genre3 = Genre(42)
        assert genre3.genre is None

    def test_g_eq_function():
        genre1 = Genre("Comedy")
        genre2 = Genre("Comedy")
        assert genre1.__eq__(genre2) is True

    def test_false_eq_function():
        genre1 = Genre("Comedy")
        genre2 = Genre(" ")
        assert genre1.__eq__(genre2) is False

    def test_lt_function():
        genre1 = Genre("Comedy")
        genre2 = Genre("Action")
        assert genre2.__lt__(genre1) is True

    def test_false_lt_function():
        genre1 = Genre("Comedy")
        genre2 = Genre("Action")
        assert genre1.__lt__(genre2) is False