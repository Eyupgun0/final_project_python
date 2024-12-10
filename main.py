from database import Veritabani  # Veritabani sınıfını içeren modülü import ediyoruz.
from log import Logger  # Logger sınıfını içeren modülü import ediyoruz.

# Kullanıcı sınıfı
class Kullanici:
    def __init__(self, kullanici_adi, parola, kullanici_tipi):
        self.kullanici_adi = kullanici_adi  # Kullanıcının adı
        self.parola = parola  # Kullanıcının parolası
        self.kullanici_tipi = kullanici_tipi  # Kullanıcının tipi (admin/standart)

# Öğrenci sınıfı
class Ogrenci:
    def __init__(self, ogrenci_id, adi, sinifi):
        self.ogrenci_id = ogrenci_id  # Öğrencinin ID'si
        self.adi = adi  # Öğrencinin adı
        self.sinifi = sinifi  # Öğrencinin sınıfı

# Öğretmen sınıfı
class Ogretmen:
    def __init__(self, ogretmen_id, adi, bolumu):
        self.ogretmen_id = ogretmen_id  # Öğretmenin ID'si
        self.adi = adi  # Öğretmenin adı
        self.bolumu = bolumu  # Öğretmenin bölümü

# Okul sistemi sınıfı
class OkulSistemi:
    def __init__(self):
        self.db = Veritabani()  # Veritabanı bağlantısı
        self.logger = Logger(self.db)  # Logger sınıfı, veritabanı bağlantısıyla
        self.giris_yapan_kullanici = None  # Giriş yapan kullanıcı bilgisi başlangıçta boş

    def kullanici_kaydet(self, kullanici_adi, parola, kullanici_tipi):
        # Yeni kullanıcıyı veritabanına kaydeder
        self.db.calistir("INSERT INTO kullanicilar (kullanici_adi, parola, kullanici_tipi) VALUES (?, ?, ?)",
                        (kullanici_adi, parola, kullanici_tipi))  # SQL sorgusu ile yeni kullanıcı ekler

    def giris(self, kullanici_adi, parola):
        # Kullanıcı girişini kontrol eder
        kullanici = self.db.birini_getir("SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND parola = ?", (kullanici_adi, parola))  # SQL sorgusu ile kullanıcı bilgilerini kontrol eder
        if kullanici:
            # Kullanıcı bilgileri doğruysa giriş yapar
            self.giris_yapan_kullanici = Kullanici(kullanici[1], kullanici[2], kullanici[3])  # Kullanıcı bilgilerini Kullanici sınıfında saklar
            print("Giriş başarılı.")
        else:
            print("Kullanıcı adı veya parola hatalı.")

    def yetki_kontrol(self, gereken_yetki):
        # Kullanıcının yetkisini kontrol eder
        if self.giris_yapan_kullanici.kullanici_tipi != gereken_yetki:
            # Gerekli yetkiye sahip değilse uyarı mesajı verir
            print(f"Bu işlemi yapabilmek için {gereken_yetki} yetkisine sahip olmanız gerekiyor.")
            return False
        return True

    def ogrenci_ekle(self, ogrenci_id, adi, sinifi):
        # Yeni öğrenci ekler, sadece admin yetkisine sahip kullanıcılar ekleyebilir
        if not self.yetki_kontrol('admin'):
            return  # Yetkisi olmayan kullanıcı işlem yapamaz
        self.db.calistir("INSERT INTO ogrenciler (ogrenci_id, adi, sinifi) VALUES (?, ?, ?)",
                        (ogrenci_id, adi, sinifi))  # SQL sorgusu ile yeni öğrenci ekler
        self.logger.eylem_kaydet("Ogrenci Ekle", self.giris_yapan_kullanici.kullanici_adi, adi, sinifi)  # Log kaydı oluşturur
        print("Yeni öğrenci eklendi.")

    def ogretmen_ekle(self, ogretmen_id, adi, bolumu):
        # Yeni öğretmen ekler, sadece admin yetkisine sahip kullanıcılar ekleyebilir
        if not self.yetki_kontrol('admin'):
            return  # Yetkisi olmayan kullanıcı işlem yapamaz
        self.db.calistir("INSERT INTO ogretmenler (ogretmen_id, adi, bolumu) VALUES (?, ?, ?)",
                        (ogretmen_id, adi, bolumu))  # SQL sorgusu ile yeni öğretmen ekler
        self.logger.eylem_kaydet("Ogretmen Ekle", self.giris_yapan_kullanici.kullanici_adi, adi, bolumu)  # Log kaydı oluşturur
        print("Yeni öğretmen eklendi.")

    def ogrencileri_listele(self):
        # Öğrencileri listeler
        ogrenciler = self.db.hepsini_getir("SELECT * FROM ogrenciler")  # Veritabanından tüm öğrencileri çeker
        for ogrenci in ogrenciler:
            print(f"ID: {ogrenci[1]}, Adı: {ogrenci[2]}, Sınıfı: {ogrenci[3]}")  # Her öğrenciyi listeler

    def ogretmenleri_listele(self):
        # Öğretmenleri listeler
        ogretmenler = self.db.hepsini_getir("SELECT * FROM ogretmenler")  # Veritabanından tüm öğretmenleri çeker
        for ogretmen in ogretmenler:
            print(f"ID: {ogretmen[1]}, Adı: {ogretmen[2]}, Bölümü: {ogretmen[3]}")  # Her öğretmeni listeler

    def cikis(self):
        # Kullanıcı çıkışı
        self.giris_yapan_kullanici = None  # Giriş yapan kullanıcı bilgilerini sıfırlar
        print("Çıkış yapıldı.")

    def loglari_excel_kaydet(self, dosya_adi='loglar.xlsx'):
        # Logları Excel dosyasına kaydeder, sadece admin yetkisine sahip kullanıcılar yapabilir
        if not self.yetki_kontrol('admin'):
            return  # Yetkisi olmayan kullanıcı işlem yapamaz
        self.logger.loglari_excel_kaydet(dosya_adi)  # Logları Excel dosyasına kaydeder
        print(f"Loglar {dosya_adi} dosyasına kaydedildi.")

