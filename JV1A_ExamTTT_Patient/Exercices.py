# "1/ Écrire la fonction permettant d’afficher la grille de jeu"

# Lorsque i = 0, 
# j = 1 soit tableau[0]
# j = 3 soit tableau [1]
# j = 5 soit tableau [2]
# Lorsque i = 1,
# j = 1 soit tableau [3] ...


# tableau = [0,0,0,0,0,0,0,0,0]
# taille_tableau = len(tableau)
# k = 0

# for i in range (5):
#     for j in range (5):
#         if (i % 2) != 0 :
#             print ("-", end = " ")
#         else :
#             if (i % 2) == (j % 2) :
#                 print (tableau[k], end = " ")
#                 k += 1
#             else :
#                 print ("|", end = " ")
#     print (" ")
       

# "2/ Écrire la fonction permettant de jouer un O ou un X."

# "Premiere tentative"

# def croix_rond (tabe, index_1, index_2, index_choix_1, index_choix_2):
#     if index_1 == 1 :
#         tabe.pop(index_2)
#         tabe.insert (index_2, index_choix_1)
#     if index_1 == 2 :
#         tabe.pop(index_2)
#         tabe.insert (index_2, index_choix_2)
#     print (tabe)
#     return tabe, index_1, index_2, index_choix_1, index_choix_2

# tableau = [0,0,0,0,0]
# taille_tableau = len(tableau)
# croix = "X"
# rond = "O"

# symbole = int(input("Quel symbole voulez-vous jouer ? (1 pour X, 2 pour O) \n"))
# place_symbole = int(input("A quelle place ? (0 à 8, de gauche à droite avec 0 = place n°1) \n"))

# tableau, symbole, place_symbole, croix, rond = croix_rond (tableau, symbole, place_symbole, croix, rond)

# "Deuxième tentative"

tableau = [0,0,0,0,0,0,0,0,0]
taille_tableau = len(tableau)
k = 0
croix = "X"
rond = "O"

symbole = int(input("Quel symbole voulez-vous jouer ? (1 pour X, 2 pour O) \n"))
place_symbole = int(input("A quelle place ? (0 à 8, de gauche à droite avec 0 = place n°1) \n"))

for i in range (5):
    for j in range (5):
        if (i % 2) != 0 :
            print ("-", end = " ")
        else :
            if (i % 2) == (j % 2) :
                print (tableau[k], end = " ")
                k += 1
                if symbole == 1 :
                    tableau.pop(place_symbole)
                    tableau.insert (place_symbole, croix)
                if symbole == 2 :
                    tableau.pop(place_symbole)
                    tableau.insert (place_symbole, rond)
            else :
                print ("|", end = " ")
    print (" ")