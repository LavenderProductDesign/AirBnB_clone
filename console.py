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
        """Calls promt with empty line + ENTER"""
        return

    def do_create(self, line):
        """Created new instance of BaseModel, saves it(to JSON file)
           and prints the id
        """
        pass

    def do_show(self, line):
        """Print the string representation of an instance based on the
           class name and id.
        """
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)
        """
        pass

    def do_all(self, line):
        """Prints all string representation of all instanced based or not
           on the class name.
        """
        pass

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
           updating attribute (save the change into the JSON file).
        """
        pass


if __name__ == '__main__':
    HBNCommand().cmdloop()
