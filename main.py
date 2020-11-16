class Transition:
    def __init__(self, state1, state2, alphabet):
        self.state1=state1
        self.state2=state2
        self.alphabet=alphabet

    def __str__(self):
        return "(" + self.state1 + ", " + self.alphabet + ") = " + self.state2

class FA:
    def __init__(self):
        self.startingState = []
        self.states = []
        self.transitions = []
        self.alphabet = []
        self.finals= []
        file_open = open("finiteAutomata.txt","r")
        with file_open:
            self.states = file_open.readline().split()
            self.startingState = file_open.readline().split()
            self.finals = file_open.readline().split()
            self.alphabet = file_open.readline().split()

            for f in file_open.readlines():
                item = f.split()
                tr= Transition(item[0], item[1], item[2])
                self.transitions.append(tr)


def main():
    fa = FA()
    print ("States: " )
    for s in fa.states:
        print(s)
    print("Alphabet: ")
    for a in fa.alphabet:
        print(a)
    print("Transitions: " )
    for t in fa.transitions:
        print(t)
    print("Starting state: ")
    for s in fa.startingState:
        print(s)
    print("Final states: ")
    for f in fa.finals:
        print(f)

if __name__ == '__main__':
    main()