# Okul Yönetim Sistemi

Bu proje, bir okul yönetim sistemini uygulayan basit bir Python uygulamasıdır. Sistem, kullanıcıların (yöneticiler ve standart kullanıcılar) öğrencileri ve öğretmenleri eklemesine, listelemesine ve log kayıtlarını Excel dosyasına aktarmasına olanak tanır.

## Proje Yapısı

Proje üç ana dosyadan oluşur:

1. **main.py**: Uygulamanın ana çalışma dosyasıdır. Kullanıcı giriş işlemlerini ve sistemdeki ana işlemleri yönetir.
2. **database.py**: SQLite veritabanı ile etkileşim kurar ve gerekli tabloları oluşturur.
3. **log.py**: Log kayıtlarını yönetir ve Excel dosyasına aktarır.

## Kullanılan Teknolojiler

- Python 3
- SQLite (Veritabanı)
- Pandas (Excel dosyasına veri aktarma)

## Kurulum

1. Gerekli Python bağımlılıklarını yükleyin:
   ```sh
   pip install pandas
   ```

2. Proje dosyalarını aynı dizine yerleştirin:
   - main.py
   - database.py
   - log.py

## Kullanım

Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:
```sh
python main.py
```

### Ana Program Döngüsü

Uygulama çalıştığında ana menü ile karşılaşacaksınız:

1. **Giriş Yap**: Var olan bir kullanıcı hesabı ile sisteme giriş yapar.
2. **Yeni Kullanıcı Oluştur**: Yeni bir kullanıcı hesabı oluşturur.

Giriş yaptıktan sonra aşağıdaki işlemleri gerçekleştirebilirsiniz:

1. **Öğrenci Ekle**: Yeni öğrenci ekler (sadece admin kullanıcılar).
2. **Öğrencileri Listele**: Tüm öğrencileri listeler.
3. **Öğretmen Ekle**: Yeni öğretmen ekler (sadece admin kullanıcılar).
4. **Öğretmenleri Listele**: Tüm öğretmenleri listeler.
5. **Logları Excel'e Kaydet**: Tüm log kayıtlarını bir Excel dosyasına kaydeder (sadece admin kullanıcılar).
6. **Çıkış Yap**: Kullanıcı çıkışı yapar.

## Sınıflar ve Metotlar

### Kullanıcı Sınıfı (Kullanici)

Kullanıcı bilgilerini tutar:
- `__init__(self, kullanici_adi, parola, kullanici_tipi)`: Kullanıcıyı tanımlar.

### Öğrenci Sınıfı (Ogrenci)

Öğrenci bilgilerini tutar:
- `__init__(self, ogrenci_id, adi, sinifi)`: Öğrenciyi tanımlar.

### Öğretmen Sınıfı (Ogretmen)

Öğretmen bilgilerini tutar:
- `__init__(self, ogretmen_id, adi, bolumu)`: Öğretmeni tanımlar.

### Okul Sistemi Sınıfı (OkulSistemi)

Okul yönetim sistemini yönetir:
- `__init__(self)`: Veritabanı ve logger sınıflarını başlatır.
- `kullanici_kaydet(self, kullanici_adi, parola, kullanici_tipi)`: Yeni kullanıcıyı veritabanına kaydeder.
- `giris(self, kullanici_adi, parola)`: Kullanıcı girişini kontrol eder ve oturum açar.
- `yetki_kontrol(self, gereken_yetki)`: Kullanıcının yetkisini kontrol eder.
- `ogrenci_ekle(self, ogrenci_id, adi, sinifi)`: Yeni öğrenci ekler (admin yetkisi gerektirir).
- `ogretmen_ekle(self, ogretmen_id, adi, bolumu)`: Yeni öğretmen ekler (admin yetkisi gerektirir).
- `ogrencileri_listele(self)`: Tüm öğrencileri listeler.
- `ogretmenleri_listele(self)`: Tüm öğretmenleri listeler.
- `cikis(self)`: Kullanıcı çıkışı yapar.
- `loglari_excel_kaydet(self, dosya_adi='loglar.xlsx')`: Logları Excel dosyasına kaydeder (admin yetkisi gerektirir).

### Veritabanı Sınıfı (Veritabani)

Veritabanı ile etkileşim kurar:
- `__init__(self)`: Veritabanı bağlantısını kurar ve tabloları oluşturur.
- `_tablolar_olustur(self)`: Gerekli veritabanı tablolarını oluşturur.
- `calistir(self, sorgu, parametreler=())`: Veritabanında bir sorgu çalıştırır.
- `hepsini_getir(self, sorgu, parametreler=())`: Bir sorgunun tüm sonuçlarını getirir.
- `birini_getir(self, sorgu, parametreler=())`: Bir sorgunun tek bir sonucunu getirir.

### Logger Sınıfı (Logger)

Log kayıtlarını yönetir:
- `__init__(self, db)`: Veritabanı bağlantısını alır.
- `eylem_kaydet(self, eylem, kullanici_adi, *args)`: Bir eylemi loglar tablosuna kaydeder.
- `loglari_excel_kaydet(self, dosya_adi='loglar.xlsx')`: Logları Excel dosyasına kaydeder.

