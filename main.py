from utils import secti, odmocnovani


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Odmocnina z",x,"a z",y," je",{odmocnovani(x,y)})

if __name__ == '__main__':
    main()
