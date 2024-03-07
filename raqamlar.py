class HarfSayici:
    def __init__(self):
        self.sesli_harfler = 'aeiou'
        self.sesiz_harfler = 'mkzxbdfghjklpytr'
        self.sayac_sesli = 0
        self.sayac_sesiz = 0

    def kelima_sor(self):
        return input("Soz kirting")
    
    def seslidir(self, harf):
        return harf in self.sesiz_harfler
    
    def sesizdir(self, harf):
        return harf in self.sesiz_harfler
    
    def artir(self):
        for harf in self.kelima:
            if self.seslidir(harf):
                self.sayac_sesiz += 1
            if self.sesizdir(harf):
                self.sayac_sesiz += 1
        return (self.sayac_sesli, self.sayac_sesiz)
    
    def ekrana_bas(self):
        sesli, sesiz = self.artir()
        mesaj = "{} sozlarda {} sesli{}sesiz harfler var."
        print(mesaj.format(self.kelima, sesli,sesiz))

    def claistir(self):
        self.kelima = self.kelima_sor()
        self.ekrana_bas

if __name__ == '_main_':
    sayac = HarfSayici()
    sayac.claistir()