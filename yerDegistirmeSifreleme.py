import math

def yer_degistirme_sifrele(metin, anahtar):
    turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    # Metnin içindeki sayıları kaldır
    #metin = ''.join(char for char in metin if not char.isdigit())
    #print(metin)
    # Metnin sadece Türkçe alfabede olan küçük harflerini al
    metin = ''.join(char for char in metin.lower() if char in turkish_alphabet)
    print(metin)
    # Metnin uzunluğunu ve satır sayısını hesapla


    metin_uzunlugu = len(metin)
    satir_sayisi = math.ceil(metin_uzunlugu / anahtar)

    # Boşlukları 'b' ile doldur
    metin += 'b' * (satir_sayisi * anahtar - metin_uzunlugu)

    # Şifrelemek için sütunları oluştur
    sutunlar = [''] * anahtar
    for i in range(anahtar):
        for j in range(satir_sayisi):
            sutunlar[i] += metin[i + j * anahtar]

    # Şifreli metni oluştur
    sifre = ''.join(sutunlar)

    return sifre


def yer_degistirme_desifrele(sifre, anahtar):
    # Sifrenin uzunluğunu ve satır sayısını hesapla
    sifre_uzunlugu = len(sifre)
    satir_sayisi = math.ceil(sifre_uzunlugu / anahtar)

    # Sifreli metni sütunlara ayır
    sutunlar = [''] * anahtar
    for i in range(anahtar):
        for j in range(satir_sayisi):
            index = j + i * satir_sayisi
            if index < sifre_uzunlugu:
                sutunlar[i] += sifre[index]

    # Orijinal metni oluştur
    metin = ''
    for i in range(satir_sayisi):
        for j in range(anahtar):
            metin += sutunlar[j][i]

    return metin.strip('b')
