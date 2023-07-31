"""
Hangman:
Klasik bir kelime tahmin oyunudur.
Bilgisayar, rastgele bir kelime seçer ve kullanıcı, harf tahminleri yaparak kelimeyi bulmaya çalışır.
Kullanıcının belirli bir sayıda yanlış tahmin hakkı vardır ve yanlış tahmin sayısı arttıkça, asılan bir adam şekli çizilir.
Kullanıcının kelimeyi tamamlayıp tamamlamadığını kontrol ederek oyunu sonlandırır.
"""

import random

def oyun():
    with open("word_list2.txt", "r") as list: # listeyi açtık
        liste = list.read().split("\n")  # satırlara göre ayırdık ve okuyoruz
        word = random.choice(liste)  # random kelime seçtik
        print(liste)  # ekranda görmek için
        #print(word)  # ekranda görmek için

    hak=len(word)*2

    # Başlangıçta boş bir liste oluşturalım, tahmin edilen harfleri burada toplayacağız.
    tahmin_edilen = []

    while (hak>0):

        # Her döngüde kelimeyi göstermek için bir boşluk dizisi oluşturuyoruz.
        kelime_gosterimi = ""

        # random seçilen kelimenin yerine kaç tane - koyacağımızı hesaplayıp bir taslak veriyoruz
        for harf in word:
            if harf in tahmin_edilen:  # harf tahmin listesinde ise
                kelime_gosterimi += harf + " "  # harfi ekliyoruz
            else:
                kelime_gosterimi += "_ "  # eğer yoksa - koyuyoruz yerine

            # kelime_gosterimi'ni ekrana yazdırıyoruz.
        print(kelime_gosterimi)

        # oyun burda başlıyor

        harf=input("bir harf giriniz: ")   # harf gir

        if harf in word:   # harf kelime içinde geçiyrsa
            tahmin_edilen.append(harf)  # tahmin listesine ekliyoruz

            if set(word) == set(tahmin_edilen):
                print("Tebrikler, kelimeyi buldunuz! Kelime:", word)
                break

        else:
            hak -= 1
            print("Yanlış harf! Kalan hakkınız:", hak)

    if hak == 0:
            print("Maalesef, tahmin hakkınız bitti. Kelime:", word)
oyun()


# set kullanarak sadece benzersiz harfleri elde ediyoruz ve küme türünde olduğu için sıra önemli değil.
"""
 Bu sayede kullanıcının girdiği harfleri tüm harfleri içeren benzersiz bir küme ile karşılaştırarak
 oyunun kazanılıp kazanılmadığını doğru şekilde tespit edebiliyoruz.
"""
