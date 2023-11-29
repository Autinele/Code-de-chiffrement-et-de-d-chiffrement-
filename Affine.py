def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def trouver_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def est_premier_entre_eux(a, b):
    return pgcd(a, b) == 1

def chiffrement_affine(texte, a, b, m):
    texte_chiffre = ""
    for char in texte:
        if char.isalpha():
            x = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            y = (a * x + b) % m
            texte_chiffre += chr(y + ord('A')) if char.isupper() else chr(y + ord('a'))
        else:
            texte_chiffre += char
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b, m):
    a_inv = trouver_inverse(a, m)
    texte_dechiffre = ""
    for char in texte_chiffre:
        if char.isalpha():
            y = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            x = (a_inv * (y - b)) % m
            texte_dechiffre += chr(x + ord('A')) if char.isupper() else chr(x + ord('a'))
        else:
            texte_dechiffre += char
    return texte_dechiffre

# Demander à l'utilisateur d'entrer la clé
a = int(input("Entrez la valeur de a pour le chiffrement affine : "))
m = 26  # Taille de l'alphabet anglais

# Vérifier si a et m sont premiers entre eux
while not est_premier_entre_eux(a, m):
    print("a et 26 ne sont pas premiers entre eux. Choisissez une autre valeur pour a.")
    a = int(input("Entrez une nouvelle valeur pour a : "))

# Calculer automatiquement b en utilisant la valeur de a donnée
b = (a + 1) % m

# Demander le message à chiffrer
message_clair = input("Entrez le message à chiffrer : ")

# Chiffrer le message
message_chiffre = chiffrement_affine(message_clair, a, b, m)
print("Message chiffré :", message_chiffre)

# Déchiffrer le message
message_dechiffre = dechiffrement_affine(message_chiffre, a, b, m)
print("Message déchiffré :", message_dechiffre)
