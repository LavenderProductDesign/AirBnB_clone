#!/usr/bin/python3
import cmd
"""
A program that contains the entry point of the command interpreter
"""


class HBNCommand(cmd.Cmd):
    """a class constructor"""

    prompt = '(hbnc) '

    def do_EOF(self, line):
        """"Exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        return


if __name__ == '__main__':
    HBNCommand().cmdloop()
