#!/usr/bin/python3
"""Console Module"""

import cmd
import json
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

    def do_emptyline(self):
        """Don't execute anything on empty line"""
        pass  # Leave like this

    def do_create(self, ):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not __class__.__name__:
            print("** class name missing **")
        if __class__.__name__ is None:
            print("** class doesn't exist **")
        
        else:
            create = BaseModel()
            with open(f"{create.id}.json", "w", encoding='UTF-8') as f:
                json.dump(create.__dict__, f)

    def do_show(self):
        """Prints the string representation of an instance based on the class name and id"""
        if not __class__.__name__:
            print("** class name missing **")
        if __class__.__name__ is None:
            print("** class doesn't exist **")
        if not id:
            print("** instance id missing **")
        if (__class__.__name__, id) not in 'create.id.json':
            print("** no instance found **")
        print(f"{self.__class__.__name__} {'create.id.json'}")

    def do_destroy(self):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not __class__.__name__:
            print("")

    def do_all(self):
        """Prints all string representation of all instances based or not on the class name"""
        pass

    def do_update(self):
        """ Updates an instance based on the class name and id by adding \
            or updating attribute (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
