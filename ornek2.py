from siniflar import (
    Hayvan, Kedi, Kopek,
    Calisan, Mudur,
    Karakter, KilicUstasi, Buyucu, SavasciBuyucu
)
# Calisan ve Mudur sınıflarından nesneler üretiyoruz
normal_personel = Calisan("Ahmet Yılmaz", 15000)
yonetici_personel = Mudur("Ayşe Kaya", 35000, "Bilgi İşlem")

# Mudur sınıfı, Calisan sınıfının özelliklerini aldı ve üstüne 'departman' ekledi
print(normal_personel.bilgileri_goster())
print(yonetici_personel.bilgileri_goster())