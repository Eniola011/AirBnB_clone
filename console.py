#!/usr/bin/python3
"""Command-Line Interpreter"""


import json
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "
    cmdClass = ["BaseModel"]

    def emptyline(self):
        pass

    def do_create(self, MyModel):
        """Creates a new instance of BaseModel"""
        if not MyModel:
            print("** class name missing **")
        elif MyModel not in HBNBCommand.cmdClass:
            print("** class doesn't exist **")
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
