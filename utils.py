import csv
from models import Futbolcu, Basketbolcu, Voleybolcu

class VeriOkuyucu:
    @staticmethod
    def kartlariOku(dosya):
        kartlar = []
        try:
            with open(dosya, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, r in enumerate(reader):
                    if r[0] == "Futbolcu": kartlar.append(Futbolcu(i, *r[1:]))
                    elif r[0] == "Basketbolcu": kartlar.append(Basketbolcu(i, *r[1:]))
                    elif r[0] == "Voleybolcu": kartlar.append(Voleybolcu(i, *r[1:]))
            return kartlar
        except Exception as e:
            print(f"Hata: {e}")
            return []