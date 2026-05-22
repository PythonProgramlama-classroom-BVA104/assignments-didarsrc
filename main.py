from oyun_modulu import * #oyun_modulu.py dosyasındaki fonksiyonları kullanmak için içe aktarılır


while True: #kullanıcı çıkış yapana kadar oyun döngüsü devam eder

    print("\n--- ŞANS OYUNLARI ---")
    print("1- Sayı Tahmin")
    print("2- Yazı Tura")
    print("3- Skorlar")
    print("4- Çıkış")

    secim = input("Seç:")



    if secim == "1": #kullanıcı sayı tahmin oyununu seçerse

        ad = input("Adın:")

        puan = sayi_tahmin()

        skor_kaydet(ad,"Sayi Tahmin",puan)



    elif secim == "2": #kullanıcı yazı tura oyununu seçerse

        ad = input("Adın:")

        puan = yazi_tura()

        skor_kaydet(ad,"Yazi Tura",puan)



    elif secim == "3": #kullanıcı skorları görmek isterse

        skor_goster()



    elif secim == "4": #kullanıcı çıkış yapmak isterse

        print("Çıkılıyor")
        break


    else:

        print("Hatalı giriş")