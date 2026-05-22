from abc import ABC, abstractmethod 


class Arac(ABC):

    def __init__(self, plaka, marka, model, musait=True): # Araç kiralık mı değil mi kontrolü için musait parametresi ekledik
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.musait = musait

    @abstractmethod
    def gunluk_ucret(self): # Araç türüne göre günlük ücret hesaplamak için abstract method oluşturduk
        pass

    def kirala(self): # Araç kiralama işlemi için kirala methodu oluşturduk
        if self.musait:
            self.musait = False
            print("Araç kiralandı.")
        else:
            print("Araç zaten kiralık.")

    def bilgileri_goster(self): # Araç bilgilerini göstermek için bilgileri_goster methodu oluşturduk
        print(
            f"Plaka:{self.plaka} "
            f"Marka:{self.marka} "
            f"Model:{self.model} "
            f"Durum:{self.musait}"
        )



class Binek(Arac): # Binek araç sınıfı, Arac sınıfından türetilmiş ve gunluk_ucret methodunu implement etmiş bir sınıftır.

    def __init__(self, plaka, marka, model): 
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1000


class Ticari(Arac):

    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1500


class Lux(Arac):

    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 3000