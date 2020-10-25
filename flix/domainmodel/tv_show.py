

class TV_Show:
    def __init__(self, tv_show_name: str, release_year: int):
        if tv_show_name == "" or type(tv_show_name) is not str:
            self.__tv_show_name = None
        else:
            self.__tv_show_name = tv_show_name.strip()
        if isinstance(release_year, int):
            if release_year >= 1900:
                self.__release_year = release_year
            else:
                self.__release_year = None
        else:
            self.__release_year = None
        self.__actor_list = []
        self.__genre_list = []
        self.__description = None
        self.__director = None
        self.__runtime = None
        self.__number_of_episodes = 0

    @property
    def tv_show_name(self) -> str:
        return self.__tv_show_name

    def __repr__(self):
        return f"<TV Show {self.__tv_show_name}, {str(self.__release_year)}>"

    def __eq__(self, other):
        if repr(self) == repr(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if repr(self) < repr(other):
            return True
        else:
            return False

    def __hash__(self):
        return hash(repr(self))

    def add_actor(self, actor):
        self.__actor_list.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actor_list:
            self.__actor_list.remove(actor)

    def add_genre(self, genre):
        self.__genre_list.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genre_list:
            self.__genre_list.remove(genre)

    def return_actor(self):
        return self.__actor_list

    def return_genre(self):
        return self.__genre_list

    @property
    def title(self):
        return self.__tv_show_name

    @title.setter
    def title(self, new_name):
        if isinstance(new_name, str):
            self.__tv_show_name = new_name.strip()
        else:
            pass

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            if new_description != "":
                self.__description = new_description.strip()
        else:
            pass

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, new_director):
        self.__director = new_director

    @property
    def actors(self):
        return self.__actor_list

    @actors.setter
    def actors(self, new_actor):
        self.__actor_list.append(new_actor)

    @property
    def genres(self):
        return self.__genre_list

    @genres.setter
    def genres(self, new_genre):
        self.__genre_list.append(new_genre)

    @property
    def runtime_minutes(self):
        return self.__runtime

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if isinstance(runtime, int):
            if runtime > 0:
                self.__runtime = runtime * self.__number_of_episodes
            else:
                raise ValueError()
        else:
            pass

    @property
    def number_of_episode(self):
        return self.__number_of_episodes

    @number_of_episode.setter
    def number_of_episode(self, number_of_episodes):
        if isinstance(number_of_episodes, int):
            if number_of_episodes > 0:
                self.__number_of_episodes = number_of_episodes
            else:
                raise ValueError()
        else:
            pass
