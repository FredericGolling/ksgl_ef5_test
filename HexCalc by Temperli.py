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


