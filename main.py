from utils import secti, obvod_obdelniku


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    vysledek_obvodu_obdelniku = obvod_obdelniku(x,y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Obvod obdelníku je: {vysledek_obvodu_obdelniku}")

if __name__ == '__main__':
    main()