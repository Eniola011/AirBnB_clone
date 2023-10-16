#!/usr/bin/python3
"""Command-Line Interpreter"""


import json
import cmd
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
                'Amenity', 'Place', 'Review']

    commands = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, MyModel):
        """Creates a new instance of BaseModel"""
        if not MyModel:
            print("** class name missing **")
        elif MyModel not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dictList = {'BaseModel': BaseModel}
            model = dictList[MyModel]()
            print(model.id)
            model.save()

    def do_show(self, argmt):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if not argmt:
            print("** class name missing **")
            return

        argmt = argmt.split(' ')
        if argmt[0] not in HBNBCommand.classes:
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
        if argmt[0] not in HBNBCommand.classes:
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

    def do_all(self, argmt):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        if not argmt:
            print("** class name missing **")
        argmt = argmt.split(' ')
        if argmt[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            allInstance = []
            for key, value in obj.items():
                objName = value.__class__.__name__
                if objName == argmt[0]:
                    allInstance += [value.__str__()]
            print(allInstance)

    def do_update(self, argmt):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if not argmt:
            print("** class name missing **")
            return
        arg = ""
        for i in argmt.split(','):
            arg = arg + i
        argmts = shlex.split(arg)

        if argmts[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(argmts) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, val in obj.items():
                objName = val.__class__.__name__
                objId = val.id
                if objName == argmt[0] and objId == argmt[1].strip('"'):
                    if len(argmts) == 2:
                        print("** attribute name missing **")
                    elif len(argmts) == 3:
                        print("** value missing **")
                    else:
                        setattr(key, argmts[2], argmts[3])
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
