#!/usr/bin/python3
"""
    AIRBNB_Clone Console Module

    Description: Allows interaction with project models/objects interactively.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        AirBnB Clone Console

        Supported commands:
            help/? - display help information (documentation)
    """
    intro = None
    prompt = '(hbnb) '
    file = None

    # ----- basic console commands -----
    def do_quit(self, line):
        """ Exit Console """
        return True

    def emptyline(self) -> bool:
        """
            Invoked when empty line is entered in the prompt
            THe console does not execute anything
        """
        pass

    def do_EOF(self, line):
        """
            End of File Marker: Exit
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
