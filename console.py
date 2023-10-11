#!/usr/bin/python3
"""Command-Line Interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_EmptyLine(self, line):
        """Empty line + ENTER shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
