from collections import deque


class HashTable:

    def __init__(self, size):
        self.items = [[] for _ in range(size)]
        self.__size = size

    #ascii
    def hashFunction(self, value):
        sum = 0
        for chr in value:
            sum += ord(chr)
        return sum % self.__size

    def add(self, value):
        self.items[self.hashFunction(value)].append(value)

    def contains(self, value):
        return value in self.items[self.hashFunction(value)]

    def __str__(self) -> str:
        finalString = ""
        for i in range(self.__size):
            finalString = finalString + str(i) + ": " + str(self.items[i]) + "\n"
        return finalString

    def getPosition(self, value):
        listPosition = self.hashFunction(value)
        listIndex = 0
        for item in self.items[listPosition]:
            if item != value:
                listIndex += 1
            else:
                break
        return (listPosition, listIndex)


class SymbolTable:

    def __init__(self, size) -> None:
        self.hashT = HashTable(size)

    def __str__(self) -> str:
        return str(self.hashT)

    def add(self, value):
        self.hashT.add(value)

    def contains(self, value):
        return self.hashT.contains(value)


    def getPosition(self, value):
        return self.hashT.getPosition(value)





