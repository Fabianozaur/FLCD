from FiniteAutomata import FiniteAutomata

class main:
    def run(self):
        while True:
            print()
            print("1. Read FA from file")
            print("2. Display the set of states")
            print("3. Display the alphabet")
            print("4. Display the transitions")
            print("5. Display the set of final states")
            print("6. Check if FA is DFA")
            print("7. Check is a sequence if accepted")
            print("8. Exit")
            print("> ")
            command=input()
            if command == "1":
                self.fa=FiniteAutomata.readFromFA('fa.in')
            elif command == "2":
                print("The set of states is: "+ str(self.fa.states))
            elif command == "3":
                print("The Alphabet is: "+ str(self.fa.alphabet))
            elif command == "4":
                print("The Transitions are: "+ str(self.fa.transition))
            elif command == "5":
                print("The set of final states is: "+ str(self.fa.finalState))
            elif command == "6":
                if self.fa.isDfa():
                    print("FA is a DFA")
                else:
                    print("FA is not a DFA")
            elif command == "7":
                sequence=input("Please input a sequence: ")
                if self.fa.isAccepted(sequence):
                    print("Sequence is accepted")
                    continue
                print("Sequence is not accepted")
            elif command == "8":
                break
            else:
                continue


main().run()

