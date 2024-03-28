def zigzag_cipher(message, num_rows):
    turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    message = ''.join(char for char in message.lower() if char in turkish_alphabet)

    # Boş bir matris oluştur
    matrix = [['' for _ in range(len(message))] for _ in range(num_rows)]
    #matrix adlı bu iki boyutlu liste
    #Her bir satır, len(message) uzunluğunda ve boş karakter dizileriyle ('') dolu olacaktır.
    #for _ in range(num_rows)] kısmı: Bu, dıştaki listenin satır sayısını temsil eder. _ yerine herhangi bir değişken adı kullanılabilir, ancak bu değişken kullanılmayacağı için yaygın olarak _ kullanılır. Bu döngü, belirtilen num_rows sayısında bir dizi oluşturur, her biri len(message) uzunluğunda boş karakter dizileri içerir.

    # Zigzag şeklinde matrise yerleştir
    row, direction = 0, 1
    for i in range(len(message)):#: Bu döngü, mesajdaki her karakter için işlem yapar. Yani, her bir karakteri Zigzag şeklindeki matrise yerleştirecek ve ona uygun bir yön belirleyecektir.
        matrix[row][i] = message[i]
        if row == num_rows - 1: #Bu satır, eğer işlem son satıra (num_rows - 1) ulaşırsa, yönü değiştirmek için bir kontrol sağlar.
            direction = -1
        elif row == 0: #Bu satır, eğer işlem ilk satıra (0'ıncı satır) ulaşırsa, yönü değiştirmek için bir kontrol sağlar.
            direction = 1
        row += direction
        #Eğer direction değeri 1 ise, row değişkeni arttırılır. Bu, satırın aşağı doğru hareket etmesini sağlar.
        #Eğer direction değeri -1 ise, row değişkeni azaltılır. Bu, satırın yukarı doğru hareket etmesini sağlar.

    # Şifreli metni oluştur
    ciphertext = ''
    for row in matrix:
        ciphertext += ''.join(row)

    return ciphertext

def zigzag_decipher(ciphertext, num_rows):
    # Boş bir matris oluştur
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(num_rows)]

    # Zigzag şeklinde matrise yerleştir
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        matrix[row][i] = '*'  # Şifrelenmiş metindeki karakterlerin yerini belirlemek için '*' kullanılır
        if row == num_rows - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction

    # Matrisi dolaşarak şifreli metni yerine koy
    plaintext = ''
    index = 0
    for r in range(num_rows):
        for c in range(len(ciphertext)):
            if matrix[r][c] == '*' and index < len(ciphertext):
                matrix[r][c] = ciphertext[index]
                index += 1

    # Deşifrelenmiş metni oluştur
    for i in range(len(ciphertext)):
        for r in range(num_rows):
            if matrix[r][i] != '':
                plaintext += matrix[r][i]

    return plaintext

