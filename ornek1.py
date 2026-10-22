
# siniflar.py dosyasındaki tüm sınıfları bu dosyaya dahil ediyoruz (import)
from siniflar import (
    Hayvan, Kedi, Kopek,
    Calisan, Mudur,
    Karakter, KilicUstasi, Buyucu, SavasciBuyucu
)

print("*" * 50)
print("SEVİYE 1: ÇOK BASİT (Temel Kalıtım)")
print("*" * 50)

# Hayvan, Kedi ve Kopek sınıflarından nesneler (objeler) üretiyoruz
genel_hayvan = Hayvan("Bilinmeyen Canlı")
benim_kedim = Kedi("Pamuk")
benim_kopegim = Kopek("Karabaş")

# Hepsinde aynı 'ses_cikar()' metodu çağrılıyor ama çıktılar farklı (Polimorfizm/Çok Biçimlilik)
print(genel_hayvan.ses_cikar())
print(benim_kedim.ses_cikar())
print(benim_kopegim.ses_cikar())
