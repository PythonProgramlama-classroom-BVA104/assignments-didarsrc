# Kişisel Bilgi Yönetim Sistemi


ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
yas = int(input("Yaşınızı girin: "))
sehir = input("Şehrinizi girin: ")
meslek = input("Mesleğinizi girin: ")

bes_yil_sonra_yas = yas + 5
toplam_harf = len(ad) + len(soyad)

print("\n--- Kişisel Bilgi Özeti ---")
print(f"Ad Soyad: {ad} {soyad}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")
print(f"Meslek: {meslek}")
print(f"5 yıl sonraki yaşınız: {bes_yil_sonra_yas}")
print(f"Ad ve soyadınızdaki toplam harf sayısı: {toplam_harf}")