# Ana program döngüsü
def main():
    okul_sistemi = OkulSistemi()  # OkulSistemi sınıfını başlatır

    while True:
        print("\nHoş geldiniz!")
        if not okul_sistemi.giris_yapan_kullanici:
            # Kullanıcı giriş yapmamışsa veya yeni kullanıcı oluşturma ekranı
            print("1. Giriş Yap")
            print("2. Yeni Kullanıcı Oluştur")
            secim = input("Seçiminizi yapın (1/2): ")

            if secim == "1":
                kullanici_adi = input("Kullanıcı adı: ")
                parola = input("Parola: ")
                okul_sistemi.giris(kullanici_adi, parola)  # Giriş işlemi
            elif secim == "2":
                kullanici_adi = input("Yeni kullanıcı adı: ")
                parola = input("Yeni parola: ")
                kullanici_tipi = input("Kullanıcı tipi (admin/standart): ")
                okul_sistemi.kullanici_kaydet(kullanici_adi, parola, kullanici_tipi)  # Yeni kullanıcı oluşturma işlemi
            else:
                print("Geçersiz seçim.")
        else:
            # Kullanıcı giriş yapmışsa yapılacak işlemler listesi
            print("İşlemler:")
            print("1. Öğrenci Ekle")
            print("2. Öğrencileri Listele")
            print("3. Öğretmen Ekle")
            print("4. Öğretmenleri Listele")
            if okul_sistemi.giris_yapan_kullanici.kullanici_tipi == 'admin':
                print("5. Logları Excel'e Kaydet")
            print("6. Çıkış Yap")
            secim = input("Seçiminizi yapın : ")

            if secim == "1":
                ogrenci_id = input("Öğrenci ID: ")
                adi = input("Adı Soyadı: ")
                sinifi = input("Sınıfı: ")
                okul_sistemi.ogrenci_ekle(ogrenci_id, adi, sinifi)  # Öğrenci ekleme işlemi
            elif secim == "2":
                okul_sistemi.ogrencileri_listele()  # Öğrencileri listeleme işlemi
            elif secim == "3":
                ogretmen_id = input("Öğretmen ID: ")
                adi = input("Adı Soyadı: ")
                bolumu = input("Bölümü: ")
                okul_sistemi.ogretmen_ekle(ogretmen_id, adi, bolumu)  # Öğretmen ekleme işlemi
            elif secim == "4":
                okul_sistemi.ogretmenleri_listele()  # Öğretmenleri listeleme işlemi
            elif secim == "5" and okul_sistemi.giris_yapan_kullanici.kullanici_tipi == 'admin':
                dosya_adi = input("Dosya adı (varsayılan: loglar.xlsx): ")
                if dosya_adi == "":
                    dosya_adi = 'loglar.xlsx'
                okul_sistemi.loglari_excel_kaydet(dosya_adi)  # Logları Excel dosyasına kaydetme işlemi
            elif secim == "6":
                okul_sistemi.cikis()  # Çıkış yapma işlemi
            else:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    main()  # Ana programı başlatır
