from utils import secti
from utils import odecti

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    vysledek_odcitani = odecti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Výsledek odčítání {x} - {y} je: {vysledek_odcitani}")

if __name__ == '__main__':
    main()