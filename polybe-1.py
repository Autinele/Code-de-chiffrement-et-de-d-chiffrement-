def create_polybe_table(starting_letter: str) -> dict:
    starting_letter = starting_letter.upper()
    alphabet = [char for char in starting_letter + 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if char.isalpha()]
    alphabet = list(dict.fromkeys(alphabet))  # Remove duplicates
    alphabet = [char if char != 'J' else 'I' for char in alphabet]

    polybe_table = {(i // 5 + 1, i % 5 + 1): c for i, c in enumerate(alphabet)}
 
    return polybe_table

def create_polybe_table_from_keyword(keyword: str) -> dict:
    keyword = keyword.upper()
    keyword = [char for char in keyword if char.isalpha()]
    keyword += [char for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if char not in keyword]
    keyword = list(dict.fromkeys(keyword))  # Remove duplicates

    polybe_table = {(i // 5 + 1, i % 5 + 1): c for i, c in enumerate(keyword)}

    return polybe_table

def polybe_encrypt(message: str, polybe_table: dict) -> str:
    encrypted_message = ''
    for char in message:
        if char.upper() == 'J':
            char = 'I'
        if char.upper() in polybe_table.values():
            coordinates = [(row, col) for (row, col), value in polybe_table.items() if value == char.upper()][0]
            encrypted_message += f"{coordinates[0]}{coordinates[1]}"
    return encrypted_message 

def polybe_decrypt(encrypted_message: str, polybe_table: dict) -> str:
    decrypted_message = ''

    for i in range(0, len(encrypted_message), 2):
        coords = encrypted_message[i:i+2]
        char = polybe_table[int(coords[0]), int(coords[1])]
        decrypted_message += char

    return decrypted_message

# Obtenir le choix de l'utilisateur
starting_letter = input("Entrez une lettre de départ (ou appuyez sur Entrée pour ne pas choisir) : ")
keyword = input("Entrez un mot-clé (ou appuyez sur Entrée pour ne pas choisir) : ")

if starting_letter:
    custom_polybe_table = create_polybe_table(starting_letter)
elif keyword:
    custom_polybe_table = create_polybe_table_from_keyword(keyword)
else:
    # Utiliser le tableau par défaut
    custom_polybe_table = create_polybe_table('A')

# Message à chiffrer
message_to_encrypt = input("Entrez le message à chiffrer : ") 
encrypted_message = polybe_encrypt(message_to_encrypt, custom_polybe_table)
print("Message chiffré:", encrypted_message)

# Message à déchiffrer
message_to_decrypt = input("Entrez le message à déchiffrer : ") 
decrypted_message = polybe_decrypt(message_to_decrypt, custom_polybe_table)
print("Message déchiffré:", decrypted_message)
