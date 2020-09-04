
class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
            self.__colleague_list = []
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__colleague_list = []

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

    def check_if_this_actor_worked_with(self, colleague):
        if len(self.__colleague_list) > 0:
            for i in self.__colleague_list:
                if i == colleague:
                    return True
            return False
        else:
            return False