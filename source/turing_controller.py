from turing import TuringMachine

class TuringController:

    def __init__(self):
        self.tm = TuringMachine()
        return
    

    def initialize_tm(self, tm):
        self.tm.read_turing_machine_from_json(tm)
        return
    


    def print_tape(self, status):
        print("########################")
        print("status: ", status[1])
        print(self.tm.get_tape_content())
    

    def run_tm(self):
        self.tm.read_input()
        if self.tm.is_limited():
            active = False
            count = self.tm.get_count()
        else:
            count = -1
            active = True
        
        while active or count > 0:
            status = self.tm.transition_function()
            active = status[0]
            if self.tm.is_qout():
                self.print_tape(status)
                if self.tm.is_limited():
                    active = False
                    count -= 1
                
        self.print_tape(status)
        return
    

    def print_tm_state(self):
        tm_state = self.tm.get_tm_state()
        print("-------------------------------")
        print("state: ", tm_state[0])
        print("pos: ", tm_state[1])
        for tape in tm_state[2]:
            print(tape)
        print("-------------------------------")
