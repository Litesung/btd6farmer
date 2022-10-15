from types import GeneratorType
from typing import List
import numpy as np

class Static:
    _data = {
            #   "HERO"              : [1, 2, 3]         cooldown changes with level-ups..............           notes
            "HEROS": {
                "QUINCY"            : {
                   "XP_RATIO": 1,
                   "MENU_LOCATION": [ 0.04140625 , 0.16111111111111112 ],
                   "COOLDOWN": [60, 70], # L15 [45,70]     L18 [45,55]
                   "ABILITY_UNLOCK": [3, 10]

                },
                "GWENDOLIN"         : {
                   "XP_RATIO": 1,
                   "MENU_LOCATION": [ 0.11953125 , 0.16111111111111112 ],
                   "COOLDOWN": [40, 60], # L15 [45,70]     L18 [45,55]
                   "ABILITY_UNLOCK": [3, 10]
                },
                "STRIKER_JONES"     : {
                   "XP_RATIO": 1,
                   "MENU_LOCATION": [ 0.19765625 , 0.16111111111111112 ],
                   "COOLDOWN": [16, 80], # L15 [11,80]
                   "ABILITY_UNLOCK": [3, 10]
                },
                "OBYN"              : {
                   "XP_RATIO": 1,
                   "MENU_LOCATION": [ 0.04140625 , 0.36944444444444446 ],
                   "COOLDOWN": [35, 90], # L15 [45,70]     L18 [45,55]
                   "ABILITY_UNLOCK": [3, 10]
                },
                "CAPTAIN_CHURCHILL" : {
                   "XP_RATIO": 1.71,
                   "MENU_LOCATION": [ 0.19765625 , 0.36944444444444446 ],
                   "COOLDOWN": [30, 60], # L20 [30,30]
                   "ABILITY_UNLOCK": [3, 10]
                },
                "BENJAMIN"          : {
                   "XP_RATIO": 1.5,
                   "MENU_LOCATION": [ 0.04140625 , 0.5777777777777777 ],
                   "COOLDOWN": [30, 65],
                   "ABILITY_UNLOCK": [3, 10]
                },
                "EZILI"             : {
                   "XP_RATIO": 1.425,
                   "MENU_LOCATION": [ 0.11953125 , 0.5777777777777777 ],
                   "COOLDOWN": [60, 90, 60],     # L12 [45,90,60]  L20 [45,90,40]  2n ability useless???
                   "ABILITY_UNLOCK": [3, 7, 10]
                },
                "PAT_FUSTY"         : {
                   "XP_RATIO": 1.425,
                   "MENU_LOCATION": [ 0.19765625 , 0.5777777777777777 ],
                   "COOLDOWN": [45, 20],
                   "ABILITY_UNLOCK": [3, 10]
                },
                "ADORA"             : {
                   "XP_RATIO": 1.71,
                   "MENU_LOCATION": [ 0.04140625 , 0.7861111111111111 ],
                   "COOLDOWN": [45, 10, 60], #  2n ability useless???
                   "ABILITY_UNLOCK": [3, 7, 10] 
                },
                "ADMIRAL_BRICKELL"  : {
                   "XP_RATIO": 1.425,
                   "MENU_LOCATION":  [ 0.11953125 , 0.7861111111111111 ],
                   "COOLDOWN":  [50, 60, 60],     # L13 [50,60,50]  L18 [50,60,40]
                   "ABILITY_UNLOCK": [3, 7, 10] 
                },
                "ETIENNE"           : {
                   "XP_RATIO": 1,
                   "MENU_LOCATION":  [ 0.19765625 , 0.7861111111111111 ],
                   "COOLDOWN":  [70, 90],         # L6 [55,90]      L13 [55,75]       L16 [50,75]
                   "ABILITY_UNLOCK": [3, 10]
                },
                "SAUDA"             : {
                   "XP_RATIO": 1.425,
                   "MENU_LOCATION":  [ 0.04140625 , 0.925 ],
                   "COOLDOWN":  [30, 45],
                   "ABILITY_UNLOCK": [3, 10]
                },
                "PSI"               : {
                    "XP_RATIO": 1.5,
                   "MENU_LOCATION":  [ 0.11953125 , 0.925 ],
                   "COOLDOWN":  [40, 60],
                   "ABILITY_UNLOCK": [3, 10]
                },
                "GERALDO"           : {
                    "XP_RATIO": 1,
                    "MENU_LOCATION":  [ 0.11953125 , 0.36944444444444446 ],
                    "COOLDOWN":  [],
                    "ABILITY_UNLOCK": []
                }
            },
            "KEYBINDS": {
                "UPGRADE": {
                    "TOP" : ",",
                    "MIDDLE" : ".",
                    "BOTTOM" : "/"
                },
                "TOWERS": {
                    "DART" : "q",
                    "BOOMERANG" : "w",
                    "BOMB" : "e",
                    "TACK" : "r",
                    "ICE" : "t",
                    "GLUE" : "y",
                    "SNIPER" : "z",
                    "SUBMARINE" : "x",
                    "BUCCANEER" : "c",
                    "ACE" : "v",
                    "HELI" : "b",
                    "MORTAR" : "n",
                    "DARTLING" : "m",
                    "WIZARD" : "a",
                    "SUPER" : "s",
                    "NINJA" : "d",
                    "ALCHEMIST" : "f",
                    "DRUID" : "g",
                    "BANANA" : "h",
                    "ENGINEER" : "l",
                    "SPIKE" : "j",
                    "VILLAGE" : "k",
                    "HERO" : "u"
                }
            },
            "HERO_XP": {
                1: 180,
                2: 460,
                3: 1000,
                4: 1860,
                5: 3280,
                6: 5180,
                7: 8320,
                8: 9380,
                9: 13620,
                10: 16380,
                11: 14400,
                12: 16650,
                13: 14940,
                14: 16380,
                15: 17820,
                16: 19260,
                17: 20700,
                18: 16470,
                19: 17280,
            },
            "BUTTON_CORDS": {
                "MAP_DIFFICULTIES": {   
                    "EASY_MODE"                 : [ 0.284765625 , 0.3902777777777778 ],
                    "MEDIUM_MODE"               : [ 0.480078125 , 0.3902777777777778 ],
                    "HARD_MODE"                 : [ 0.675390625 , 0.3902777777777778 ],
                },
                "GAMEMODES": {
                    "CHIMPS_MODE"               : [ 0.835546875 , 0.6805555555555556 ],
                    "DEFLATION"                 : [ 0.662890625 , 0.4166666666666667 ],
                    "SANDBOX_EASY"              : [ 0.5015625   , 0.6770833333333334 ],
                    "SANDBOX_MEDIUM"            : [ 0.667578125 , 0.6791666666666667 ],
                    "SANDBOX_HARD"              : [ 0.1453125   , 0.5458333333333333 ],
                    "PRIMARY_ONLY"              : [ 0.48671875  , 0.4152777777777778 ],
                    "APOPALYPSE"                : [ 0.667578125 , 0.4048611111111111 ],
                    "REVERSE"                   : [ 0.500390625 , 0.6798611111111111 ],
                    "MILITARY_ONLY"             : [ 0.4984375   , 0.41458333333333336],
                    "MAGIC_MONKEYS_ONLY"        : [ 0.49609375  , 0.4097222222222222 ],
                    "DOUBLE_HP_MOABS"           : [ 0.65859375  , 0.40902777777777777],
                    "HALF_CASH"                 : [ 0.83671875  , 0.40694444444444444],
                    "ALTERNATE_BLOONS_ROUNDS"   : [ 0.501171875 , 0.6680555555555555 ],
                    "IMPOPPABLE"                : [ 0.660546875 , 0.6791666666666667 ],
                    "CHIMPS"                    : [ 0.835546875 , 0.6805555555555556 ],
                    "STANDARD_GAME_MODE"        : [ 0.330859375 , 0.5416666666666666 ],
                },
                "MAP_CORDS": {
                    1               : [ 0.2734375 , 0.24305555555555555 ],
                    2               : [ 0.5546875 , 0.24305555555555555 ],
                    3               : [ 0.78125   , 0.24305555555555555 ],
                    4               : [ 0.2734375 , 0.4861111111111111 ],
                    5               : [ 0.5546875 , 0.4861111111111111 ],
                    6               : [ 0.78125   , 0.4861111111111111 ],
                },
                "MAP_MENU": {
                    "HOME_MENU_START"           : [ 0.438671875 , 0.8666666666666667 ],
                    "EXPERT_SELECTION"          : [ 0.69453125 , 0.9055555555555556 ],
                    "BEGINNER_SELECTION"        : [ 0.30390625 , 0.9055555555555556 ],
                    "RIGHT_ARROW_SELECTION"     : [ 0.856640625 , 0.4041666666666667 ],
                    "OVERWRITE_SAVE"            : [ 0.59375 , 0.6763888888888889 ],

                },
                "INGAME_MENU": {
                    "VICTORY_CONTINUE"          : [ 0.501171875 , 0.84375 ],
                    "VICTORY_HOME"              : [ 0.366796875 , 0.7805555555555556 ],
                    "DEFEAT_HOME"               : [ 0.29453125 , 0.7520833333333333 ],
                    "DEFEAT_HOME_CHIMPS"        : [ 0.36328125 , 0.7520833333333333 ],
                    "RESTART_WIN"               : [ 0.551953125 , 0.7597222222222222 ],
                    "RESTART_CONFIRM"           : [ 0.591796875 , 0.6694444444444444 ],
                    "RESTART_DEFEAT"            : [ 0.430859375 , 0.7520833333333333 ],
                    "RESTART_DEFEAT_CHIMPS"     : [ 0.5 , 0.7597222222222222 ],
                    "CONFIRM_CHIMPS"            : [ 0.500390625 , 0.6805555555555556 ],
                    "FREEPLAY"                  : [ 0.629296875 , 0.7722222222222223 ],
                    "OK_MIDDLE"                 : [ 0.5 , 0.6965277777777777 ],
                },
                "COLLECTION_EVENT": {
                    "EVENT_BUTTON"              : [ 0.499609375 , 0.6326388888888889 ],
                    "F_LEFT_INSTA"              : [ 0.3390625 , 0.5013888888888889 ],
                    "F_RIGHT_INSTA"             : [ 0.65625 , 0.5013888888888889 ],
                    "LEFT_INSTA"                : [ 0.41953125 , 0.5034722222222222 ],
                    "RIGHT_INSTA"               : [ 0.577734375 , 0.5027777777777778 ],
                    "MID_INSTA"                 : [ 0.4984375 , 0.5048611111111111 ],
                    "CONTINUE"                  : [ 0.5 , 0.9236111111111112 ],
                },
                "HERO" : {
                    "HERO_SELECT"               : [ 0.312109375 , 0.8833333333333333 ],
                    "CONFIRM_HERO"              : [ 0.587890625 , 0.5722222222222222 ],
                }

            },
            "MAPS": {
                # "NAME" : {
                #   LOCATION: [PAGE, INDEX],
                #   DIFFICULTY: 1-4
                # }
                # BEGINNER
                "MONKEY_MEADOW" : {
                    "LOCATION":[1, 1], 
                    "DIFFICULTY" : 1
                },
                "TREE_STUMP" : {
                    "LOCATION":[1, 2], 
                    "DIFFICULTY" : 1
                },
                "TOWN_CENTER" : {
                    "LOCATION":[1, 3],
                    "DIFFICULTY" : 1
                },
                "SCRAPYARD" : {
                    "LOCATION":[1, 4], 
                    "DIFFICULTY" : 1
                },
                "THE_CABIN" : {
                    "LOCATION":[1, 5], 
                    "DIFFICULTY" : 1
                }, 
                "RESORT" : {
                    "LOCATION":[1, 6], 
                    "DIFFICULTY" : 1
                },
                "SKATES" : {
                    "LOCATION":[2, 1], 
                    "DIFFICULTY" : 1
                },
                "LOTUS_ISLAND" : {
                    "LOCATION":[2, 2],
                    "DIFFICULTY" : 1
                },
                "CANDY_FALLS" : {
                    "LOCATION":[2, 3],
                    "DIFFICULTY" : 1
                },
                "WINTER_PARK" : {
                    "LOCATION":[2, 4],
                    "DIFFICULTY" : 1
                },
                "CARVED" : {
                    "LOCATION":[2, 5], 
                    "DIFFICULTY" : 1
                },
                "PARK_PATH" : {
                    "LOCATION":[2, 6], 
                    "DIFFICULTY" : 1
                },
                "ALPINE_RUN" : {
                    "LOCATION":[3, 1],
                    "DIFFICULTY" : 1
                },
                "FROZEN_OVER" : {
                    "LOCATION":[3, 2], 
                    "DIFFICULTY" : 1
                    },
                "IN_THE_LOOP" : {
                    "LOCATION":[3, 3],
                    "DIFFICULTY" : 1
                },
                "CUBISM" : {
                    "LOCATION":[3, 4],
                    "DIFFICULTY" : 1
                },
                "FOUR_CIRCLES" : {
                    "LOCATION":[3, 5],
                    "DIFFICULTY" : 1
                },
                "HEDGE" : {
                    "LOCATION":[3, 6],
                    "DIFFICULTY" : 1
                },
                "END_OF_THE_ROAD" : {
                    "LOCATION":[4, 1],
                    "DIFFICULTY" : 1
                },
                "LOGS" : {
                    "LOCATION":[4, 2],
                    "DIFFICULTY" : 1
                },
                # INTERMEDIATE
                "COVERED_GARDEN" : {
                    "LOCATION":[5, 1],
                    "DIFFICULTY" : 2
                },
                "QUARRY" : {
                    "LOCATION":[5, 2],
                    "DIFFICULTY" : 2
                },
                "QUIET_STREET" : {
                    "LOCATION":[5, 3],
                    "DIFFICULTY" : 2
                },
                "BLOONARIUS_PRIME" : {
                    "LOCATION":[5, 4],
                    "DIFFICULTY" : 2
                },
                "BALANCE" : {
                    "LOCATION":[5, 5],
                    "DIFFICULTY" : 2
                },
                "ENCRYPTED" : {
                    "LOCATION":[5, 6],
                    "DIFFICULTY" : 2
                },
                "BAZAAR" : {
                    "LOCATION":[6, 1],
                    "DIFFICULTY" : 2
                },
                "ADORAS_TEMPLE" : {
                    "LOCATION":[6, 2],
                    "DIFFICULTY" : 2
                },
                "SPRING_SPRING" : {
                    "LOCATION":[6, 3],
                    "DIFFICULTY" : 2
                },
                "KARTSNDARTS" : {
                    "LOCATION":[6, 4],
                    "DIFFICULTY" : 2
                },
                "MOON_LANDING" : {
                    "LOCATION":[6, 5],
                    "DIFFICULTY" : 2
                },
                "HAUNTED" : {
                    "LOCATION":[6, 6],
                    "DIFFICULTY" : 2
                },
                "DOWNSTREAM" : {
                    "LOCATION":[7, 1],
                    "DIFFICULTY" : 2
                },
                "FIRING_RANGE" : {
                    "LOCATION":[7, 2],
                    "DIFFICULTY" : 2
                }, 
                "CRACKED" : {
                    "LOCATION":[7, 3],
                    "DIFFICULTY" : 2
                },
                "STREAMBED" : {
                    "LOCATION":[7, 4],
                    "DIFFICULTY" : 2
                },
                "CHUTES" : {
                    "LOCATION":[7, 5],
                    "DIFFICULTY" : 2
                },
                "RAKE" : {
                    "LOCATION":[7, 6],
                    "DIFFICULTY" : 2
                },
                "SPICE_ISLANDS" : {
                    "LOCATION":[8, 1],
                    "DIFFICULTY" : 2
                },
                # ADVANCED
                "MIDNIGHT_MANSION" : {
                    "LOCATION":[9, 1],
                    "DIFFICULTY" : 2
                },
                "SUNKEN_COLUMNS" : {
                    "LOCATION":[9, 2], 
                    "DIFFICULTY" : 3
                },
                "XFACTOR" : {
                    "LOCATION":[9, 3], 
                    "DIFFICULTY" : 3
                },
                "MESA" : {
                    "LOCATION":[9, 4], 
                    "DIFFICULTY" : 3
                },
                "GEARED" : {
                    "LOCATION":[9, 5], 
                    "DIFFICULTY" : 3
                },
                "SPILLWAY" : {
                    "LOCATION":[9, 6], 
                    "DIFFICULTY" : 3
                },
                "CARGO" : {
                    "LOCATION":[10, 1], 
                    "DIFFICULTY" : 3
                },
                "PATS_POND" : {
                    "LOCATION":[10, 2], 
                    "DIFFICULTY" : 3
                },
                "PENINSULA" : {
                    "LOCATION":[10, 3], 
                    "DIFFICULTY" : 3
                },
                "HIGH_FINANCE" : {
                    "LOCATION":[10, 4], 
                    "DIFFICULTY" : 3}
                , 
                "ANOTHER_BRICK" : {
                    "LOCATION":[10, 5], 
                    "DIFFICULTY" : 3
                },
                "OFF_THE_COAST" : {
                    "LOCATION":[10, 6], 
                    "DIFFICULTY" : 3
                },
                "CORNFIELD" : {
                    "LOCATION":[11, 1], 
                    "DIFFICULTY" : 3
                },
                "UNDERGROUND" : {
                    "LOCATION":[11, 2], 
                    "DIFFICULTY" : 3
                },
                # EXPERT
                "SANCTUARY" : {
                    "LOCATION":[12, 1], 
                    "DIFFICULTY" : 4
                },
                "RAVINE" : {
                    "LOCATION":[12, 2], 
                    "DIFFICULTY" : 4
                },
                "FLOODED_VALLEY" : {
                    "LOCATION":[12, 3], 
                    "DIFFICULTY" : 4
                },
                "INFERNAL" : {
                    "LOCATION":[12, 4], 
                    "DIFFICULTY" : 4
                },
                "BLOODY_PUDDLES" : {
                    "LOCATION":[12, 5], 
                    "DIFFICULTY" : 4
                },
                "WORKSHOP" : {
                    "LOCATION":[12, 6], 
                    "DIFFICULTY" : 4
                },
                "QUAD" : {
                    "LOCATION":[13, 1], 
                    "DIFFICULTY" : 4
                },
                "DARK_CASTLE" : {
                    "LOCATION":[13, 2], 
                    "DIFFICULTY" : 4
                },
                "MUDDY_PUDDLES" : {
                    "LOCATION":[13, 3], 
                    "DIFFICULTY" : 4
                },
                "OUCH" : {
                    "LOCATION":[13, 4], 
                    "DIFFICULTY" : 4
                }
         
            }
        }

    @property
    def heros(self):
        return self._data["HEROS"]

    @property
    def tower_keybinds(self):
        return self._data["KEYBINDS"]["TOWERS"]

    @property
    def button_locations(self):
        return self._data["BUTTON_CORDS"]

    @property
    def map(self):
        return self._data["MAPS"]

    @property
    def upgrade_keybinds(self):
        return self._data["KEYBINDS"]["UPGRADE"]




    # Index, regular targets, spike factory targets
    target_order_regular = [ "FIRST", "LAST", "CLOSE", "STRONG" ]
    target_order_spike   = [ "NORMAL", "CLOSE", "FAR", "SMART" ]


