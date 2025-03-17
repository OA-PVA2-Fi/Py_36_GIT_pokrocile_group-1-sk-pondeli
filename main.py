from utils import secti
from utils import nasobeni

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Výsledek násobení {x} a {y} je: {nasobeni(x, y)}")
if __name__ == '__main__':
    main()