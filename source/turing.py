
class TuringMachine():

    def __init__(self, num_tapes: int):
        # _ is the blank symbol
        self.in_put_alphabet = set()
        self.tape_alphabet = set().add("_")
        self.states = set()
        self.initial_state = "q_0"
        self.final_states = set()
        self.tapes = [[] for i in range(num_tapes)]
        self.pos = [0 for i in range(num_tapes)]
        self.current_state = self.initial_state
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
        for tape, pos in enumerate(self.postions):
            key + "," + self.tapes[tape][pos]
        
        return key


    def update_tapes(self, moves):
        for tape, elem in enumerate(moves):
            if elem[0] in self.tape_alphabet:
                pos = self.pos[tape]
                self.tapes[tape][pos] = elem[0]
                self.pos[tape] += self.move_set[elem[1]]
            else:
                return False
        return True



    def transition_function(self):
        key = self.create_transition_key()
        if key in self.transitions.keys():
            trans = self.transitions[key]
            self.current_state = trans[0]
            moves = trans[1]
            if self.update_tapes(moves):
                if self.current_state in self.final_states:
                    return self.machine_states[0]
                return self.machine_states[3]
            else:
                return self.machine_states[2]
        else:  
            return self.machine_states[2]
        
    
   
    def write_input(self, input_str):
        for elem in input_str:
            if elem not in self.in_put_alphabet:
                return False
            self.tapes[0].append(elem)
        return True

    def get_konfiguration(self):
        return self.konfiguration
    

    def start_run(self, max_steps = None: int):
        if max_steps == None:

    
