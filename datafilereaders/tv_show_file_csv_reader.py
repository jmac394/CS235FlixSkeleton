import csv

from domainmodel.tv_show import TV_Show
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class TVShowFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_tv_shows = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            tv_show_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in tv_show_file_reader:
                no_tv_show_duplicate = True
                no_actor_duplicate = True
                no_director_duplicate = True
                no_genre_duplicate = True
                title = row['Title']
                release_year = int(row['Year'])
                #print(f"TV Show {index} with title: {title}, release year {release_year}")

                #TV Shows
                tv_show = TV_Show(title, release_year)
                for i in self.dataset_of_tv_shows:
                    if tv_show.__eq__(i):
                        no_tv_show_duplicate = False
                if no_tv_show_duplicate:
                    self.dataset_of_tv_shows.append(tv_show)

                #Actors
                actors = row['Actors']
                actor_list = []
                actors_list = list(actors.split(","))
                for i in actors_list:
                    ind = actors_list.index(i)
                    actors_list[ind] = i.strip()
                    actor_list.append(Actor(actors_list[ind]))
                for actor in actor_list:
                    for j in self.dataset_of_actors:
                        if actor.__eq__(j):
                            no_actor_duplicate = False
                    if no_actor_duplicate:
                        self.dataset_of_actors.append(actor)
                    no_actor_duplicate = True

                #Directors
                directors = row['Director']
                director = Director(directors)
                for i in self.dataset_of_directors:
                    if director.__eq__(i):
                        no_director_duplicate = False
                if no_director_duplicate:
                    self.dataset_of_directors.append(director)

                #Genres
                genres = row['Genre']
                genre_list = []
                genres_list = list(genres.split(","))
                for i in genres_list:
                    ind = genres_list.index(i)
                    genres_list[ind] = i.strip()
                    genre_list.append(Genre(genres_list[ind]))
                for genre in genre_list:
                    for j in self.dataset_of_genres:
                        if genre.__eq__(j):
                            no_genre_duplicate = False
                    if no_genre_duplicate:
                        self.dataset_of_genres.append(genre)
                    no_genre_duplicate = True
                index += 1
