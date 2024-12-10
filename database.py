import sqlite3

class Veritabani:
    def __init__(self):
        # Veritabanı bağlantısını kurar
        self.conn = sqlite3.connect('okul.db')
        self.cursor = self.conn.cursor()
        self._tablolar_olustur()

    def _tablolar_olustur(self):
        # Kullanıcılar, öğrenciler, öğretmenler ve loglar tablolarını oluşturur
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
                                id INTEGER PRIMARY KEY,
                                kullanici_adi TEXT NOT NULL,
                                parola TEXT NOT NULL,
                                kullanici_tipi TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ogrenciler (
                                id INTEGER PRIMARY KEY,
                                ogrenci_id TEXT NOT NULL,
                                adi TEXT NOT NULL,
                                sinifi TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ogretmenler (
                                id INTEGER PRIMARY KEY,
                                ogretmen_id TEXT NOT NULL,
                                adi TEXT NOT NULL,
                                bolumu TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS loglar (
                                id INTEGER PRIMARY KEY,
                                zaman TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                eylem TEXT NOT NULL,
                                kullanici_adi TEXT NOT NULL,
                                ek_bilgi TEXT)''')

    def calistir(self, sorgu, parametreler=()):
        # Veritabanında bir sorgu çalıştırır
        self.cursor.execute(sorgu, parametreler)
        self.conn.commit()

    def hepsini_getir(self, sorgu, parametreler=()):
        # Bir sorgunun tüm sonuçlarını getirir
        self.cursor.execute(sorgu, parametreler)
        return self.cursor.fetchall()

    def birini_getir(self, sorgu, parametreler=()):
        # Bir sorgunun tek bir sonucunu getirir
        self.cursor.execute(sorgu, parametreler)
        return self.cursor.fetchone()
