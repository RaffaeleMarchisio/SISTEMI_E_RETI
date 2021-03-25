import pygame
import sys
import csv

dizionario = {'a': [0, 0, 0, 0, 0], 'b': [0, 0, 0, 0, 1], 'c': [0, 0, 0, 1, 0], 'd': [0, 0, 0, 1, 1],
              'e': [0, 0, 1, 0, 0], 'f': [0, 0, 1, 0, 1], 'g': [0, 0, 1, 1, 0], 'h': [0, 0, 1, 1, 1],
              'i': [0, 1, 0, 0, 0],
              'l': [0, 1, 0, 0, 1], 'm': [0, 1, 0, 1, 1], 'n': [0, 1, 1, 0, 0], 'o': [0, 1, 1, 0, 1],
              'p': [0, 1, 1, 1, 0], 'q': [0, 1, 1, 1, 1], 'r': [1, 0, 0, 0, 0], 's': [1, 0, 0, 0, 1],
              't': [1, 0, 0, 1, 0],
              'u': [1, 0, 0, 1, 1], 'v': [1, 0, 1, 0, 0], ' ': [1, 0, 1, 0, 1], '0': [1, 0, 1, 1, 0],
              '1': [1, 0, 1, 1, 1], '2': [1, 1, 0, 0, 0], '3': [1, 1, 0, 0, 1], '4': [1, 1, 0, 1, 0],
              '5': [1, 1, 0, 1, 1], '6': [1, 1, 1, 0, 0], '7': [1, 1, 1, 0, 1], '8': [1, 1, 1, 1, 0],
              '9': [1, 1, 1, 1, 1]}

SIZE=(600,600)
NERO=(0,0,0)
BIANCO=(255,255,255)
#def draw_qrcode(lista):
    #dimensione=50
    #ciclo per ciascun elemento della lista di liste e disegno la griglia(non ancora funzionate cicla per sempre)
    #for elemento in lista:
     #   for bit in elemento:
      #      for x in range(0,SIZE[0],dimensione):
      #          for y in range(0,SIZE[1],dimensione):
      #              if bit==1:
      #                  pieno=pygame.Rect(x,y,dimensione,dimensione)
      #                  pygame.draw.rect(screen,NERO,pieno,1)
      #              elif bit==0:
      #                  vuoto=pygame.Rect(x,y,dimensione,dimensione)
      #                  pygame.draw.rect(screen,BIANCO,vuoto,1)


def main():
    lista = []
    str = 0
    lung = 0
    #global screen
    #pygame.init()
    #screen=pygame.display.set_mode(SIZE)
    #ciclo per determinare se la stringa ha il numero di caratteri consentiti
    while lung > 12 or lung == 0:
        str = input("inserire la stringa da modificare:")
        lung = len(str)

        if lung > 12 or lung == 0:
            print("la stringa deve essere massimo 12 caratteri")
    cont = 0
    for carattere in str:                         #ciclo per ogni carattere
        for chiave, valore in dizionario.items():
            if  carattere == chiave:
                lista.append(valore)

    csvreader=open("code.csv","w") #apro il file in modalita scrittura
    csvwriter=csv.writer(csvreader)

    for elemento in lista:          #ciclo per ogni elemento della lista di liste creata in precedenza
        csvwriter.writerow(elemento)

    csvreader.close()
'''
    while True:
        draw_qrcode(lista)
        for event in pygame.event.get(): #ciclo for gestione eventi
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
'''

if __name__ == '__main__':
    main()
