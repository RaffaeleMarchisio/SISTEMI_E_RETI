ALFABETO1 = {"A":"P", "B":"Q","C":"R", "D":"S", "E":"T","F":"U", "G":"V", "H":"W", "I":"X","J":"Y", "K":"Z", "L":"A", "M":"B",
            "N":"C", "O":"D", "P":"E", "Q":"F", "R":"G", "S":"H", "T":"I", "U":"J", "V":"K", "W":"L", "X":"M", "Y":"N",
            "Z":"O",
            "a": "p", "b": "q", "c": "r", "d": "s", "e": "t", "f": "u", "g": "v", "h": "w", "i": "x", "j": "y",
            "k": "z", "l": "a", "m": "b","n": "c", "o": "d", "p": "e", "q": "f", "r": "g", "s": "h", "t": "i", "u": "j", "v": "k", "w": "l",
            "x": "m", "y": "n",
            "z": "o"}
ALFABETO2 = {"P":"A", "Q":"B","R":"C", "S":"D", "T":"E","U":"F", "V":"G", "W":"H", "X":"I","Y":"J", "Z":"K", "A":"L", "B":"M",
            "C":"N", "D":"O", "E":"P", "F":"Q", "G":"R", "H":"S", "I":"T", "J":"U", "K":"V", "L":"W", "M":"X", "N":"Y",
            "O":"Z",
            "p": "a", "q": "b", "r": "c", "s": "d", "t": "e", "u": "f", "v": "g", "w": "h", "x": "i", "y": "j",
            "z": "k", "a": "l", "b": "m","c": "n", "d": "o", "e": "p", "f": "q", "g": "r", "h": "s", "i": "t", "j": "u", "k": "v", "l": "w",
            "m": "x", "n": "y",
            "o": "z"}

risp = 1
str = ""
while risp == 1 or risp == 2:
    risp = int(input("1-codificare\n2-decodificare\n3-esci\nscegliere:"))
    if risp == 1:
        str = input("stringa da codificare:")
        cont = 0
        while cont < len(str):
            str=str.replace(str[cont],ALFABETO1[str[cont]])
            cont = cont + 1
        print(str)
    elif risp==2:
        str = input("stringa da codificare:")
        cont = 0
        while cont < len(str):
            str = str.replace(str[cont], ALFABETO2[str[cont]])
            cont = cont + 1
        print(str)

