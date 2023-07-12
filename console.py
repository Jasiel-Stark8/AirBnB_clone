#!/usr/bin/env python
""" HBNB cmd console """
import cmd
from models.base_model import BaseModel

class Console(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_

    Returns:
        _type_: _description_
    """
    prompt = "cmd"
    intro = "Welcome to HBNB cmd console\n"

    # def do_help(self):
    #     print("Available commands:")
    #     print("  help - this message")
    #     print("  exit - exit the console")
    #     print("  list - list all models")
    #     print("  create - create a new model")
    #     print("  update - update an existing model")
    #     print("  delete - delete an existing model")
    #     print("  get - get an existing model")
    #     print("  set - set an existing model")
    
    def do_exit(self, arg):
        print("Exiting console")
        return True
    
    def do_create(self, arg):
        """create an object of Base and print it's ID"""
        Object = BaseModel()
        print(object.id)
    
if __name__ == "__main__":
    Console().cmdloop()
