def karsi_parittomat(lista):
    # Luodaan tyhjä lista, johon tallennetaan parilliset luvut.
    parilliset = []

    # Käydään läpi jokainen luku listassa.
    for luku in lista:
        # Tarkistetaan, onko luku parillinen jakojäännöksen avulla.
        if luku % 2 == 0:
            # Jos luku on parillinen, lisätään se parillisten listaan.
            parilliset.append(luku)

    return parilliset


# Pääohjelma

if __name__ == "__main__":
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista (ilman parittomia lukuja):", karsittu_lista)