class Hero(Static):
    """
        Gets values from static when init
    """
    def __init__(self, hero_name:str, gameplan:dict, _map:object):
        
        self.xp_ratio                     = Static._data["HEROS"][hero_name]["XP_RATIO"]
        self.menu_location                = Static._data["HEROS"][hero_name]["MENU_LOCATION"]
        self.cooldown_time                = Static._data["HEROS"][hero_name]["COOLDOWN"]
        self.ability_levels_unlocked_list = Static._data["HEROS"][hero_name]["ABILITY_UNLOCK"]

        self.round_placed = self.get_round_placed(gameplan)
        self.xp_map = self.xp_gained_per_round(_map)

        self.ability_round_avaliable = [_round for _round in self.abilies_available]

        self.name = hero_name

    def get_round_placed(self, gameplan):
        for _round in gameplan.keys():
            for instruction in gameplan[_round]:
                if instruction["INSTRUCTION_TYPE"] == "PLACE_TOWER":
                    if instruction["ARGUMENTS"]["MONKEY"] == "HERO":
                        return int(_round)
    
    @property
    def cooldown(self):
        return self.cooldown_time

    @property
    def cords(self):
        return Static._data["HEROS"][self.name]["MENU_LOCATION"]

    @property
    def xp_per_level(self):
        return Static._data["HERO_XP"]

    def xp_gained_per_round(self, map):
        """
            A method which will return how much XP a hero will gain per round (if its placed ofc)

            Round 1 starts off with 40 XP, and up until round 20 this amount increases by 20 each round (40 XP, 60 XP, 80 XP, and so on). Then on rounds 21-50 the amount experience gained each round increases by 40 each round (460 XP, 500 XP, and so on). And last, from round 51 and further, this amount increases by 90 each round (1710 XP, 1800 XP, and so on). Adding this up, you get a total of 231,150 XP in a game from round 6 to round 100 on Impoppable or C.H.I.M.P.S.. Each map difficulty above beginner gives a 10% xp bonus, e.g. playing on expert gives you a 30% XP boost. 

            TODO: Calculate base xp gain per level
            https://github.com/hemisemidemipresent/cyberquincy/blob/dd41deb3fe44f0812331649c541344005b360a59/helpers/heroes.js#L54-L93
        """

        LEVELING_MAP_DIFFICULTY_MODIFIERS = {
            1: 1.0,  # "BEGINNER"
            2: 1.1,  # "INTERMEDIATE"
            3: 1.2,  # "ADVANCED"
            4: 1.3,  # "EXPERT"
        }

        ENERGIZER_MODIFIER = 1

        acc_xp_gain = {}

        gain = 0
        for r in range(1, 101):
            if r == 0:
                gain = 0
            elif r == 1: # starts off with 40 XP
                gain += 40
            elif r < 21: # r2-r20
                gain += 20
            elif r < 51: # r21-r50
                gain += 40
            else:        # 90 gain
                gain += 90

            acc_xp_gain[r] = gain * LEVELING_MAP_DIFFICULTY_MODIFIERS[map.difficulty] * ENERGIZER_MODIFIER

        return acc_xp_gain
    
    @property
    def abilies_available(self) -> GeneratorType:
        """
        Will return a list rounds that all hero abilities should be unlocked

        NOTES: 
            - All heroes have a specific XP ratio. Heroes with a higher XP ratio require more XP to level up and therefore level up slower.
            - Heroes gain XP at the end of the round by the same formula as towers
            - Each hero has multiple abilities (all have two with the exception of Ezili, Adora, and Admiral Brickell, who have three and Geraldo who has one) 
                that can be used to the player's advantage. The first ability is unlocked at level 3, and the second ability is unlocked at level 10; 
                for Ezili, Adora and Brickell, they gain their second ability at level 7 and third at level 10. 
                The highest level a hero can reach is 20. 
            - Hero XP amount is calculate the same way as tower xp https://bloons.fandom.com/wiki/Experience_Points#BTD6

        For example:
            - Obyn has a xp ratio of 1.0. He gets his abillity at round 3 and 10.
                If he is placed at round lvl 12 he will get his abilities at round 14 and 51

        TODO: 
            - Add support for energizer (Energizer is the only tower that increases levelling speed.)
            - MK or support for everyone w/o MK? 
                - There are several Monkey Knowledge points that can affect hero levelling:
                    - Self Taught Heroes: +10% XP
                    - Monkey Education: +8% XP
                    - Monkeys Together Strong: +5% XP
                    - Scholarships: -10% cost
            - Each map difficulty above beginner gives a 10% xp bonus, e.g. playing on expert gives you a 30% XP boost. 
        """
        # for for every level that a ability is unlocked
        for level_ability_unlocked in self.ability_levels_unlocked_list:

            # reset hero abillity counter to the round the hero was placed
            round_since_hero_placed = self.round_placed

            # Defined xp_sum to the amount of xp earned at the end of the round
            accumilated_xp_sum = self.xp_map[round_since_hero_placed]

            # Calculate the total xp needed to reach ability level    
            total_hero_xp_needed = 0
            for hero_level, xp_gained_amount in self.xp_per_level.items():
                if hero_level < level_ability_unlocked:
                    total_hero_xp_needed += xp_gained_amount 

            total_hero_xp_needed *= self.xp_ratio
            
            while accumilated_xp_sum < np.round(total_hero_xp_needed):
                
                # XP gain undefined after round 100
                if round_since_hero_placed > 100:
                    xp_gain += self.xp_map[100]
                
                round_since_hero_placed += 1
                accumilated_xp_sum += np.round(self.xp_map[round_since_hero_placed])

            # When xp_sum is greater than to the xp needed for the next level, we have found the round
            yield round_since_hero_placed + 1
    


