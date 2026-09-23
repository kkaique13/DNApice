from organismo import Organismo
import os
def Game(organismo:Organismo):
    os.system('cls')
    while True:
        organismo.mostrarStatus()

        print("1- Fazer o organismo correr")
        print("2- Beber água do cantil")
        print("3- Ficar no sol") #Como benefício, vai diminuir a taxa de desidratação do organismo por ele estar se acostumando com o sol, mas ele ainda vai desidratar mais de imediato
        print("4- Mostrar status")
        print("5- Desistir")
        es = int(input("\nEscolha uma das opções: \n"))