


class FiniteAutomata:
    def __init__(self,states,alphabet,initalState,finalStates,transition):
        self.states=states
        self.alphabet=alphabet
        self.initialState=initalState
        self.finalState=finalStates
        self.transition=transition

    @staticmethod
    def readFromFA(file):
        with open(file) as f:
            states=f.readline().strip().split(' ')[2:]
            alphabet=f.readline().strip().split(' ')[2:]
            initial=f.readline().strip().split(' ')[2:]
            final=f.readline().strip().split(' ')[2:]
            print(states,alphabet,initial,final)
            f.readline()
            transitions={}
            for line in f:
                simplifyed=line.strip().split(' ')
                state,alph,to=simplifyed[1], simplifyed[3], simplifyed[6]
                transitions[(state,alph)]=to
                print(state,alph,to)
            print(transitions)

FiniteAutomata.readFromFA('fa.in')