class FailSafe(Exception):
    """ failsafe exception """
    def __init__(self, *args):
        super().__init__(*args)
    def __str__(self):
        return 'Failsafe triggered. Exiting bot.'


class InvalidGameplanPath(Exception):
    """ Invalid / no gameplan path found """

# add more exceptions for better debug purposes eg InvalidInstructionOption, InvalidGameplanPath