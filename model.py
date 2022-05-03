STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'

class Igra:
    def __init__(self, geslo: str, crke=[]):
        self.geslo = geslo.upper()
        self.crke = crke
    
    def napacne_crke(self):
        return [i for i in self.crke if i not in self.geslo]
    
    def pravilne_crke(self):
        return [i for i in self.crke if i in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka: str):
        if crka.upper() in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka.upper())
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka.upper() in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open('besede.txt', encoding='utf8') as d:
    bazen_besed = d.read().split('\n')

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)