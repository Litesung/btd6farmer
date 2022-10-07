import time
import copy
import tkinter
import sys
import ctypes
import json


from Static import Hero, Map

class BotConfig:
    """
        Holds all information that the user passed into the script
            - Gameplan
            - Setup file

        Also holds generic information souch as screen resolution
    """
    def __init__(self, user_args):
        self.path = user_args["path"]

        self.bot_start_time = time.time()
        self.game_start_time = time.time()

        self.debug_mode   = user_args["debug"]
        self.verbose_mode = user_args["verbose"]
        self.restart_mode = user_args["restart"]
        self.sandbox_mode = user_args["sandbox"]

        self.gameplan = self._load_json(self.path/ "instructions.json")
        self.gameplan_settings = self._load_json(self.path / "setup.json")
        
        self._game_plan_copy = copy.deepcopy(self.gameplan) # Unmodified version of gameplan

        # Gets all neccecary information from the static classes
        self.map = Map(self.map_name, self.gamemode, self.difficulty)
        self.hero = Hero(self.hero_name, self._game_plan_copy, self.map)

        try:
            if sys.platform == "win32":
                ctypes.windll.shcore.SetProcessDpiAwareness(2) # DPI indipendent
            
            tk = tkinter.Tk()
            self.width, self.height = tk.winfo_screenwidth(), tk.winfo_screenheight()

            # if sys.platform == "linux":
            #     import subprocess
            #     output = subprocess.Popen('xrandr | grep "primary" | grep -Eo "[0-9][0-9][0-9][0-9]x[0-9][0-9][0-9][0-9]" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
            #     if len(output) > 0:
            #         output = output.decode("utf-8").replace("\n", "")
            #         self.width, self.height = map(int, output.split("x"))

        except Exception as e:
            raise Exception("Could not retrieve monitor resolution")

    # @property
    # def gameplan(self):
    #     return self.gameplan

    @property
    def version(self):
        return self.gameplan_settings["VERSION"]

    @property
    def hero_name(self):
        return self.gameplan_settings["HERO"]

    @property
    def map_name(self):
        return self.gameplan_settings["MAP"]
    
    @property
    def difficulty(self):
        return self.gameplan_settings["DIFFICULTY"]
    
    @property
    def gamemode(self):
        return self.gameplan_settings["GAMEMODE"]


    def restore_gameplan(self):
        self.gameplan = copy.deepcopy(self._game_plan_copy)

    def _load_json(self, path):
        """
            Will read the @path as a json file load into a dictionary.
        """
        data = {}
        with path.open('r', encoding="utf-8") as f:
            data = json.load(f)
        return data

