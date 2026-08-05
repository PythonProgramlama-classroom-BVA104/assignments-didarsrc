#Ürünlerin olduğu liste
urunler = []

# Her biri dictionary min 3 ürün ekleyelim 
urunler.append({"ad": "Elma", "fiyat": 10, "stok": 20})
urunler.append({"ad": "Süt", "fiyat": 25, "stok": 3})
urunler.append({"ad": "Ekmek", "fiyat": 7, "stok": 2})

print("Ürün Listesi:")
for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']} TL, Stok: {urun['stok']}")

print("\nKritik Stok Uyarıları:")
for urun in urunler:
    if urun["stok"] < 5:
        print(f" {urun['ad']} için kritik stok! (Stok: {urun['stok']})")

# Toplam stok değerini hesaplama
toplam_deger = 0
for urun in urunler:
    toplam_deger += urun["fiyat"] * urun["stok"]

print(f"\nToplam Stok Değeri: {toplam_deger} TL")