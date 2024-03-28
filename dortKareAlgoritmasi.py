#Matrislerin Tanımlanması

alfabetikSolUst_kare = [
    ['a', 'b', 'c', 'ç', 'd', 'e'],
    ['f', 'g', 'ğ', 'h', 'ı', 'i'],
    ['j', 'k', 'l', 'm', 'n', 'o'],
    ['ö', 'p', 'r', 's', 'ş', 't'],
    ['u', 'ü', 'v', 'y', 'z', 'x']
]
alfabetikSagAlt_kare = [
    ['a', 'b', 'c', 'ç', 'd', 'e'],
    ['f', 'g', 'ğ', 'h', 'ı', 'i'],
    ['j', 'k', 'l', 'm', 'n', 'o'],
    ['ö', 'p', 'r', 's', 'ş', 't'],
    ['u', 'ü', 'v', 'y', 'z', 'x']
]

karisikSagUst_kare = [
    ['j', 'ö', 'x', 't', 'y', 'z'],
    ['v', 'd', 'o', 'l', 'ş', 'ç'],
    ['g', 'ü', 'b', 'i', 'k', 'r'],
    ['u', 'f', 'h', 's', 'a', 'ğ'],
    ['c', 'p', 'm', 'ı', 'n', 'e']
]

karisikSolAlt_kare = [
    ['d', 'g', 'o', 'e', 't', 'n'],
    ['j', 'p', 'ç', 'l', 'ü', 'ı'],
    ['a', 'ş', 'v', 'f', 's', 'c'],
    ['u', 'h', 'x', 'z', 'ğ', 'm'],
    ['r', 'i', 'ö', 'b', 'y', 'k']
]

def dortKareSifrele(metin):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    metin = ''.join(char for char in metin.lower() if char in alfabe)
    # Metni ikişer ikişer böler
    metin = metin if len(metin) % 2 == 0 else metin + 'b'
    #for i in range(0, len(metin), 2): Bu ifade, metnin her iki karakterinde birer adım atarak bir döngü oluşturur.
    # Yani, metnin indekslerini sıfırdan başlayarak metnin uzunluğuna kadar ikişer ikişer artırır. Bu, her döngü adımında i değişkeni bir çift harf için başlangıç indeksini belirtir.
    ciftler = [metin[i:i + 2] for i in range(0, len(metin), 2)]
    # metin[i:i + 2]: Bu ifade, her döngü adımında metindeki i indeksinden başlayarak iki karakter alır.
    # Yani, metnin i indeksinden başlayarak bir sonraki indekse kadar olan iki karakterlik bir alt dizeyi alır.
    # çift karakterlerin oluşturduğu bir listeyi üretecektir.

    sifrelenmis_metin = ''
    for cift in ciftler:
        ilk_harf = cift[0]
        ikinci_harf = cift[1]

        # İlk karakterin konumunu bul
        row_index = next((i for i, row in enumerate(alfabetikSolUst_kare) if ilk_harf in row), None)
        # enumerate(alfabetikSolUst_kare): Bu ifade, alfabetikSolUst_kare matrisindeki her bir satırı birlikte indeksleriyle birlikte döndürür.
        # Yani, her döngü adımında i indeksi satırın indeksi olarak, row ise satırın kendisi olarak atanır
        # (i for i, row in enumerate(alfabetikSolUst_kare) if ilk_harf in row): bu ifade Eğer ilk_harf bir satırda bulunuyorsa, bu satırın indeksi i olarak atanır. Eğer ilk_harf hiçbir satırda bulunmuyorsa, bu ifade None değeri döndürür.
        # next ....  Bu ifade, yukarıdaki adımda bulunan satır indeksini döndürür. Eğer ilk_harf matriste bulunamazsa, None değeri döndürülür.

        col_index = next((i for i, char in enumerate(alfabetikSagAlt_kare[row_index]) if char == ilk_harf), None)
        # Her döngü adımında i indeksi karakterin indeksi olarak, char ise karakteri temsil eder.
        # Bu ifade, belirli bir satırdaki karakterleri kontrol eder ve ilk_harf'in hangi sütunda bulunduğunu belirler. Eğer ilk_harf bir sütunda bulunuyorsa, bu sütunun indeksi i olarak atanır.

        # İkinci karakterin konumunu bul
        row_index_2 = next((i for i, row in enumerate(alfabetikSagAlt_kare) if ikinci_harf in row), None)
        col_index_2 = next((i for i, char in enumerate(alfabetikSolUst_kare[row_index_2]) if char == ikinci_harf), None)

        # İlk şifrelenmiş karakteri bul
        sifreli_harf_1 = karisikSagUst_kare[row_index][col_index_2]

        # İkinci şifrelenmiş karakteri bul
        sifreli_harf_2 = karisikSolAlt_kare[row_index_2][col_index]

        # Şifrelenmiş metne ekle
        sifrelenmis_metin += sifreli_harf_1 + sifreli_harf_2

    return sifrelenmis_metin

def dortKareDesifrele(sifrelenmis_metin):
    metin = ''
    for i in range(0, len(sifrelenmis_metin), 2):
        sifreli_cift = sifrelenmis_metin[i:i + 2]

        # İlk karakterin konumunu bul
        row_index = None
        for i, row in enumerate(karisikSagUst_kare):
            if sifreli_cift[0] in row:
                row_index = i
                break
        if row_index is None:
            print(f"Hata: '{sifreli_cift[0]}' karakteri 'karisikSagUst_kare' matrisinde bulunamadı.")
            return None

        col_index = None
        for i, char in enumerate(karisikSagUst_kare[row_index]):
            if char == sifreli_cift[0]:
                col_index = i
                break

        # İkinci karakterin konumunu bul
        row_index_2 = None
        for i, row in enumerate(karisikSolAlt_kare):
            if sifreli_cift[1] in row:
                row_index_2 = i
                break
        if row_index_2 is None:
            print(f"Hata: '{sifreli_cift[1]}' karakteri 'karisikSolAlt_kare' matrisinde bulunamadı.")
            return None

        col_index_2 = None
        for i, char in enumerate(karisikSolAlt_kare[row_index_2]):
            if char == sifreli_cift[1]:
                col_index_2 = i
                break

        # Orijinal karakterleri bul
        orijinal_harf_1 = alfabetikSolUst_kare[row_index][col_index_2]
        orijinal_harf_2 = alfabetikSagAlt_kare[row_index_2][col_index]

        # Metne ekle
        metin += orijinal_harf_1 + orijinal_harf_2

    return metin.rstrip('b')