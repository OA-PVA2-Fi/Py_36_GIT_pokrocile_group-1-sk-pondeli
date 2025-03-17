from utils import secti, obsah_obdelniku

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    vysledek_obsahu_obdelniku = obsah_obdelniku(x,y)
    print(f"Obsah obdélníku je: {vysledek_obsahu_obdelniku}")

if __name__ == '__main__':
    main()