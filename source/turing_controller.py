from turing import TuringMachine

class TuringController:

    def __init__(self):
        self.tm = TuringMachine()
        return
    

    def initialize_tm(self, tm):
        self.tm.read_turing_machine_from_json(tm)
        return
    

    def run_tm(self):
        self.tm.read_input()
        active = True
        while active:
            status = self.tm.transition_function()
            active = status[0]

        print("Done")
        print("status: ", status[1])
        print(self.tm.get_tape_content())
        return
