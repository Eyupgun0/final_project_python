import pandas as pd

class Logger:
    def __init__(self, db):
        # Logger sınıfı, veritabanı bağlantısını alır
        self.db = db

    def eylem_kaydet(self, eylem, kullanici_adi, *args):
        # Bir eylemi loglar tablosuna kaydeder
        bilgi = ', '.join(args)
        self.db.calistir("INSERT INTO loglar (eylem, kullanici_adi, ek_bilgi) VALUES (?, ?, ?)",
                        (eylem, kullanici_adi, bilgi))

    def loglari_excel_kaydet(self, dosya_adi='loglar.xlsx'):
        # Logları Excel dosyasına kaydeder
        loglar = self.db.hepsini_getir("SELECT * FROM loglar")
        df = pd.DataFrame(loglar, columns=['ID', 'Zaman Damgası', 'Eylem', 'Kullanıcı Adı', 'Ek Bilgi'])
        df.to_excel(dosya_adi, index=False)
