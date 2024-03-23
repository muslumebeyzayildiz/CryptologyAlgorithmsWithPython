import math
def route_encrypt(plain_text="", step_size=5):
    """
        Takes plain text as input and produces encrypted text as output
        Implements the route cipher technique
    """

    idx = 0
    matrix_representation = [] #adlı bir liste oluşturulur. Bu liste, metnin matris temsiliyetini içerecek şekilde düzenlenir
    encrypted_text = ""

    # width = step_size ile düz metinden bir matris oluşturun
    for i in range(math.ceil(len(plain_text) / step_size)):
        matrix_row = []
        for j in range(step_size):
            if i * step_size + j < len(plain_text):
                matrix_row.append(plain_text[i * step_size + j])
            else:
                matrix_row.append("-")
        matrix_representation.append(matrix_row)

    matrix_width = len(matrix_representation[0])
    matrix_height = len(matrix_representation)
    allowed_depth = 0
    #Bu, spiralin ne kadar derinleşeceğini belirler.
    if matrix_width < matrix_height:
        allowed_depth = matrix_width // 2
    else:
        allowed_depth = matrix_height // 2

    # Here "i" denotes the depth we're into the matrix
    # Here we read the normal matrix in a spiral form starting from top right corner
    for i in range(allowed_depth):

        # Going up on the bottom side (starting from bottom left corner)
        # Sol alt köşeden başlayarak yukarı doğru
        for j in range(matrix_height - i - 1, i - 1, -1):
            encrypted_text += matrix_representation[j][i]

        # Going right
        # Yukarıdan başlayarak sağa doğru
        for j in range(i + 1, matrix_width - i):
            encrypted_text += matrix_representation[i][j]

        # Going down to bottom
        # Sağdan başlayarak aşağı doğru
        for j in range(i + 1, matrix_height - i):
            encrypted_text += matrix_representation[j][matrix_width - i - 1]

        # Going up
        # Soldan başlayarak yukarı doğru
        for j in range(matrix_width - i - 2, i, -1):
            encrypted_text += matrix_representation[matrix_height - i - 1][j]

    return encrypted_text