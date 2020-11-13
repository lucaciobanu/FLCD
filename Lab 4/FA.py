class FA:
    def __init__(self, states, alphabet, q0, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.q0 = q0
        self.final_states = final_states
        self.transitions = transitions



    def readFromFile(fileName):
        with open(fileName) as file:
            states = file.readline().strip().split(" ")
            alphabet = file.readline().strip().split(" ")
            q0 = file.readline()[0]
            final_states = file.readline().strip().split(" ")
            transitions = {}
            for line in file:
                source = line.strip().split("->")[0].strip().replace("(","").replace(")","").split(",")[0]
                alphabet_road = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = line.strip().split('->')[1].strip()

                if (source,alphabet_road) in transitions.keys():
                    transitions[(source,alphabet_road)].append(destination)
                else:
                    transitions[(source,alphabet_road)] = [destination]

            return FA(states, alphabet, q0, final_states, transitions)

    def checkDFA(self):
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False
        return True


fa = FA.readFromFile("FA.txt")

def menu():

    menu_switch = False
    while not menu_switch:
        print("1. Show states")
        print("2. Show alphabet")
        print("3. Show q0")
        print("4. Show final states")
        print("5. Show transitions")
        print("6. Check DFA")

        command = input()
        if command == "1":
            print("States: { " + ', '.join(fa.states) + " }")
        elif command == "2":
            print("Alphabet: { " + ', '.join(fa.alphabet) + " }")
        elif command == "3":
            print("q0: " + str(fa.q0))
        elif command == "4":
            print("Final states: { " + ', '.join(fa.final_states) + " }")
        elif command == "5":
            print("Transitions: " + str(fa.transitions))
        elif command == "6":
            print("Check DFA: " + str(fa.checkDFA()))
        elif command == "exit":
            menu_switch = True
        else:
            continue


menu()
