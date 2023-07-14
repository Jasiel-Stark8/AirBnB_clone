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

    def create(self):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        pass

    def show(self):
        """Prints the string representation of an instance based on the class name and id"""
        pass

    def destroy(self):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        pass

    def all(self):
        """Prints all string representation of all instances based or not on the class name"""
        pass

    def update(self):
        """ Updates an instance based on the class name and id by adding \
            or updating attribute (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
