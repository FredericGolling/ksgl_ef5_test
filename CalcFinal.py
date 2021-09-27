Zahl = int(input())

#----------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------
HexList = ['0','0','0','0']
HexArchive = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


def HexDez(initial):
    counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    while initial > 0:
        while initial >= 16:
            while initial >= 256:
                while initial >= 4096:
                    HexList[0] = HexArchive[0 + counter]
                    counter += 1
                    initial -= 4096
                else:
                    HexList[1] = HexArchive[0 + counter1]
                    counter1 += 1
                    initial -= 256
            else:
                 HexList[2] = HexArchive[0 + counter2]
                 counter2 += 1
                 initial -= 16
        else:
             if initial > 0:
                 HexList[3] = HexArchive[0 + counter3]
                 counter3 += 1
                 initial -= 1

    else:

        print(*HexList)
        return HexList

HexDez(Zahl)
Binary(Zahl)