from pathlib import Path
import mouse
import keyboard
import tkinter
import sys
import ctypes
import json
import base64
import hashlib
import time

class GamePlanMaker():
    def __init__(self):
        self.keybinds = {
            "next": "l",
            "Click": "c",
            "Move": "m",
            "Wait": "w",
            "save": "ctrl+s",
            "exit": "ctrl+q",
        }
        self.gameplan = {}
        
        
        self.last_action = None

        ## TODO:  Set up event listner for keybinds when ingame


        try:
            if sys.platform == "win32":
                ctypes.windll.shcore.SetProcessDpiAwareness(2) # DPI indipendent
            tk = tkinter.Tk()
            self.width, self.height = tk.winfo_screenwidth(), tk.winfo_screenheight()
        except Exception as e:
            raise Exception("Could not retrieve monitor resolution")

    def add_item(self, item):
        self.gameplan.append(item)

    def load_temp(self, filename):
        with open(filename, "r") as f:
            for line in f:
                self.gameplan.append(line)

    def save_temp(self) -> None:
        """

        """
    
    def get_kebind(self) -> str:
        """
            Returns the keybind for the last action
        """
        
    @property
    def current_position(self) -> tuple:
        """
            Returns the current position of the mouse with normalized cordinates
        """
        x, y = mouse.get_position()
        x_norm, y_norm = x / self.width, y / self.height
        return (x_norm, y_norm)

    def init_setupfile(self):
        """
            Creates a setup file for the gameplan by asking user questions
        """
        self.difficulty = input("Difficulty: ")
        self.map = input("Map: ")
        self.hero = input("Hero: ")
        self.rounds = input("Rounds: ")
        

    def hard_save(self, filename):
        """
            Saves the gameplan to a file when done
        """
        with open(filename, "w") as f:
            for item in self.gameplan:
                f.write(item + "")

    def log(self,) -> None:
        """
            loop log which prints keybinds and last action
        """
        print('='*10)
        for keybind_key, keybind_value in self.keybinds.items():
            print(f"{keybind_key}: {keybind_value}")
        print(f"Last action: {self.last_action}")
        print('='*10)


def main():
    gamplanmaker_instance = GamePlanMaker()
    import os, sys
    # Loop 
    os.system("cls")

    while True:
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
    with open(Path(__file__).parents[1] / Path("Instructions/Dark_Castle_Hard_Standard/instructions.json"), "r") as f:
        data = str(f.readlines())
        encoded_md5 = hashlib.md5(data.encode()).hexdigest()
        print(encoded_md5)
        encoded_base64 = base64.b64encode(data.encode('ascii'))
        # print(base64.b64decode(encoded_base64))