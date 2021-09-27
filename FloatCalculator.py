BinaryList = []


def Binary(number):
    while number != 0:
        if number % 2 == 0:
            BinaryList.insert(0, '0')

        else:
            BinaryList.insert(0, '1')

        number = number // 2
    print(*BinaryList)
    return BinaryList

def VorKommaConv(Zahl):
    VorKomma = Zahl // 1
    return VorKomma

def NachKommaConv(number):

    # minus 10 bis kleiner als 10
    # minus 5 bis kleiner als 5 etc.


def floatconverter(number):
    VorKomma = VorKommaConv(number)
    BinVorKomma = Binary(int(VorKomma))
    NachKomma =

floatconverter(float(12.5))
