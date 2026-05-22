import random
import csv


def sayi_tahmin(): 

    sayi = random.randint(1,100) #1 ile 100 arasında rastgele bir sayı seçilir
    hak = 7 #kullanıcının 7 hakkı vardır

    while hak > 0: #kullanıcı hakkı olduğu sürece tahmin yapmaya devam eder

        try:
            tahmin = int(input("Tahmin gir: ")) 

            if tahmin == sayi: #kullanıcının tahmini doğruysa
                print("Bildin")
                return 50

            elif tahmin < sayi: #kullanıcının tahmini sayıdan küçükse
                print("Daha büyük")

            else:
                print("Daha küçük") #kullanıcının tahmini sayıdan büyükse

            hak -= 1

        except ValueError: #kullanıcı sayı yerine geçersiz bir giriş yaparsa
            print("Sayı girmen gerekiyor")

    print("Kaybettin") #kullanıcı hakkını kaybettiğinde kaybettiği mesajı gösterilir
    return 0



def yazi_tura(): #kullanıcıya yazı mı tura mı seçmesi istenir

    secim = input("Yazı mı Tura mı: ") #kullanıcının seçimi alınır

    sonuc = random.choice(["yazi","tura"]) #rastgele olarak yazı veya tura seçilir

    if secim.lower() == sonuc: #kullanıcının seçimi ile rastgele seçilen sonuç karşılaştırılır
        print("Kazandın")
        return 20

    else:
        print("Kaybettin")
        return 0



def skor_kaydet(oyuncu, oyun, puan): #skorları kaydetmek için bir fonksiyon oluşturulur 

    with open("skorlar.csv","a") as dosya: 
        dosya.write(f"{oyuncu},{oyun},{puan}\n")



def skor_goster(): #skorları göstermek için bir fonksiyon oluşturulur

    try:

        with open("skorlar.csv","r") as dosya:

            print("\nSKORLAR")

            for satir in dosya:
                print(satir)

    except FileNotFoundError: 

        open("skorlar.csv","w")
        print("Henüz skor yok")