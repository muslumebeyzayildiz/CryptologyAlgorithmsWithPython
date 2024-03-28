import random
#müslümebeyza 56+^%+yıldız
def yerine_koyma_sifrele(metin, anahtar):
    sifrelenmis_metin = ""
    turkce_harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

    for harf in metin.lower():
        if harf != ' ' and harf in turkce_harfler:
            if harf in anahtar:
                sifrelenmis_harf = anahtar[harf]
                sifrelenmis_metin += sifrelenmis_harf
            else:
                sifrelenmis_metin += harf
    return sifrelenmis_metin

def yerine_koyma_desifrele(sifreli_metin, anahtar):
    orijinal_metin = ""
    turkce_harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    for harf in sifreli_metin.lower():
        if harf != ' ' and harf in turkce_harfler:
            for key, value in anahtar.items():
                if value == harf:
                    orijinal_metin += key
                    break
            else:
                orijinal_metin += harf
    return orijinal_metin

def anahtar_olustur():
    anahtar_alfabe = {
        'a': 'm', 'b': 'n', 'c': 'o', 'ç': 'ö', 'd': 'ç', 'e': 'p', 'f': 'r', 'g': 's',
        'ğ': 'l', 'h': 'ş', 'ı': 't', 'i': 'u', 'j': 'ü', 'k': 'v', 'l': 'y', 'm': 'z',
        'n': 'a', 'o': 'b', 'ö': 'c', 'p': 'd', 'r': 'e', 's': 'f', 'ş': 'g', 't': 'ğ',
        'u': 'h', 'ü': 'ı', 'v': 'i', 'y': 'j', 'z': 'k'
    }
    return anahtar_alfabe