class Map(Static):
    """
        Gets values from static when init
    """

    def __init__(self, map_name, gamemode, difficulty):
        self.map_name = map_name
        self.__gamemode = gamemode
        self.__difficulty = difficulty # Difficulty in the map

    @property
    def page(self):
        return Static._data["MAPS"][self.map_name]["LOCATION"][0]

    @property
    def index(self):
        return Static._data["MAPS"][self.map_name]["LOCATION"][1]

    @property
    def cords(self ):
        """
        """
        return Static._data["BUTTON_CORDS"]["MAP_CORDS"][self.index]

    @property
    def difficulty(self) -> int:
        """
            Returns the difficulty of the map represented by an integer
                1 = Beginner
                2 = Intermediate
                3 = Advanced
                4 = Expert
        """
        return self._data["MAPS"][self.map_name]["DIFFICULTY"]
    
    @property
    def map_difficulty(self) -> str:
        """
            Returns the map difficulty 

            ### TODO: hardcode this to make the user only need to choose the gamemode

        """
        return Static._data["BUTTON_CORDS"]["MAP_DIFFICULTY"][self.__difficulty]

    @property
    def gamemode_cords(self) -> List[float]:
        return Static._data["BUTTON_CORDS"]["GAMEMODES"][self.__gamemode]


