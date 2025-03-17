from utils import secti, obvod_ctverce


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Obvod čtverce {x} je {obvod_ctverce(x)}")
if __name__ == '__main__':
    main()