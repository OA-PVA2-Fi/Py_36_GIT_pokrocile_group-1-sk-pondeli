from utils import secti, prevod_na_procenta


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print('číslo', x,'je v procentech',prevod_na_procenta(x),'%')
    print('číslo', y,'je v procentech',prevod_na_procenta(y),'%')
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

if __name__ == '__main__':
    main()