def vigenere_sifrele(metin, anahtar):
    # Türkçe alfabeyi tanımla
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

    # Metni ve anahtarı Türkçe alfabeye uyumlu hale getir
    metin = metin.lower()
    anahtar = anahtar.lower()

    # Anahtarı metnin uzunluğuna genişlet
    # Anahtar metnin uzunluğuna ulaşana kadar çoğaltılır. Eğer anahtar, metinden daha uzunsa, fazla kısmı kesilir. Bu işlem, metnin her bir karakterine karşılık gelen bir anahtar oluşturur.
    genisletilmis_anahtar = anahtar * (len(metin) // len(anahtar)) + anahtar[:len(metin) % len(anahtar)]

    # Şifreleme işlemi
    sifreli_metin = ''
    #zip() fonksiyonu, metin ve genişletilmiş anahtar arasında aynı konumda bulunan karakterleri çiftler halinde birleştirir.
    # Yani her bir adımda, metinden bir karakter (m) ve anahtardan bir karakter (a) alınır.
    for m, a in zip(metin, genisletilmis_anahtar):
        #Karakterin alfabede olup olmadığını kontrol eder. Eğer karakter alfabede yer alıyorsa, şifreleme işlemi uygulanır.
        if m in alfabe:
            m_index = alfabe.index(m) #Şifrelenen metindeki karakterin alfabe içindeki dizinini bulur.
            a_index = alfabe.index(a) #Anahtar metindeki karakterin alfabe içindeki dizinini bulur.
            sifreli_index = (m_index + a_index) % len(alfabe)
            sifreli_metin += alfabe[sifreli_index]
        else:
            # Eğer karakter alfabede yoksa olduğu gibi bırak
            sifreli_metin += m

    return sifreli_metin

def vigenere_desifrele(sifreli_metin, anahtar):
    # Türkçe alfabeyi tanımla
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

    # Şifreli metni ve anahtarı Türkçe alfabeye uyumlu hale getir
    sifreli_metin = sifreli_metin.lower()
    anahtar = anahtar.lower()

    # Anahtarı şifreli metnin uzunluğuna genişlet
    genisletilmis_anahtar = anahtar * (len(sifreli_metin) // len(anahtar)) + anahtar[:len(sifreli_metin) % len(anahtar)]

    # Deşifreleme işlemi
    orijinal_metin = ''
    for s, a in zip(sifreli_metin, genisletilmis_anahtar):
        if s in alfabe:
            s_index = alfabe.index(s)
            a_index = alfabe.index(a)
            orijinal_index = (s_index - a_index) % len(alfabe)
            orijinal_metin += alfabe[orijinal_index]
        else:
            # Eğer karakter alfabede yoksa olduğu gibi bırak
            orijinal_metin += s

    return orijinal_metin

