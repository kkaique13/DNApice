from coracao import Coracao
from pulmao import Pulmao
from organismo import Organismo
from bioma import Bioma

if __name__ == "__main__":
    ambiente = Bioma("Caatinga", 27.7)
    ambiente.mostrarStatus()

    avatar = Organismo("Kaíque", ambiente)
    avatar.mostrarStatus()

    avatar.correr()
    avatar.ficarNoSol()
    avatar.ficarNoSol()
    avatar.ficarNoSol()
    avatar.ficarNoSol()
    avatar.ficarNoSol()
    avatar.mostrarStatus()

    avatar.beberAgua()
    avatar.mostrarStatus()