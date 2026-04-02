from abc import ABC, abstractmethod
import random


class Sporcu(ABC):
    def __init__(self, id, ad, takim, brans, day, en, yetenek):
        self.sporcuID = id
        self.sporcuAdi = ad
        self.sporcuTakim = takim
        self.brans = brans
        self.enerji = int(en)
        self.maxEnerji = int(en)
        self.dayaniklilik = int(day)
        self.seviye = 1
        self.deneyimPuani = 0
        self.ozelYetenek = yetenek
        self.kartKullanildiMi = False
        self.moral_bonusu = 0

    def performansHesapla(self, temel_stat, moral):
        ceza = 0
        if 40 <= self.enerji <= 70:
            ceza = temel_stat * 0.10
        elif 0 < self.enerji < 40:
            ceza = temel_stat * 0.20

        if 80 <= moral <= 100:
            self.moral_bonusu = 10
        elif 50 <= moral < 79:
            self.moral_bonusu = 5
        else:
            self.moral_bonusu = -5

        seviye_bonusu = (self.seviye - 1) * 5
        return temel_stat + self.moral_bonusu + seviye_bonusu - ceza


class Futbolcu(Sporcu):
    def __init__(self, id, ad, takim, pen, ser, kal, day, en, yetenek):
        super().__init__(id, ad, takim, "Futbol", day, en, yetenek)
        self.penalti, self.serbestVurus, self.kaleciKarsiKarsiya = int(pen), int(ser), int(kal)


class Basketbolcu(Sporcu):
    def __init__(self, id, ad, takim, uc, iki, ser, day, en, yetenek):
        super().__init__(id, ad, takim, "Basketbol", day, en, yetenek)
        self.ucluk, self.ikilik, self.serbestAtis = int(uc), int(iki), int(ser)


class Voleybolcu(Sporcu):
    def __init__(self, id, ad, takim, ser, blok, smac, day, en, yetenek):
        super().__init__(id, ad, takim, "Voleybol", day, en, yetenek)
        self.servis, self.blok, self.smac = int(ser), int(blok), int(smac)


class KartSecmeStratejisi(ABC):
    @abstractmethod
    def kartSec(self, eldeki_kartlar, brans): pass


class KolayStrateji(KartSecmeStratejisi):
    def kartSec(self, eldeki_kartlar, brans):
        uygun = [k for k in eldeki_kartlar if k.brans == brans and k.enerji > 0]
        return random.choice(uygun) if uygun else None


class OrtaStrateji(KartSecmeStratejisi):
    def kartSec(self, eldeki_kartlar, brans):
        uygun = [k for k in eldeki_kartlar if k.brans == brans and k.enerji > 0]
        return max(uygun, key=lambda k: k.enerji) if uygun else None
