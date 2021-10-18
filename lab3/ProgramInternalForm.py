class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def addToken(self, token, pos):
        self.__content.append((token, pos))

    def __str__(self):
        text = ""
        for pair in self.__content:
            text += 'Token ' + pair[0] + " on Position: " + str(pair[1])  + "\n"
        return text