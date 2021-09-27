

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]



def Dezimal(Zahl):
    outcome = 0
    HexArchive = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    integer = str(Zahl)

    for i in range (len(integer)):
        print (integer[i])
        charnum = ord(integer[i])
        if ( charnum > 64) and (charnum < 123):
            # it's a Hexadecimal

            for k in range (4):
                digit = Zahl(k)
                index = HexArchive.index(digit)
                outcome += index * (16 ** i)
            print(outcome)
            return outcome


        else:
            # it's a binary number

            new = reverse(str(Zahl))
            for i in range (len(integer)):
                bö = integer[i]
                if bö != 0:
                    outcome += 2 ** i

            print(outcome)
            return outcome

Dezimal(1100)

werte = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
hexzahl = []
y = int(input("zahl"))
while y > 0:
    rest = y % 16
    y = y // 16
    hexzahl.append(werte[rest])

hexzahl.reverse()
print(hexzahl)
print(''.join(str(x) for x in hexzahl))
