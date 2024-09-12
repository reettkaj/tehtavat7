vuodenajat = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi"
)

def paohjelma():
    kuukausi = int(input("Anna kuukauden numero (1-12): "))

    if 1 <= kuukausi <= 12:
        vuodenaika = vuodenajat[kuukausi - 1]
        print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")
    else:
        print("Virheellinen kuukauden numero. Anna numero väliltä 1-12.")

paohjelma()