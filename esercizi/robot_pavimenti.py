# ROBOT E PAVIMENTI
# memorizzare un programma pavimento e ostacoli
#
#
# Nx e Ny dizionario
import turtle
import pygame
import sys

pavimento = [[1, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 1],
             [1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 0, 0],
             [1, 0, 0, 1, 0, 1]]
OSTACOLO=-1
CELLE_ADIACENTI=[[-1,0],[0,1],[1,0],[0,-1]]
N_RIGHE=len(pavimento)
N_COLONNE=len(pavimento[0])

def controlla_celle_adiacenti(p,x,y):
    #scorrere su celle adiacenti
    #verifica se 
    pass

DIMENSIONI=(600,600)
NERO=(0,0,0)
BIANCO=(255,255,255)
def draw_grid():
    dimensionex=DIMENSIONI[0]//N_COLONNE
    dimensioney=DIMENSIONI[0]//N_RIGHE

    conty=0

    for y in range(0,DIMENSIONI[0],dimensioney):
        riga=pavimento[conty]

        if conty <N_RIGHE-1:
            conty+=1

        contx=0
        for x in range(0,DIMENSIONI[0],dimensionex):
            colonna=riga[contx]

            if contx < N_COLONNE-1:
                contx+=1
            if colonna == 0:
                piastrell= pygame.Rect(x,y,dimensionex,dimensioney)
                pygame.draw.rect(finestra,BIANCO,piastrell,1)
            else:
                ostacolo= pygame.Rect(x,y,dimensionex,dimensioney)
                pygame.draw.rect(finestra, BIANCO, ostacolo)


def main():
    pygame.init()
    pavimento_numerato = []
    piastrelle_numerate = []



    dizionario = {}
    cont = -1
    for riga in pavimento:
        piastrelle_numerate = []
        for piastrelle in riga:
            if piastrelle == 0:
                cont += 1
                piastrelle_numerate.append(cont)
            elif piastrelle == 1:
                piastrelle_numerate.append(OSTACOLO)
        pavimento_numerato.append(piastrelle_numerate)

    print(f"{pavimento}\n{pavimento_numerato}")

    for elemento in pavimento_numerato:
        for piastrelle in elemento:
            pass

    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIMENSIONI)
    finestra.fill(NERO)
    while True:
        draw_grid()
        for event in pygame.event.get():  # ciclo for gestione eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
