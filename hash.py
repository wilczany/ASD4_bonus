def Eukl(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


class HaszMapa:
    hasz = "kwadratowe"

    def __init__(self, size):
        self.rozmiar = size
        self.tablica = [[None, -1] for _ in range(self.rozmiar)]
        self.ilosc = 0
        pass

    def clear(self):
        self.tablica = [None for _ in range(self.rozmiar)]

    def put(self, item, key):
        hasz = self.__haszowanie(key)
        i = 0
        while True:
            if self.tablica[hasz][0] is None:
                self.tablica[hasz][0] = item
                self.tablica[hasz][1] = key
                break
            else:
                # jezeli taki sam klucz to zastepje obiekt
                if self.tablica[hasz][1] == key:
                    self.tablica[hasz][0] = object
                    break
                else:
                    i += 1
                    hasz = self.__haszowanie(key, i)

        return hasz

    def get(self, key):
        hasz = self.__haszowanie(key)
        i = 0
        while True:
            if self.tablica[hasz][1] == key:
                return self.tablica[hasz][0]
            else:
                i += 1
                hasz = self.__haszowanie(key, i)

    def remove(self, key):
        hasz = self.__haszowanie(key)
        i = 0
        if self.tablica[hasz][1] == key:
            return self.tablica[hasz][0]
        else:
            i += 1
            hasz = self.__haszowanie(key, i)

    def __haszowanie(self, klucz, krotka=0) -> int:

        #hasz1() = klucz mod rozmiar
        #hasz2() = wynik funkcji ma być względnie pierwszy z rozmiarem tablicy ?

        if krotka == 0:
            return klucz % self.rozmiar
        coprime = krotka * (klucz %)
        Eukl(self.rozmiar, b)

        return (
                       krotka * (klucz % self.ilosc)
                       + klucz % self.rozmiar - 1
               ) \
               % self.rozmiar

    def show(self):
        i = 0
        for h in range(self.rozmiar):
            if i == self.ilosc:
                break
            if self.tablica[h][0] is not None:
                print("[" + str(h) + "]"
                      + "--->"
                      + "Object: " + str(self.tablica[h][0])
                      + "\tKey: " + str(self.tablica[h][1])
                      )


