from pathlib import Path
from threading import Thread
import mouse
import keyboard
import tkinter
import sys
import ctypes
import json
import base64
import hashlib
import time
import os 
import sys



import json
from _ctypes import PyObj_FromPtr
import re
# from pprint import pprint

inputFile = r"C:\Users\limpan\Documents\GitHub\btd6farmer\Instructions\Dark_Castle_Hard_Standard\instructions.json"

# https://stackoverflow.com/questions/13249415/how-to-implement-custom-indentation-when-pretty-printing-with-the-json-module

# converter: https://raw.githubusercontent.com/linus-jansson/btd6farmer/d8e722f15a91e3987da03cf58ab9a78a64bbd33d/bottools/convert_gameplan_to_v1.py

class NoIndent(object):
    """ Value wrapper. """
    def __init__(self, value):
        self.value = value


class MyEncoder(json.JSONEncoder):
    FORMAT_SPEC = '@@{}@@'
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

    def __init__(self, **kwargs):
        # Save copy of any keyword argument values needed for use here.
        self.__sort_keys = kwargs.get('sort_keys', None)
        super(MyEncoder, self).__init__(**kwargs)

    def default(self, obj):
        return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent)
                else super(MyEncoder, self).default(obj))

    def encode(self, obj):
        format_spec = self.FORMAT_SPEC  # Local var to expedite access.
        json_repr = super(MyEncoder, self).encode(obj)  # Default JSON.

        # Replace any marked-up object ids in the JSON repr with the
        # value returned from the json.dumps() of the corresponding
        # wrapped Python object.
        for match in self.regex.finditer(json_repr):
            # see https://stackoverflow.com/a/15012814/355230
            id = int(match.group(1))
            no_indent = PyObj_FromPtr(id)
            json_obj_repr = json.dumps(no_indent.value, sort_keys=self.__sort_keys)

            # Replace the matched id string with json formatted representation
            # of the corresponding Python object.
            json_repr = json_repr.replace(
                            '"{}"'.format(format_spec.format(id)), json_obj_repr)

        return json_repr


"""
TODO plans: 
    - if prompt user for inputs, wait for user to be done...
    - the user can specify the path to the instructions if they want to edit it ( replaces the need for a temp file), just save to the main instructions file
"""

