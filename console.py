#!/usr/bin/env python3
"""Shell console for the application"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreters for HBNB."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        Usage: show <class name> <class id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Usage: destroy <class name> <class id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name.

        Usage: all <class name> or all <.>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg == '.':
            objs = storage.all()
        else:
            try:
                cls = eval(arg)
                objs = storage.all(cls)
            except NameError:
                print("** class doesn't exist **")
                return
        for obj_id in objs.keys():
            obj = objs[obj_id]
            print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objs[key]
        attr_name = args[2]
        attr_value = args[3]

        setattr(obj, attr_name, attr_value)

    def do_quit(self, line):
        """Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_count(self, cls_name):
        """Counts the number of instances of a class."""
        count = 0
        objs = storage.all()

        for key, value in objs.items():
            cls = key.split('.')
            if cls[0] == cls_name:
                count += 1
        print(count)

    def do_EOF(self, line):
        """exit the program with EOF."""
        print()
        return True

    def emptyline(self):
        """Empty line does nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
