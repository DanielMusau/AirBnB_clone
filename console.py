#!/usr/bin/env python3
"""Shell console for the application"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreters for HBNB."""
    prompt = '(hbnb) '

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
