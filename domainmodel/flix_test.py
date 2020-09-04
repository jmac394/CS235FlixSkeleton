import pytest
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

@pytest.fixture
def test_init(self):
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None


def test_eq_function(self):
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert director1.__eq__(director2) is True


def false_test_eq_function(self):
    director1 = Director("Taika Waititi")
    director2 = Director(" ")
    assert director1.__eq__(director2) is False


def test_lt_function(self):
    director1 = Director("Taika Waititi")
    director2 = Director(" ")
    assert director1.__eq__(director2) is True


def false_test_lt_function(self):
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert director1.__eq__(director2) is False