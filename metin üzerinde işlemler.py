import time
class Dosya():

    def __init__(self):
        
        with open("metin.txt","r",encoding = "utf-8") as file:
            self.dosya_icerigi = file.read()
            kelimeler = self.dosya_icerigi.split()

            self.tüm_kelimeler = list()
            

            for i in kelimeler:

                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.tüm_kelimeler.append(i)
            
    def kelime_sözlügü(self):

        sözlük = set()
        for i in self.tüm_kelimeler:
            sözlük.add(i)

        print("Metindeki Tüm Kelimeler:")
        for i in sözlük:
            print(i)
            print("***************************")

    def frekans(self):
        sayac = dict()
        for i in self.tüm_kelimeler:

            if i in sayac:
                sayac[i]+=1

            else:
                sayac[i] = 1
        
        for anahtar,deger in sayac.items():
            print("{} kelimesi {} tane  bulunmakta".format(anahtar,deger))
            print("******************************")
    
    def seç(self,arama):
        if (arama in self.tüm_kelimeler):
            print("\nAramış olduğunuz {} kelimesi metinde bulunmakta".format(arama))
        else:
            print("Aradığınız kelime metinde bulunmuyor")

    def __str__(self):
        
        return self.dosya_icerigi
        


            
dosya = Dosya()
while True:
    print("""\nMetin Üzerinde İşlemler
    1. Metini görmek için 1'i
    2. Metinde geçen tüm kelimeleri göremk için 2'i
    3. Metinde hangi kelimenin ne kadar geçtiğini görmek için 3 'yi
    4. Metinde kelime aramak için 4'ü
    5. Çıkmak için 5'ü tuşlayın
     """)
    try:
        secim = int(input("Seçiminizi Girin:"))
    except ValueError:
        print("Lütfen bir sayı girin...")
        time.sleep(2)
    
    if (secim==1):
        print(dosya)
        input("Devam etmek için bir tuşa basın")

    elif (secim==2):
        dosya.kelime_sözlügü()
        
        input("Devam etmek için bir tuşa basın\n")

    elif (secim ==3):
        dosya.frekans()
        
        input("Devam etmek için bir tuşa basın\n")

    elif (secim ==4):
        kelime = input("Arayacağınız kelimeyi girin")
        dosya.seç(kelime)
        
    elif (secim ==5):
        print("Çıkış yapılıyor..")
        time.sleep(2)
        break


