import random
secenek = ["taş", "kağıt", "makas"]
taş = secenek[0]
kağıt = secenek[1]
makas = secenek[2]
print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
print("Çıkmak isterseniz 'q' basın. \n")

while True:
    secim = input("Taş mı, Kağıt mı, Makas mı? (Çıkmak için: q)\n -->")
    bil_secim= random.choice(secenek)
    if secim == taş:
        if bil_secim == taş:
            print("Bilgisayarın seçimi: Taş \n --> Berabere kaldınız!")
        elif bil_secim == kağıt:
            print("Bilgisayarın seçimi: Kağıt \n --> Kaybettiniz!")
        elif bil_secim == makas:
            print("Bilgisayarın seçimi: Makas \ --> Kazandınız!")
        else: 
            print("Hata!")
            break       
    if secim == kağıt:
        if bil_secim == taş:
            print("Bilgisayarın seçimi: Taş \n --> Kazandınız!")
        elif bil_secim == kağıt:
            print("Bilgisayarın seçimi: Kağıt \n --> Berabere Kaldınız!")
        elif bil_secim == makas:
            print("Bilgisayarın seçimi: Makas \ --> Kaybettiniz!")
        else: 
            print("Hata!")
            break
    if secim == makas:
        if bil_secim == taş:
            print("Bilgisayarın seçimi: Taş \n --> Kaybettiniz!")
        elif bil_secim == kağıt:
            print("Bilgisayarın seçimi: Kağıt \n --> Kazandınız!")
        elif bil_secim == makas:
            print("Bilgisayarın seçimi: Makas \ --> Berabere kalınız!")
        else: 
            print("Hata!")
            break
    if secim == 'q':
        print("Kapatılıyor!")
        break