


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
            initial=f.readline().strip().split(' ')[2:][0]
            final=f.readline().strip().split(' ')[2:]
            # print(states,alphabet,initial,final)
            f.readline()
            transitions={}
            for line in f:
                simplifyed=line.strip().split(' ')
                state,alph,to=simplifyed[1], simplifyed[3], simplifyed[6]
                transitions[(state,alph)]=to
                # print(state,alph,to)

            # validating
            if initial not in states:
                raise Exception("Invalid finite automata! The initial state is not in the set of states")
            for fini in final:
                if fini not in states:
                    raise Exception("Invalid finite automata! The final states are not in the set of states")
            for key in transitions:
                if key[0] not in states:
                    raise Exception("Invalid finite automata! One of the states is not in the set of states")
                if key[1] not in alphabet:
                    raise Exception("Invalid finite automata! One of the symbols is not in the set of symbols")
                for dest in transitions[key]:
                    if dest not in states:
                        raise Exception("Invalid finite automata! One of the states is not in the set of states")
            return FiniteAutomata(states,alphabet,initial,final,transitions)
    def isDfa(self):
        for key in self.transition.keys():
            if len(self.transition[key]) > 1:
                return False
        return True

    def isAccepted(self,seq):
        if self.isDfa():
            temporarState=self.initialState
            for symbol in seq:
                if (temporarState,symbol) in self.transition.keys():
                    temporarState=self.transition[(temporarState,symbol)][0]
                else:
                    return False
            if temporarState in self.finalState:
                return True
            else:
                return False
        return False

