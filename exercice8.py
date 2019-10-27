from random import *
nombre_aleatoire=randint(0,100)
print("nombre_aleatoire=",nombre_aleatoire)
nombre_utilisateur=input("choisir un nombre entre 0 et 100:")
nombre_utilisateur=int(nombre_utilisateur)
while(nombre_utilisateur != nombre_aleatoire):
    if(nombre_utilisateur < nombre_aleatoire):
        print("votre nombre est plus petit")
    elif(nombre_utilisateur > nombre_aleatoire):
        print("votre nombre est plus grand")
    nombre_utilisateur=input("choisir un nombre entre 0 et 100:")
    nombre_utilisateur=int(nombre_utilisateur)
if(nombre_utilisateur == nombre_aleatoire):
    print("vous avez trouvé")
