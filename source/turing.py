import json


class TuringMachine:

    def __init__(self):
        # _ is the blank symbol
        self.discription = str()
        self.in_put_alphabet = set()
        self.tape_alpahabet = set("_")
        self.states = set()
        self.initial_state = None
        self.final_states = set()
        self.tapes = None
        self.pos = None
        self.current_state = None
        self.move_set = {"N": 0, "L": -1, "R": +1}
        self.machine_states = ("Final_State", "Hold", "Error", "Run")
        self.konfiguration = None
        #transitions as dict where the key is a string of the current State and pos
        #e.g q_0,a : (q_1, [(b, R)])
        #e.g for two tapes q_0,a,b : (q_1, [(b,R), (a,L)])
        self.transitions = dict()
    

    def set_tape_alpahabet(self, tape_alphabet):
        self.tape_alpahabet = tape_alphabet
    

    def set_in_alphabet(self, in_put_alphabet):
        if in_put_alphabet.issubset(self.set_in_alphabet):
            self.in_put_alphabet = in_put_alphabet
            return True
        else:
            return False
    

    def set_states(self, states):
        self.states = states
    

    def set_final_states(self, final_states):
        if final_states.issubset(self.states):
            self.set_final_states = final_states
            return True
        else:
            return False


    def set_transitions(self, transitions):
        self.transitions = transitions
    


    def create_transition_key(self):
        key = self.current_state
        for tape, pos in enumerate(self.pos):
            key = key + "," + self.tapes[tape][pos]
        
        return key


    def add_new_blank(self, tape_num):
        self.tapes[tape_num].append("_")
        


    def update_tapes(self, moves):
        for tape, elem in enumerate(moves):
            if elem[0] in self.tape_alpahabet:
                pos = self.pos[tape]
                self.tapes[tape][pos] = elem[0]
                if pos == len(self.tapes[tape]) - 1:
                    self.add_new_blank(tape)
                self.pos[tape] += self.move_set[elem[1]]
            else:
                return False
        return True



    def transition_function(self):
        print("###############/n/n")
        key = self.create_transition_key()
        if key in self.transitions.keys():
            print("from: ", key)
            print("too: ", self.transitions[key])
            print("old_tape: ", self.tapes)
            trans = self.transitions[key]
            self.current_state = trans[0]
            moves = trans[1]
            if self.update_tapes(moves):
                print("new_tape: ", self.tapes)
                if self.current_state in self.final_states:
                    return (False, self.machine_states[0])
                return (True, self.machine_states[3])
            else:
                return (False, self.machine_states[2])
        else:  
            return (False, self.machine_states[1])
        
    
   
    def write_input(self, input_str):
        for elem in input_str:
            if elem not in self.in_put_alphabet:
                return False
            self.tapes[0].append(elem)
        return True


    def get_konfiguration(self):
        return self.konfiguration
    

    
    def read_turing_machine_from_json(self, machine_name):
        with open("../data/turing.json") as tms:
            data = json.load(tms)
        
        machine = data[machine_name]
        self.discription = machine["discription"]
        self.num_tapes = machine["num_tapes"]
        self.in_put_alphabet = set(machine["input_alphabet"])
        self.tape_alpahabet = set(machine["tape_alphabet"])
        self.initial_state = machine["initial_state"]
        self.current_state = self.initial_state
        self.states = set(machine["states"])
        self.final_states = set(machine["final_states"])
        self.transitions = machine["transitions"]

        num_tapes = machine["num_tapes"]
        self.tapes = [list() for i in range(num_tapes)]
        self.pos = [0 for i in range(num_tapes)]


    def read_input(self):
        in_put = str()
        incorect = True
        while(incorect):
            incorect = False
            print("/n Input alphabet: ", self.in_put_alphabet, "/n")
            in_put = input("input: ")
            for x in in_put:
                if x not in self.in_put_alphabet:
                    corect = True
                    break
        
        self.write_input(in_put)
        return True
    

    def get_tape_content(self):
        return self.tapes[0]
