from flix.domainmodel.tv_show import TV_Show

class TV_Show_WatchList:
    def __init__(self):
        self.__watched_tv_shows = []

    def add_tv_show(self, tv_show):
        if isinstance(tv_show, TV_Show):
            if tv_show not in self.__watched_tv_shows:
                self.__watched_tv_shows.append(tv_show)

    def remove_tv_show(self, tv_show):
        if isinstance(tv_show, TV_Show):
            if tv_show in self.__watched_tv_shows:
                self.__watched_tv_shows.remove(tv_show)

    def select_tv_show_to_watch(self, index):
        if index < len(self.__watched_tv_shows)-1 or index > 0 - len(self.__watched_tv_shows):
            return self.__watched_tv_shows[index]
        else:
            return None

    def size(self):
        return len(self.__watched_tv_shows)

    def first_tv_show_in_watchlist(self):
        if len(self.__watched_tv_shows) > 0:
            return self.__watched_tv_shows[0]
        else:
            return None

    def __iter__(self):
        iter(self.__watched_tv_shows)

    def __next__(self):
        next(self.__watched_tv_shows)
