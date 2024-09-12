def pääohjelma():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")

        valinta = input("Syötä valintasi (1/2/3): ")

        if valinta == "1":
            icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
            nimi = input("Syötä lentoaseman nimi: ")

            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

        elif valinta == "2":
            icao = input("Syötä haettava ICAO-koodi: ").upper()

            if icao in lentoasemat:
                print(f"Lentoaseman nimi: {lentoasemat[icao]}")
            else:
                print("Lentoaseman ICAO-koodia ei löytynyt.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")

pääohjelma()