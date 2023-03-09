#!/usr/bin/env python3
"""Shell console for the application"""
import cmd
from models.base_model import BaseModel
from models import storage


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

        del cls
        cls = eval(args[0])

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """exit the program with EOF."""
        print()
        return True

    def emptyline(self):
        """Empty line does nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
