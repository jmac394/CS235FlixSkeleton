import pytest
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

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


class TestDirectorMethods:

    def test_init():
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_eq_function():
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waititi")
        assert director1.__eq__(director2) is True

    def test_false_eq_function():
        director1 = Director("Taika Waititi")
        director2 = Director(" ")
        assert director1.__eq__(director2) is False

    def test_lt_function():
        director1 = Director("Taika Waititi")
        director2 = Director("A A")
        assert director2.__lt__(director1) is True

    def test_false_lt_function():
        director1 = Director("Taika Waititi")
        director2 = Director("A A")
        assert director1.__lt__(director2) is False