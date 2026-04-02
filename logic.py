import random
from models import KolayStrateji, OrtaStrateji

class OyunYonetici:
    def __init__(self, tum_kartlar):
        self.userWinStreak = 0
        self.userLoseStreak = 0
        self.computerWinStreak = 0
        self.computerLoseStreak = 0
        self.secilen = ""
        self.kullanici_skor = 0
        self.bilgisayar_skor = 0
        self.kullanici_moral = 70
        self.bilgisayar_moral = 70
        self.tur_sirasi = ["Futbol", "Basketbol", "Voleybol"] * 4
        self.tur_sayisi = 0
        self.kullanici_eli, self.bilgisayar_eli = self.kartlari_dagit(tum_kartlar)
        self.bilgisayarOzelYetenek = False
        self.kullaniciOzelYetenek = False

    def kartlari_dagit(self, tum_kartlar):
        random.shuffle(tum_kartlar)
        f = [k for k in tum_kartlar if k.brans == "Futbol"]
        b = [k for k in tum_kartlar if k.brans == "Basketbol"]
        v = [k for k in tum_kartlar if k.brans == "Voleybol"]

        user = f[:4] + b[:4] + v[:4]
        comp = f[4:8] + b[4:8] + v[4:8]
        return user, comp

    def karsilastir(self, u_kart, c_kart, brans):
            self.kullaniciOzelYetenek = False
            self.bilgisayarOzelYetenek = False

            if u_kart is None or c_kart is None:
                return "Hukmen Galibiyet"

            ozellikler_listesi = {
                "Futbol": ["penalti", "serbestVurus", "kaleciKarsiKarsiya"],
                "Basketbol": ["ucluk", "ikilik", "serbestAtis"],
                "Voleybol": ["servis", "blok", "smac"]
            }
            
            ana_ozellik = random.choice(ozellikler_listesi[brans])
            self.secilen = ana_ozellik
            
            u_puan = u_kart.performansHesapla(getattr(u_kart, ana_ozellik), self.kullanici_moral)
            c_puan = c_kart.performansHesapla(getattr(c_kart, ana_ozellik), self.bilgisayar_moral)

            kazanan = None
            
            # Özelliklerin kontrolü
            kontrol_sirasi = [ana_ozellik] + [oz for oz in ozellikler_listesi[brans] if oz != ana_ozellik]
            
            for ozellik in kontrol_sirasi:
                u_val = u_kart.performansHesapla(getattr(u_kart, ozellik), self.kullanici_moral)
                c_val = c_kart.performansHesapla(getattr(c_kart, ozellik), self.bilgisayar_moral)
                
                if u_val > c_val:
                    kazanan = "USER"
                    break
                elif c_val > u_val:
                    kazanan = "COMP"
                    break

            # Özel Yetenek Kontrolü
            if kazanan is None:
                u_ozel = getattr(u_kart, "ozelYetenek", 0)
                c_ozel = getattr(c_kart, "ozelYetenek", 0)
                if u_ozel > c_ozel: 
                    kazanan = "USER"
                    self.kullaniciOzelYetenek = True
                elif c_ozel > u_ozel: 
                    kazanan = "COMP"
                    self.bilgisayarOzelYetenek = True

            # Dayanıklılık Kontrolü
            if kazanan is None:
                if u_kart.dayaniklilik > c_kart.dayaniklilik: kazanan = "USER"
                elif c_kart.dayaniklilik > u_kart.dayaniklilik: kazanan = "COMP"

            # Enerji Kontrolü
            if kazanan is None:
                if u_kart.enerji > c_kart.enerji: kazanan = "USER"
                elif c_kart.enerji > u_kart.enerji: kazanan = "COMP"

            # SEviye Kontrolü
            if kazanan is None:
                if u_kart.seviye > c_kart.seviye: kazanan = "USER"
                elif c_kart.seviye > u_kart.seviye: kazanan = "COMP"

            # -----------------------------
            
            if kazanan == "USER":
                self.userWinStreak += 1
                self.userLoseStreak = 0
                self.computerWinStreak = 0
                self.computerLoseStreak += 1
                
                if self.kullaniciOzelYetenek == True: self.kullanici_skor += 15
                if self.computerLoseStreak >= 2: self.bilgisayar_moral -= 5
                if self.userWinStreak >= 2: self.kullanici_moral += 10
                if self.userWinStreak >= 3: self.kullanici_moral += 15
                
                self.kullanici_skor += u_puan
                u_kart.enerji -= 5
                c_kart.enerji -= 10
                
                return "KAZANDIN"

            elif kazanan == "COMP":
                self.userWinStreak = 0
                self.userLoseStreak += 1
                self.computerWinStreak += 1
                self.computerLoseStreak = 0
                
                if self.bilgisayarOzelYetenek == True: self.bilgisayar_skor += 15
                if self.userLoseStreak >= 2: self.kullanici_moral -= 5
                if self.computerWinStreak >= 2: self.bilgisayar_moral += 10
                if self.computerWinStreak >= 3: self.bilgisayar_moral += 15
                
                self.bilgisayar_skor += c_puan
                u_kart.enerji -= 10
                c_kart.enerji -= 5
                return "KAYBETTİN"

            else:
                u_kart.enerji -= 3
                c_kart.enerji -= 3
                return "BERABERLİK"