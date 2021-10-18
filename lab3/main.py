
reserved=[]
operators=[]
separators=[]

def readTokens():
    with open('Token.txt','r') as f:
        for i in range(5):
            separator=f.readline().strip()
            if separator=="<space>":
                separator=" "
            separators.append(separator)
        for i in range(11):
            operators.append(f.readline().strip())
        for i in range(17):
            reserved.append(f.readline().strip())
