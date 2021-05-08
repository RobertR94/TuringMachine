from turing_controller import TuringController
import json


class UserController:

    def __init__(self):
        self.valid_menu_inputs = {"Add", "Run", "List", "Exit"}
        self.valid_list_inputs = {"Back"}
        self.list_of_tms = dict()
        self.current_tm = None
        return
    

    def get_tms(self):
        with open("../data/turing.json") as tms:
            data = json.load(tms)
        
        for tm in data.keys():
            self.list_of_tms[tm] = data[tm]["discription"]
    

    def select_tm(self, tm):
        print("herer: ", tm)
        self.current_tm = tm



    def list_tms(self):
        list_tm = True
        while list_tm:
            print("\n\n--------------List of Tm--------------\n\n\n")
            for elem in self.list_of_tms.keys():
                print("TM name: ", elem, " | ", "description: ", self.list_of_tms[elem])
        
            print("\n\n1. Select Tm: [TM-name]")
            print("2. Back: [Back]")
            print("\nSelected Tm: ", self.current_tm)
            print("\n\n")
            in_put = input("Selection: ")
            if in_put in self.list_of_tms.keys():
                self.select_tm(in_put)
            elif in_put == "Back":
                list_tm = False
        return


    def run(self):
        print("\n\n--------------Start Tm--------------\n\n\n")
        tc = TuringController()
        tc.initialize_tm(self.current_tm)
        tc.run_tm()
        not_valid_in = True
        while not_valid_in:
            in_put = input("Back to menu [Yes]? ")
            if in_put == "Yes":
                not_valid_in = False
        return


    def menu(self):
        self.get_tms()
        menu = True
        wrong_input = False
        no_tm = False
        while menu:
            print("\n\n--------------Turingemulator--------------\n\n\n")
            if wrong_input:
                print("\n\nPlease enter a valid command!\n\n")
            elif no_tm:
                print("\n\nPlease select a valid Tm\n\n")
            print("1. Add Tm: [Add]")
            print("2. List Tms: [List]")
            print("3. Select Tm: [TM-name]")
            print("3. Run: [Run]")
            print("4. Exit: [Exit]")
            print("\nSelected Tm: ", self.current_tm)
            print("\n\n")
            in_put = input("Selection: ")
            if in_put == "Exit":
                return
            elif in_put == "List":
                wrong_input = False
                self.list_tms()
            elif in_put == "Run":
                if self.current_tm in self.list_of_tms.keys():
                    self.run()
                    no_tm = False
                else:
                    no_tm = True
            elif in_put in self.list_of_tms.keys():
                self.select_tm(in_put)
            else:
                wrong_input = True
        return
