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


Binary(9999)
