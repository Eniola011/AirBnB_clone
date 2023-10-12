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

    def do_show(self, argmt):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if not argmt:
            print("** class name missing **")
            return

        argmt = argmt.split(' ')
        if argmt[0] not in HBNBCommand.cmdClass:
            print("** class doesn't exist **")
        elif len(argmt) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, value in obj.items():
                objName = value.__class__.__name__
                objId = value.id
                if objName == argmt[0] and objId == argmt[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, argmt):
        """Deletes an instance based on the class name and id"""
        if not argmt:
            print("** class name missing **")

        argmt = argmt.split(' ')
        if argmt[0] not in HBNBCommand.cmdClass:
            print("** class doesn't exist **")
        elif len(argmt) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, value in obj.items():
                objName = value.__class__.__name__
                objId = value.id
                if objName == argmt[0] and objId == argmt[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
