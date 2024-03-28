def permutation_cipher(msg: str, key: int, decrypt: bool=False) -> str:
    key = str(key)
    key_len = len(key)
    result = ''
    turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

    # Msg'deki Türk alfabesi harflerini filtrele, özel karakterleri ve sayıları kaldır
    filtered_msg = ''.join(char for char in msg.lower() if char in turkish_alphabet)
    print('küçük harflerden oluşan metin',filtered_msg)

    # Msg'yi gerekliyse b ekleyerek bir tam sayı katına tamamla
    if len(filtered_msg) % key_len != 0:
        filtered_msg += 'b' * (key_len - (len(filtered_msg) % key_len))

    # Blok sayısını hesapla
    num_blocks = len(filtered_msg) // key_len

    # Her bloğu işle
    for num_block in range(num_blocks):
        # Geçerli bloğu al
        # Her parçayı, anahtar kullanarak karakterlerin yerlerini değiştirerek yeni bir blok oluştur.
        start_idx = num_block * key_len
        block = [x for x in filtered_msg[start_idx:(start_idx + key_len)]]
        #Bu kısım, verilen mesajı parçalara böler. start_idx değişkeni, mevcut bloğun başlangıç indeksini hesaplar.
        # Her bir blok, start_idx ile başlayıp (start_idx + key_len) ile biten bir dilim ile alınır.

        #msg[start_idx:(start_idx + key_len)] ifadesi, mesajdaki bu bloğu seçer ve bu bloğun karakterlerini tek tek bir listeye ekler.

        # Bu bloktaki karakterleri yeni bir blok halinde yeniden düzenleme
        new_block = [' '] * key_len #new_block adında bir boşluklarla dolu bir liste oluşturulur.
        for idx1, idx2 in enumerate(key): #enumerate(key) ifadesi, anahtar üzerinde indekslerle birlikte döngü kurar.
            # Bu, anahtarın her karakterini ve indeksini almak için kullanılır.
            idx2 = int(idx2) - 1
            #Python'daki liste indeksleme 0'dan başlar. Ancak anahtar olarak verilen stringin karakterleri genellikle 1'den başlayarak numaralandırılır (örneğin, "1234" gibi).
            #Bu nedenle, anahtarın her karakteri bir sayı olarak ele alınır ve 1 eksiltildikten sonra kullanılır. Böylece, 1 numaralı karakter 0 indeksli elemana,
            if decrypt:
                new_block[idx2] = block[idx1]
            else:
                new_block[idx1] = block[idx2]
            #Eğer decrypt değeri True ise, new_block'un indeksini anahtarın karakteri olan idx2 olarak kullanarak, şifrelenmiş metindeki karakterlerin orijinal konumlarına yerleştirir.
            #Eğer decrypt değeri False ise, new_block'un indeksini anahtarın indeksi olan idx1 olarak kullanarak, orijinal metindeki karakterlerin şifreli konumlarına yerleştirir.

        # Sonuç mesajına yeni bloğu ekleyin
        result += ''.join(new_block)

    return result


