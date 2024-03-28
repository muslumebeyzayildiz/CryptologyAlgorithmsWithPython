from dortKareAlgoritmasi import dortKareSifrele, dortKareDesifrele
from rotaSifreleme import route_encrypt
from vigenereAlgoritmasi import vigenere_sifrele, vigenere_desifrele
from yerDegistirmeSifreleme import yer_degistirme_sifrele, yer_degistirme_desifrele
from permütasyonSifreleme import permutation_cipher
from yerineKoyma import anahtar_olustur, yerine_koyma_sifrele, yerine_koyma_desifrele
from zigzagSifreleme import zigzag_cipher, zigzag_decipher


#  müslümebeyzayıldız
# boşlukları, sayıları ve özel kkaarakterleri atlayarak türkçe alfabedeki küçük harfe çeviriuor
# müSLüme123 BeYZA+%+%&% yıldız
def main():
    #CTRL / İLE TOPLU YORUM SATIRI OLUŞTURMA KALDIRMA

    metin = input("YERİNE KOYMA ALGORİTMASIYLA Şifrelemek istediğiniz metni girin: ")
    anahtar = anahtar_olustur()
    print("Oluşturulan anahtar:", anahtar)
    sifrelenmis_metin = yerine_koyma_sifrele(metin, anahtar)
    print("Şifrelenmiş metin:", sifrelenmis_metin)
    orijinal_metin = yerine_koyma_desifrele(sifrelenmis_metin, anahtar)
    print("Orijinal metin:", orijinal_metin)

    print("*********************************************")

    key = "346215"
    message = input("PERMÜTASYON ŞİFRELEMEYLE Şifrelemek istediğiniz metni girin: ")
    encrypted = permutation_cipher(message, key)
    print(encrypted)
    decrypted = permutation_cipher(encrypted, key, decrypt=True)
    print(decrypted)

    print("*********************************************")

    metin = input("YER DEĞİŞTİRME-SAYI ANAHTARLI- ŞİFRELEMEYLE Şifrelemek istediğiniz metni girin: ")
    anahtar = int(input("anahtarı girin: "))
    #anahtar = 5
    sifrelenmis_metin = yer_degistirme_sifrele(metin, anahtar)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)
    orijinal_metin = yer_degistirme_desifrele(sifrelenmis_metin, anahtar)
    print("Orijinal Metin:", orijinal_metin)

    print("*********************************************")


    plain_text = input("ROTA ŞİFRELEMEYLE Şifrelemek istediğiniz metni girin: ")
    step_size = int(input("anahtarı girin: "))
    encrypted_text = route_encrypt(plain_text,step_size)
    print("Encrypted Text:",encrypted_text)

    print("*********************************************")

    metin = input("ZİGZAG ŞİFRELEMEYLE Şifrelemek istediğiniz metni girin: ")
    anahtar_sayisi = int(input("anahtarı girin: "))
    sifrelenmis_metin = zigzag_cipher(metin, anahtar_sayisi)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)
    orijinal_metin = zigzag_decipher(sifrelenmis_metin, anahtar_sayisi)
    print("Orijinal Metin:", orijinal_metin)

    print("*********************************************")

    metin = input("VIGENERE ALGORİTMASIYLA Şifrelemek istediğiniz metni girin: ")
    anahtar = input("anahtar olacak -STRING- metni  girin: ")
    sifrelenmis_metin = vigenere_sifrele(metin, anahtar)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)
    orijinal_metin = vigenere_desifrele(sifrelenmis_metin, anahtar)
    print("Orijinal Metin:", orijinal_metin)

    print("*********************************************")

    # müSLüme123 BeYZA+%+%&% yıldız
    metin = input("DÖRT KARE ALGORİTMASIYLA Şifrelenecek metni girin: ")
    sifrelenmis_metin = dortKareSifrele(metin)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)
    orijinal_metin = dortKareDesifrele(sifrelenmis_metin)
    if orijinal_metin is not None:
        print("Orijinal Metin:", orijinal_metin)



if __name__ == "__main__":
    main()
