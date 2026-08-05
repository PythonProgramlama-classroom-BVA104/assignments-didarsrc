def uzunluk_kontrol(sifre):
    return len(sifre) >= 8


def buyuk_harf_kontrol(sifre):
    return any(harf.isupper() for harf in sifre)


def kucuk_harf_kontrol(sifre):
    return any(harf.islower() for harf in sifre)


def rakam_kontrol(sifre):
    return any(harf.isdigit() for harf in sifre)


def sifre_kontrol(sifre):
    eksikler = []

    if not uzunluk_kontrol(sifre):
        eksikler.append("Şifre en az 8 karakter olmalıdır.")

    if not buyuk_harf_kontrol(sifre):
        eksikler.append("Şifre en az 1 büyük harf içermelidir.")

    if not kucuk_harf_kontrol(sifre):
        eksikler.append("Şifre en az 1 küçük harf içermelidir.")

    if not rakam_kontrol(sifre):
        eksikler.append("Şifre en az 1 rakam içermelidir.")

    return eksikler

# Kullanıcıdan şifre alma
sifre = input("Şifrenizi girin: ")

# Şifreyi kontrol etme
sonuc = sifre_kontrol(sifre)

if len(sonuc) == 0:
    print("Şifre Doğru")
else:
    print(" Şifre Doğru Değil")
    print("Eksik kurallar:")
    for kural in sonuc:
        print("-", kural)