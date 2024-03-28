import math
def route_encrypt(plain_text="", step_size=None):
    idx = 0
    matrix_representation = [] # metnin, satır ve sütunlarını içeren bir matrisin temsilidir.
    #metnin düzgün bir şekilde satırlara ve sütunlara bölünmüş bir temsilidir
    encrypted_text = ""

    turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    # Metindeki sadece Türkçe alfabedeki küçük harfleri al
    plain_text = ''.join(char for char in plain_text.lower() if char in turkish_alphabet)

    # step_size belirtilmemişse, varsayılan değeri 5 olarak ayarla
    if step_size is None:
        step_size = 5

    # width = step_size ile düz metinden bir matris oluşturun
    for i in range(math.ceil(len(plain_text) / step_size)):
        matrix_row = []
        for j in range(step_size):
            if idx < len(plain_text):
                matrix_row.append(plain_text[idx])
                idx += 1
            else:
                matrix_row.append("b")
        matrix_representation.append(matrix_row)

    matrix_width = len(matrix_representation[0])
    matrix_height = len(matrix_representation)
    allowed_depth = 0
    #Bu, spiralin ne kadar derinleşeceğini belirler.
    if matrix_width < matrix_height:
        allowed_depth = matrix_width // 2
    else:
        allowed_depth = matrix_height // 2

    # Burada "i" matrisin derinliğini ifade ediyor
    # Burada normal matrisi üstten başlayarak spiral şeklinde okuyoruz.
    # Rota şifreleme tekniğini uygularight corner
    for i in range(allowed_depth):

        # Alt taraftan yukarı çıkıyoruz (sol alt köşeden başlayarak)
        for j in range(matrix_height - i - 1, i - 1, -1):
            encrypted_text += matrix_representation[j][i]
#matrix_height - i - 1 ifadesi, başlangıç indeksini belirler. Bu ifade, her adımda bir satır yukarı çıktığımız için başlangıç indeksi
#Bitiş değeri i - 1 olarak belirleni

        # Yukarıdan başlayarak sağa doğru
        for j in range(i + 1, matrix_width - i):
            encrypted_text += matrix_representation[i][j]
#i değeri, şu anda işlenen adımın derinliğini ifade eder. + 1 eklenmesi, her seferinde sütunun bir sonraki sütundan başlamasını sağlar.

        # Sağdan başlayarak aşağı doğru
        for j in range(i + 1, matrix_height - i):
            encrypted_text += matrix_representation[j][matrix_width - i - 1]

# matrix_height, matrisin toplam satır sayısını ifade eder. i, şu anda işlenen adımın derinliğini ifade eder.


        # alt kenarından başlayarak sola doğru dolaşmayı sağlar.
        for j in range(matrix_width - i - 2, i, -1):
            encrypted_text += matrix_representation[matrix_height - i - 1][j]
# matrix_width, matrisin toplam sütun sayısını ifade eder. i, şu anda işlenen adımın derinliğini ifade eder. - 2 eklenmesi, sağ kenardaki iki sütunu atlamamızı sağlar, çünkü bu sütunlar zaten önceki adımlarda işlenmiştir.
# Bitiş değeri i olarak belirlenir. Bu, döngünün her bir adımında, mevcut adımın sütununa kadar gitmesini sağlar.

    return encrypted_text