class FailSafe(Exception):
    """ failsafe exception """
    def __init__(self, *args):
        super().__init__(*args)
    def __str__(self):
        return 'Failsafe triggered. Exiting bot.'


# add more exceptions for better debug purposes eg InvalidInstructionOption, InvalidGameplanPath