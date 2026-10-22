# Sadece Kılıç Ustası olan bir karakter
from siniflar import (
    Hayvan, Kedi, Kopek,
    Calisan, Mudur,
    Karakter, KilicUstasi, Buyucu, SavasciBuyucu
)

savasci = KilicUstasi("Garen", 1000)
print(savasci.saldir())
print(savasci.kilic_vur())
# savasci.buyu_yap("Buz") # Bu kod HATA verir çünkü Savaşçı büyü yapamaz!

print("-" * 30)

# Hem savaşçı hem büyücü olan melez (Çoklu Kalıtım) karakter nesnesi
melez_kahraman = SavasciBuyucu("Geralt", 1500, 200)

# Üst sınıfların metotlarına erişim (Karakter sınıfından geldi)
print(melez_kahraman.saldir())

# Hem KilicUstasi hem de Buyucu metotlarına sorunsuz erişebilir!
print(melez_kahraman.kilic_vur())
print(melez_kahraman.buyu_yap("Şimşek"))

print("-" * 15 + " ÖZEL GÜÇ " + "-" * 15)
# SavasciBuyucu sınıfının kendisine ait metodu
print(melez_kahraman.ozel_saldiri())