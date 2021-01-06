import random

dizionarioESA = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
                 12: "C", 13: "D", 14: "E", 15: "F"}


def generaMAC():
    cont = 0
    while cont < 17:
        if cont != 2 and cont != 5 and cont != 8 and cont != 11 and cont != 14:
            n = random.randint(0, 15)
            print(dizionarioESA[n], end="")
        elif cont == 2 or cont == 5 or cont == 8 or cont == 11 or cont == 14:
            print(":", end="")
        cont = cont + 1


generaMAC()