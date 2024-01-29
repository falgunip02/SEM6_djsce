def generate_playfair_matrix(key):
    # Create a 5x5 matrix for the Playfair cipher
    matrix = [['' for _ in range(5)] for _ in range(5)]
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    
    # Fill in the matrix with the key
    key_pos = set()
    row, col = 0, 0
    for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in key_pos:
            matrix[row][col] = char
            key_pos.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1
    
    return matrix

def find_position(matrix, char):
    # Find the position of a character in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    ciphertext = ''
    
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        if len(pair) == 1:  # Handle odd-length plaintext by adding a dummy character
            pair += 'X'
        
        # Find positions of characters in the matrix
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        # Encrypt the pair
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Get user input for the key and plaintext
key = input("Enter the key for Playfair cipher: ")
plaintext = input("Enter the plaintext to encrypt: ")

# Encrypt the plaintext using Playfair cipher
ciphertext = playfair_encrypt(plaintext, key)

# Display the result
print("Ciphertext:", ciphertext)
