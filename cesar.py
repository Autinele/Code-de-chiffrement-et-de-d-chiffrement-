def chiffrement_cesar(message, ecart):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            decalage = ord('a') if lettre.islower() else ord('A')
            resultat += chr((ord(lettre) - decalage + ecart) % 26 + decalage)
        else:
            resultat += lettre
    return resultat

def dechiffrement_cesar(message, ecart):
    return chiffrement_cesar(message, -ecart)

# Demander à l'utilisateur l'écart pour le chiffrement de César
ecart_chiffrement = int(input("Entrez l'écart pour le chiffrement de César : "))

# Demander à l'utilisateur le message à chiffrer
message_a_chiffrer = input("Entrez le message à chiffrer : ")

# Chiffrer le message
message_chiffre = chiffrement_cesar(message_a_chiffrer, ecart_chiffrement)
print("Message chiffré :", message_chiffre)

# Demander à l'utilisateur le message à déchiffrer
message_a_dechiffrer = input("Entrez le message à déchiffrer : ")

# Déchiffrer le message
message_dechiffre = dechiffrement_cesar(message_a_dechiffrer, ecart_chiffrement)
print("Message déchiffré :", message_dechiffre)
