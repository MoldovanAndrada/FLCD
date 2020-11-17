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

class Citire:
    def __init__(self):
        self.filename = ""

    def citeste(self):
        fa = FA()
        file_open = open(self.filename, "r")
        with file_open:
            fa.states = file_open.readline().split()
            fa.startingState = file_open.readline().split()
            fa.finals = file_open.readline().split()
            fa.alphabet = file_open.readline().split()

            for f in file_open.readlines():
                item = f.split()
                tr = Transition(item[0], item[1], item[2])
                fa.transitions.append(tr)
        return fa

def main():
    citire = Citire()
    citire.filename = "finiteAutomata.txt"
    fa=citire.citeste()

    #fa = FA()
    a = """
    Choose a number:
    
        1. Display the states.
        2. Display the alphabet.
        3. Display the transitions.
        4.Display the initial state.
        5.Display the final states.
        0.Exit  
    """
    while(True):
        print(a)
        number = input("Number from the menu: ");

        if number == "1":

            print("States: ")
            for s in fa.states:
                print(s)
        elif number =="2":

            print("Alphabet: ")
            for al in fa.alphabet:
                print(al)

        elif number == "3":

            print("Transitions: ")
            for t in fa.transitions:

                print(t)
        elif number =="4":

            print("Starting state: ")
            for s in fa.startingState:
                print(s)

        elif number =="5":

            print("Final states: ")
            for f in fa.finals:
                print(f)

        elif number == "0":

            break;

        else:
            print("Please enter a number from the list. ")


if __name__ == '__main__':
    main()
