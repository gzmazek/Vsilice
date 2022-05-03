import model

def izpis_igre(igra):
    niz = f"""{igra.pravilni_del_gesla()}
    Nepravilni ugibi: {igra.nepravilni_ugibi()}
    Napačno lahko ugibaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1}-krat."""
    return niz

def izpis_zmage(igra):
    niz = f"Čestitke! Pravilo ste uganili besedo {igra.geslo}."
    return niz

def izpis_poraza(igra):
    return f"Več sreče prihodnjič, pravilno geslo je bilo {igra.geslo}." 

def zahtevaj_vnos():
    return input("Ugibaj črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while not igra.zmaga() and not igra.poraz():
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))
    else:
        print(izpis_poraza(igra))

pozeni_vmesnik()