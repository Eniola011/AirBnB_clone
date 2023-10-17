#!/usr/bin/python3
"""Command-Line Interpreter"""


import json
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_count(self, classname):
        """retrieve the number of instances of a class:
        <class name>.count().
        """
        count = 0
        objs = storage.all()
        for key, value in objs.items():
            cls = key.split('.')
            if cls[0] == classname:
                count = count + 1
        print(count)

    def do_create(self, MyModel):
        """Creates a new instance of BaseModel"""
        if not MyModel:
            print("** class name missing **")
        elif MyModel not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dictList = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                        'City': City, 'Amenity': Amenity, 'State': State,
                        'Review': Review}
            model = dictList[MyModel]()
            print(model.id)
            model.save()

    def do_show(self, argmts):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if not argmts:
            print("** class name missing **")
            return

        argmt = argmts.split(' ')
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

    def do_destroy(self, argmts):
        """Deletes an instance based on the class name and id"""
        if not argmts:
            print("** class name missing **")

        argmt = argmts.split(' ')
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

    def do_all(self, argmts):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        if not argmts:
            print("** class name missing **")
        argmt = argmts.split(' ')
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

    def do_update(self, argmts):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if not argmts:
            print("** class name missing **")
            return
        arg = ""
        for argv in argmts.split(','):
            arg = arg + argv
        argmt = shlex.split(arg)

        if argmt[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(argmt) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, val in obj.items():
                objName = val.__class__.__name__
                objId = val.id
                if objName == argmt[0] and objId == argmt[1].strip('"'):
                    if len(argmt) == 2:
                        print("** attribute name missing **")
                    elif len(argmt) == 3:
                        print("** value missing **")
                    else:
                        setattr(key, argmt[2], argmt[3])
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
