from fileinput import filename
from pathlib import Path
from threading import Thread
try:
    import mouse
    import keyboard
except ImportError:
    print("you need to run this script using sudo")
    sys.exit(1)


import tkinter
import sys
import ctypes
import json
import base64
import hashlib
import time
import os 
import sys
import argparse
import zlib

import json
from _ctypes import PyObj_FromPtr
import re
# from pprint import pprint

# https://stackoverflow.com/questions/13249415/how-to-implement-custom-indentation-when-pretty-printing-with-the-json-module

# converter: https://raw.githubusercontent.com/linus-jansson/btd6farmer/d8e722f15a91e3987da03cf58ab9a78a64bbd33d/bottools/convert_gameplan_to_v1.py

class NoIndent(object):
    """ Value wrapper. """
    def __init__(self, value):
        self.value = value


class JsonObjEncoder(json.JSONEncoder):
    """
        Sorts gameplan for easier navigation
    """

    FORMAT_SPEC = '@@{}@@'
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

    def __init__(self, **kwargs):
        # Save copy of any keyword argument values needed for use here.
        self.__sort_keys = kwargs.get('sort_keys', None)
        super(JsonObjEncoder, self).__init__(**kwargs)

    def default(self, obj):
        return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent)
                else super(JsonObjEncoder, self).default(obj))

    def encode(self, obj):
        format_spec = self.FORMAT_SPEC  # Local var to expedite access.
        json_repr = super(JsonObjEncoder, self).encode(obj)  # Default JSON.

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
    def __init__(self, compress_save=False, debug=False, existing_gameplan=None):
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
            "place_tower": {
                "keybind": "ctrl+p",
                "callback": self.PLACE_TOWER
            },
            "upgrade_tower": {
                "keybind": "ctrl+u",
                "callback": self.UPGRADE_TOWER
            },
            "set_static_target": {
                "keybind": "ctrl+s+t",
                "callback": self.SET_STATIC_TARGET
            },
            "set_round_start": {
                "keybind": "ctrl+r+s",
                "callback": self.ROUND_START
            },
            "change_target": {
                "keybind": "ctrl+c+t",
                "callback": self.CHANGE_TARGET
            },
            "debug_test": {
                "keybind": "ctrl+shift+t",
                "callback": self.INSERT_DEBUG_TEST
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
        self.should_compress = compress_save



        self.threads = []
        self.DEBUG_MODE = debug
        
        # Sets up keybind listner
        for keybind_descriptor, keybind_dict in self.keybinds.items():
            key, callback_function = keybind_dict.values()
            if self.DEBUG_MODE:
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
        if existing_gameplan:
            self.existing_gameplan_path = Path(__file__).resolve().parents[1] / Path(existing_gameplan)
            self.load_gameplan()
        else:
            # Prompting the user to a new setup
            self.init_setupfile()
                       
        # else creates a new gameplan instance with temp file

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
                    if self.DEBUG_MODE:
                        print("DEBUG: Key pressed: " + key)

                    is_pressed = True
                    callback = callback_function() # calls the function provided
                    if isinstance(callback, dict):
                        if self.DEBUG_MODE:
                            print("DEBUG: Added instruction to round {}".format(self.current_round))
                        
                        # If the round is not yet in the gameplan, add it
                        if self.gameplan.get(self.current_round) is None:
                            self.gameplan[self.current_round] = []

                        # append the instruction to the current round
                        self.gameplan[self.current_round].append(callback)

                        d = self.save_gameplan()
                        if self.DEBUG_MODE and d:
                            print("DEBUG: Saved gameplan to {}".format(d))

                elif not keyboard.is_pressed(key): # reset is_pressed when key is released
                    is_pressed = False
                

        self.threads.append(Thread(target=listen_for_key, args=(key, callback_function,), daemon=True).start())
        

    def add_item(self, item):
        self.gameplan.append(item)

    def load_gameplan(self):
        """
            loads an already existing gameplan
        """
        try:
            # try to load the save file as a normal json
            # filename = self.existing_gameplan_path
            with open(self.existing_gameplan_path, "r") as f:
                self.gameplan = json.load(f)
        except:
            try:
                # try to parse the file as compress by decompressing
                with open(self.existing_gameplan_path, "rb") as f:
                    self.gameplan = json.loads(zlib.decompress(f.read()))
            except:
                raise Exception("Could not load existing save file")
            

    def save_gameplan(self) -> str | None:
        """
            Saves the gameplan to a file

            returns the filepath to the saved temp file
        """
        filename = "gameplantest.json"
        if self.should_compress:
            import zlib
            with open(filename, "wb") as f:
                compressed_data = zlib.compress(json.dumps(self.gameplan, cls=JsonObjEncoder, indent=None).encode("utf-8"))
                f.write(compressed_data)
                # json.dump(self.gameplan, f, indent=4, cls=JsonObjEncoder)
        else:
            with open(filename, "w") as f:
                json.dump(self.gameplan, f, cls=JsonObjEncoder, indent=None)
            
            return filename

    def save_tempfile(self) -> str | None:
        """
            Everytime self.gameplan is changed save to tempfile

            returns the filepath to the saved temp file
        """
        return None
    
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

    @property
    def current_round(self) -> str:
        """
            Returns the current selected round
        """
        self._current_round = 1
        return str(self._current_round)


    def increment_round(self) -> None:
        """
            Increments the round
        """
        self._current_round += 1 

    def decrease_round(self) -> None:
        """
            Increments the round
        """
        if self._current_round > 0:
            self._current_round -= 1


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
        print("Welcome to the gameplan maker")
        input("Press enter to continue")


        settings = {
            "VERSION": 1,
            "HERO": input("Hero: "),
            "MAP": input("Map: "),
            "DIFFICULTY": input("DIFFICULTY: "),
            "GAMEMODE": input("Gamemode: ")
        }

        gameplan_path = Path(__file__).resolve().parents[1] / Path("{}_{}_{}".format(settings["MAP"], settings["DIFFICULTY"], settings["GAMEMODE"]))
        
        # create folder of not exist
        if not gameplan_path.exists():
            gameplan_path.mkdir()

        # create setup file with settings data
        with open(gameplan_path / Path("setup.json"), "w") as f:
            json.dump(settings, f, indent=4)

        

    def final_save(self):
        """
            Saves the gameplan to a file when done

            TODO: get map, diff, gamemode from setup dict or file
        """
        path = Path(__file__).resolve().parents[1]/Path("Instructions/{}_{}_{}".format(self.map, self.difficulty, self.gamemode))
        
        if not path.is_dir():
            path.mkdir(parents=True)

        with open(path/"instructions.json", "w") as f:
            for item in self.gameplan:
                f.write(item + "")

    def log_round_instructions(self) -> None:
        """
            Logs the instructions for the current round to output
        """
        pass

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

    def validate_user_input(self, dictionary, user_input):
        """
            Validates user input.

            If the input (key) is valid return its dictionary value
        """
        keys = dictionary.keys()
        
        if user_input in keys:
            return dictionary[user_input]
        else:
            return None


    def INSERT_DEBUG_TEST(self) -> dict:
        """
            Debug function for testing
        """
        position = self.current_position

        instruction = {}
        instruction["INSTRUCTION_TYPE"] = "TEST_INSTRUCTION"
        instruction["ARGUMENTS"] = {
            "LOCATION": position,
        }

        return instruction

    def SET_STATIC_TARGET(self) -> dict:
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

    def UPGRADE_TOWER(self) -> dict | None:
        tower_position = self.current_position
        try:
            upgrade_path = input("What tower are you placing? up, middle, bottom (ex 1, 0, 2) > ")
            upgrade_path = list(map(int, upgrade_path.replace(" ", "").split(",")))
        except:
            print("Invalid input for upgrade path")
            return None

        instruction = {}

        instruction["INSTRUCTION_TYPE"] = "UPGRADE_TOWER"
        instruction["ARGUMENTS"] = {
            "LOCATION": tower_position,
            "UPGRADE_PATH": upgrade_path # Convert old format to new
        }

        return instruction

    def PLACE_TOWER(self) -> dict | None:
        tower_position = self.current_position
        tower = input("What tower are you placing? ")
        instrucion = {}
        
        instrucion["INSTRUCTION_TYPE"] = "PLACE_TOWER"
        instrucion["ARGUMENTS"] = {
            "MONKEY": tower,
            "POSITION": tower_position
        }
        
        return instrucion


    def ROUND_START(self) -> dict | None:
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

    def CHANGE_TARGET(self) -> dict:
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


def main(parser):
    args = vars(parser.parse_args())
    gamplanmaker_instance = GamePlanMaker(compress_save=args["compress"], debug=args["debug"], existing_gameplan=args["reuse"])
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
    parser = argparse.ArgumentParser(description="Gameplan maker")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")
    parser.add_argument("-r", "--reuse", type=str, help="Modify a already existing gameplan")
    parser.add_argument("-c", "--compress", action="store_true", help="Compresses saved gameplan with zlib")
    
    main(parser)
    # import zlib
    # with open(Path(__file__).parents[1] / Path("Instructions/Dark_Castle_Hard_Standard/instructions.json"), "r") as f:
    #     data = str(f.readlines())
    #     encoded_md5 = hashlib.md5(data.encode()).hexdigest()
    #     print(encoded_md5)
    #     encoded_base64 = base64.b64encode(data.encode('ascii'))

    #     compress_zlib = zlib.compress(data.encode())
    #     print(compress_zlib)
    #     # print(base64.b64decode(encoded_base64))