class GamePlanMaker():
    def __init__(self):
        def test():
            print("hello world")


        ## TODO: Possible to provide arguments to keybind thread?
        self.keybinds = {
            "next_round": {
                "keybind": "ctrl+n+r",
                "callback": test
            },
            "save_instruction": {
                "keybind": "ctrl+s",
                "callback": test
            },
            "Undo": {
                "keybind": "ctrl+z",
                "callback": test
            },
            "redo": {
                "keybind": "ctrl+r",
                "callback": test
            },
            "save": {
                "keybind": "ctrl+S",
                "callback": test
            },
            "exit": {
                "keybind": "ctrl+Q",
                "callback": self.exit
            },
        }

        self.gameplan = {}
        self.gameplan_before = {}
        self.running = True
        self.threads = []
        
        # Sets up keybind listner
        for keybind_descriptor, keybind_dict in self.keybinds.items():
            key, callback_function = keybind_dict.values()
            print("DEBUG: adding keybind: \n{}".format(keybind_dict))
            self.add_key_listner(key, callback_function)
        

        try:
            if sys.platform == "win32":
                ctypes.windll.shcore.SetProcessDpiAwareness(2) # DPI indipendent
            tk = tkinter.Tk()
            self.width, self.height = tk.winfo_screenwidth(), tk.winfo_screenheight()
        except Exception as e:
            raise Exception("Could not retrieve monitor resolution")


        # Loads temp file if it exists
        # else creates a new gameplan instance with temp file
        # Prompting the user to a new setup

    def exit(self, save_temp=True):
        """
            Exits the gameplan maker
        """
        try:
            if save_temp:
                tempfile_path = self.save_tempfile()
                print("Saved temp gameplan in {}".format(tempfile_path))

            
        except Exception as e:
            print("Could not save temp file")
            print(e) 
        finally:
            self.running = False ## Stops the main while loop
            sys.exit() # Exit the thread

    def add_key_listner(self, key, callback_function, *cb_args):
        """
            Creates a thread for a keybind with a callback function to be called when the keybind is pressed
        """
        def listen_for_key(key, callback_function):
            is_pressed = False
            while True:
                if keyboard.is_pressed(key) and not is_pressed:
                    print("DEBUG: Key pressed: " + key)
                    is_pressed = True
                    callback_function() # calls the function provided
                elif not keyboard.is_pressed(key): # reset is_pressed when key is released
                    is_pressed = False
                

        self.threads.append(Thread(target=listen_for_key, args=(key, callback_function,), daemon=True).start())
        

    def add_item(self, item):
        self.gameplan.append(item)

    def load_tempfile(self):
        filename = "tmp"
        with open(filename, "r") as f:
            self.gameplan = json.load(f)


    def save_tempfile(self) -> str:
        """
            Everytime self.gameplan is changed save to tempfile

            returns the filepath to the saved temp file
        """
    
    @property
    def last_action(self) -> str | None:
        """
            Returns the keybind for the last action
        """
        return None
        
    @property
    def current_position(self) -> tuple:
        """
            Returns the current position of the mouse with normalized cordinates
        """
        x, y = mouse.get_position()
        x_norm, y_norm = x / self.width, y / self.height
        return (x_norm, y_norm)

    def increment_round(self):
        """
            Increments the round
        """
        pass

    def insert_instruction(self, instruction):
        """
            Inserts an instruction into the gameplan
        """
        pass

    def init_setupfile(self):
        """
            Creates a setup file for the gameplan by asking user questions

            TODO: Print instructions to the user (how to use) then propmt with questions
        """
        self.difficulty = input("Difficulty: ")
        self.map = input("Map: ")
        self.hero = input("Hero: ")
        self.rounds = input("Rounds: ")
        

    def final_save(self):
        """
            Saves the gameplan to a file when done

            TODO: get map, diff, gamemode from setup dict or file
        """
        path = path(__file__).resolve().parents[1]/path("Instructions/{}_{}_{}".format(self.map, self.difficulty, self.gamemode))
        
        if not path.is_dir():
            path.mkdir(parents=True)

        with open(path/"instructions.json", "w") as f:
            for item in self.gameplan:
                f.write(item + "")

    def log(self,) -> None:
        """
            loop log which prints keybinds and last action

            TODO: ADD print for current round in gameplan
        """
        print('='*10)
        for keybind_key, keybind_value in self.keybinds.items():
            print(f"{keybind_key}: {keybind_value}")
        print(f"Last action: {self.last_action}")
        print('='*10)

    
    def SET_STATIC_TARGET(self):
        tower_position = self.current_position
        print("Waiting.. Move mouse to position of static target then press ctrl + enter")
        keyboard.wait("ctrl+enter")
        target_position = self.current_position
        instruction = {}

        instruction["INSTRUCTION_TYPE"] = "SET_STATIC_TARGET"
        instruction["ARGUMENTS"] = {
            "LOCATION": tower_position,
            "TARGET": target_position
        }

        return instruction

    def UPGRADE_TOWER(self):
        tower_position = self.current_position
        try:
            upgrade_path = input("What tower are you placing? up, middle, bottom")
            upgrade_path = list(map(int, upgrade_path.replace(" ", "").split(",")))
        except:
            print("Invalid input for upgrade path")


        instruction = {}

        instruction["INSTRUCTION_TYPE"] = "UPGRADE_TOWER"
        instruction["ARGUMENTS"] = {
            "LOCATION": tower_position,
            "UPGRADE_PATH": upgrade_path # Convert old format to new
        }

        return instruction

    def PLACE_TOWER(self):
        tower_position = self.current_position
        tower = input("What tower are you placing? ")
        instrucion = {}
        
        instrucion["INSTRUCTION_TYPE"] = "PLACE_TOWER"
        instrucion["ARGUMENTS"] = {
            "MONKEY": tower,
            "POSITION": tower_position
        }
        
        return instrucion


    def ROUND_START(self):
        """
            Inserts a round start instruction:

            {
                "INSTRUCTION_TYPE": "START",
                "ARGUMENTS": {
                    "FAST_FORWARD": true
                }
            }
        """
        instruction = {}

        instruction["INSTRUCTION_TYPE"] = "START"
        instruction["ARGUMENTS"] = {
            "FAST_FORWARD": True
        }

        return instruction

    def CHANGE_TARGET(self):
        tower_position = self.current_position
        target_type = input("What target type are you changing REGULAR or SPIKE? ")
        targets = input("What targets? ")
        delay = None
        instruction = {}

        # print("INSTRUCTION CHANGE TARGET")
        instruction["INSTRUCTION_TYPE"] = "CHANGE_TARGET"

        instruction["ARGUMENTS"] = {
            "LOCATION": tower_position,
            "TARGET": targets.split(","),
            "TYPE": target_type,  
            "DELAY": delay
        }

        return instruction


def main():
    gamplanmaker_instance = GamePlanMaker()
    # os.system("cls||clear")

    ## TODO: set up event listner for keybinds when ingame

    while gamplanmaker_instance.running:
        # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        # print(chr(27) + "[2J")
        sys.stdout.write("\r")
        sys.stdout.flush()
        # gamplanmaker_instance.log()
        sys.stdout.write(str(gamplanmaker_instance.current_position))
        # gamplanmaker_instance.log()
        # print(gamplanmaker_instance.current_position)
        # time.sleep(0.2)

if __name__ == "__main__":
    main()
    # import zlib
    # with open(Path(__file__).parents[1] / Path("Instructions/Dark_Castle_Hard_Standard/instructions.json"), "r") as f:
    #     data = str(f.readlines())
    #     encoded_md5 = hashlib.md5(data.encode()).hexdigest()
    #     print(encoded_md5)
    #     encoded_base64 = base64.b64encode(data.encode('ascii'))

    #     compress_zlib = zlib.compress(data.encode())
    #     print(compress_zlib)
    #     # print(base64.b64decode(encoded_base64))