class Generic(Static):

    @property
    def buttons(self):
        return Static._data["BUTTON_CORDS"]

    @property
    def upgrade_keybinds(self):
        return Static._data["KEYBINDS"]["UPGRADE"]

    @property
    def home_menu_start(self):
        return Static._data["BUTTON_CORDS"]["MAP_MENU"]["HOME_MENU_START"]
    
    # MAPS menu
    @property
    def expert_button(self):
        return Static._data["BUTTON_CORDS"]["MAP_MENU"]["EXPERT_SELECTION"]


    @property
    def beginner_button(self):
        return Static._data["BUTTON_CORDS"]["MAP_MENU"]["BEGINNER_SELECTION"]


    @property
    def right_arrow_button(self):
        return Static._data["BUTTON_CORDS"]["MAP_MENU"]["RIGHT_ARROW_SELECTION"]


    @property
    def overwrite_save(self):
        return Static._data["BUTTON_CORDS"]["MAP_MENU"]["OVERWRITE_SAVE"]

    # Ingame buttons
    @property
    def victory_continue(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["VICTORY_CONTINUE"]
    
    @property
    def victory_home(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["VICTORY_HOME"]

    @property
    def defeat_home(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["DEFEAT_HOME"]

    @property
    def defeat_chimps_home(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["DEFEAT_HOME_CHIMPS"]

    @property
    def restart_win(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["RESTART_WIN"]

    @property
    def restart_confirm(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["RESTART_CONFIRM"]

    @property
    def restart_defeat(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["RESTART_DEFEAT"]

    @property
    def restart_defeat_chimps(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["RESTART_DEFEAT_CHIMPS"]

    @property
    def confirm_chimps(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["CONFIRM_CHIMPS"]

    @property
    def freeplay(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["FREEPLAY"]

    @property
    def ok_middle(self):
        return Static._data["BUTTON_CORDS"]["INGAME_MENU"]["OK_MIDDLE"]

    # COLLECTION EVENTs
    @property 
    def collection_event_button(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["EVENT_BUTTON"]

    # TODO: detect insta monkeys and click on their position instead of just clicking randomly
    @property
    def f_left_insta(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["F_LEFT_INSTA"]

    @property
    def f_right_insta(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["F_RIGHT_INSTA"]

    @property
    def left_insta(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["LEFT_INSTA"]

    @property
    def right_insta(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["RIGHT_INSTA"]

    @property
    def middle_insta(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["MID_INSTA"]

    @property
    def collection_continue(self):
        return Static._data["BUTTON_CORDS"]["COLLECTION_EVENT"]["CONTINUE"]

    # Hero menu
    @property
    def hero_menu_button(self):
        return Static._data["BUTTON_CORDS"]["HERO"]["HERO_SELECT"]

    @property
    def hero_confirm(self):
        return Static._data["BUTTON_CORDS"]["HERO"]["CONFIRM_HERO"]


    
    

