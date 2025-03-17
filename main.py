from utils import secti
from utils import deleni

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    vysledek_deleni=deleni(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Vysledek deleni {x} a {y} je: {vysledek_deleni}")

if __name__ == '__main__':
    main()
