Dans ce code on essaye de chiffrer et de déchiffrer des messages en utilisant la méthode de chiffrement affine.
D'abord la fonction pgcd(a,b) calcule le pgcd entre deux nombres a et b. La fonction trouver_inverse(a,m) cherche
l'inverse de a modulo m. La fonction est_premier_entre_eux(a,b) vérifie si a et b sont premiers entre eux en utilisant
la fonction pgcd. Les fonctions chiffrement_affine et déchiffrement_affine font respectivement le cryptage et le décryptage
des messages en utilisant respectivement les fonctions affine. L'utilisateur donne une valeur pour le a et on vérifie que
cette valeur et 26(le nombre de lettres de l'alphabet) sont premiers entre eux. Si non on lui demande de mettre une autre valeur
et on détermine la valeur de b pour pouvoir mieux utiliser les fonctions pour le chiffrement et le déchiffrement.
