from entities import * # entities.py dosyasından tüm sınıfları içe aktarıyoruz


araclar = [ # araç listesi oluşturuyoruz ve her araç türünden birer örnek ekliyoruz
    Binek("34ABC01", "Toyota", "Corolla"),
    Ticari("34XYZ22", "Ford", "Transit"),
    Lux("34LUX99", "BMW", "X5")
]


toplam_gelir = 0 # toplam geliri takip etmek için bir değişken oluşturuyoruz


while True: #kullanıcıdan seçim yapmasını istiyoruz

    print("\n--- ARAÇ KİRALAMA SİSTEMİ ---")
    print("1- Kiralanabilir araçları listele")
    print("2- Araç kirala")
    print("3- Toplam günlük gelir")
    print("4- Çıkış")

    secim = input("Seçim:") 

    if secim == "1": 

        for arac in araclar:
            if arac.musait:
                arac.bilgileri_goster()
                print("Ücret:", arac.gunluk_ucret())

    elif secim == "2":

        plaka = input("Plaka gir:")

        bulundu = False

        for arac in araclar: # araç listesinde kullanıcı tarafından girilen plakaya sahip aracı bulmaya çalışıyoruz

            if arac.plaka == plaka:

                arac.kirala()
                toplam_gelir += arac.gunluk_ucret()
                bulundu = True

        if bulundu == False:
            print("Araç bulunamadı")

    elif secim == "3":

        print("Toplam gelir:", toplam_gelir, "TL")

    elif secim == "4":

        print("Çıkış yapılıyor...")
        break

    else:
        print("Hatalı seçim")