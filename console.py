#!/usr/bin/env python
""" HBNB cmd console """
import cmd
import readline
import sys
from models.engine.file_storage import FileStorage

class HBNB(cmd.Cmd):
    """_summary_

    functions:
        cmd (prompt): returns command prompt
        intro: Welcome prompt message
        quit: Handles cmd exit
    """
    prompt = "(hbnb) "
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
        try:
            print("Exiting console")
            return True
        except KeyboardInterrupt:
            print("Exiting console")
        return True

    def EOF(self, arg):
        """Handle End Of File Error"""
        try:
            readline(sys.argv)
            if sys.argv[1:] == '\n':
                return True
        except EOFError:
            return ""
        
    def do_empty_line(self, arg):
        """an empty line + ENTER shouldn’t execute anything"""
        

if __name__ == "__main__":
    HBNB().cmdloop()
