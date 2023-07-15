#!/usr/bin/python3
"""Console Module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

CLS_LIST = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '
    storage.reload()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits on EOF"""
        return True

    def emptyline(self):
        """Don't execute anything on empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance, saves it and prints the id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in CLS_LIST:
            print("** class doesn't exist **")
            return
        new_inst = eval(args[0])()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, args):
        """Print the instance as a string"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in CLS_LIST:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        try:
            eval(args[0])
            print(obj_dict[f"{args[0]}.{args[1]}"])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance and saves to JSON file"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in CLS_LIST:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        try:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
            del obj_dict[f"{args[0]}.{args[1]}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints string representations of instances"""
        obj_list = []
        obj_dict = storage.all()
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance and saves to JSON file"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLS_LIST:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        try:
            obj = obj_dict[f"{args[0]}.{args[1]}"]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        # Check for valid attr
        if args[2] not in obj.__class__.__dict__:
            print(f"** attribute {args[2]} not found **")
            return

        # Set attr and save
        attr = args[2]
        value = args[3]
        setattr(obj, attr, value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()