#!/usr/bin/python3
"""Console Module"""

import cmd 
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True 
    
    def do_EOF(self, args):
        """Exits on EOF"""
        return True

    def emptyline(self):
        """Don't execute anything on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
