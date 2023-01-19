import random


class hasz_mapa():

    def __init__(self, size):
        self.rozmiar = size
        self.tablica = [None for _ in range(self.rozmiar)]
        pass

    def clear(self):
        self.tablica = [None for _ in range(self.rozmiar)]

    def put(self, object, key):
        hasz = self.__haszowanie(key)
        while True:
            if self.tablica[hasz] is None:
                self.tablica[hasz] = object
                break
            else:
                # rozwiązanie problemu adresowania
                pass
        return hasz

    def get(self, key):
        hasz = self.__haszowanie(key)
        while

        pass

    def remove(self):
        pass

    def __haszowanie(self, klucz) -> int:
        key = random.randint(0, self.rozmiar - 1)

        pass

    def show(self):
        pass