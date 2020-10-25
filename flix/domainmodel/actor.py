


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
            self.__colleague_list = []
            self.__movie_list = []
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__colleague_list = []
            self.__movie_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleague_list.append(colleague)

    def return_actor_colleague(self):
        return self.__colleague_list

    def movie_list(self):
        return self.__movie_list

    def check_if_this_actor_worked_with(self, colleague):
        if len(self.__colleague_list) > 0:
            for i in self.__colleague_list:
                if i == colleague:
                    return True
            return False
        else:
            return False

    def is_applied_to(self, movie) -> bool:
        return movie in self.__movie_list

    def add_movie(self, movie):
        self.__movie_list.append(movie)

def make_actor_association(movie, actor: Actor):
    if actor.is_applied_to(movie):
        raise ModelException(f'Tag {actor.actor_full_name} already applied to Movie "{movie.title}"')

    movie.add_actor(actor)
    actor.add_movie(movie)
