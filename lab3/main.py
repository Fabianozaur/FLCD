from Scanner import Scanner,operators,separators,reserved
from SymbolTable import SymbolTable
from ProgramInternalForm import ProgramInternalForm


def readTokens():
    with open('Token.txt','r') as f:
        for i in range(5):
            separator=f.readline().strip()
            if separator=="<space>":
                separator=" "
            separators.append(separator)
        for i in range(12):
            operators.append(f.readline().strip())
        for i in range(15):
            reserved.append(f.readline().strip())

def main():
    readTokens()
    fileName = "p1err.txt"
    st = SymbolTable(16)
    pif = ProgramInternalForm()
    scanner = Scanner()
    exceptionMessage = ""

    with open(fileName, 'r') as file:
        lineCounter = 0
        for line in file:
            lineCounter += 1
            for token in scanner.tokenizeFunction(line.strip()):
                if token in reserved + separators + operators:
                    if token == ' ':
                        continue
                    pif.addToken(token, (0, 0))
                elif scanner.checkIfIdentifier(token) or scanner.checkIfConstant(token):
                    if not st.contains(token):
                        st.add(token)
                        id=st.getPosition(token)
                        pif.addToken(token, id)
                else:
                    exceptionMessage += 'Lexical error at token ' + token + ' at line ' + str(lineCounter) + "\n"

    with open('st.out', 'w') as writer:
        writer.write(str(st))

    with open('pif.out', 'w') as writer:
        writer.write(str(pif))

    if exceptionMessage == '':
        print("No lexical errors")
    else:
        print(exceptionMessage)
main()
