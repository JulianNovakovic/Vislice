import model


def izpis_igre(igra):
    tekst = f'''########################################\n
    {igra.pravilni_del_gesla()}\n
    Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n
    Nepravilne črke: {igra.nepravili_ugibi()}
    ########################################\n'''
    return tekst

def izpis_zmage(igra):
    tekst = f'''########################################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
    ########################################\n'''
    return tekst

def izpis_poraza(igra):
    tekst = f"""########################################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo()}\n
    ########################################\n"""
    return tekst

def zahtevaj_vnos():
    return input('Vnesite črko:')

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))

pozeni_vmesnik()