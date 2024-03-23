import random
def yerine_koyma_sifrele(metin, anahtar):
    sifrelenmis_metin = ""
    for harf in metin:
        if harf in anahtar:
            sifrelenmis_harf = anahtar[harf]
            sifrelenmis_metin += sifrelenmis_harf
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

def yerine_koyma_desifrele(sifreli_metin, anahtar):
    orijinal_metin = ""
    for harf in sifreli_metin:
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

