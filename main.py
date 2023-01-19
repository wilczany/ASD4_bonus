import hash as h
d = {
    'Włochy',
    'Polska'
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mapa = h.hasz_mapa(20)
    print(mapa.tablica)
    print(mapa.__hash__())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
