#!/usr/bin/python3
"""Command-Line Interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "

    do_quit(self, line):
        """Quit: to exit the program"""
        return True

    do_EOF(self, line):
        """EOF: to exit the program"""
        return True

    do_EmptyLine(self, line):
        """Empty line + ENTER shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
