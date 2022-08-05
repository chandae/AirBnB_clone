#!/usr/bin/python3
"""
    AIRBNB_Clone Console Module

    Description: Allows interaction with project models/objects interactively.
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        AirBnB Clone Console

        Supported commands:
            help/? - display help information (documentation)
    """
    intro = None
    prompt = '(hbnb) '

    # ----- basic console commands -----
    def do_create(self, args: str):
        """
            Create new BaseModel instance and save it to JSON file
            prints the instance id
            Usage: create <ClassName>
        """

        # initialise a list for commands
        cmds = args.split()

        if len(cmds) == 0:
            print("** class name is missing **")
            return

        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        try:
            # create new object: cmd[0] is class name
            # expression below evaluates to <ClassName>()
            # Example: BaseModel()
            newObject = eval(cmds[0])()
            print(newObject.id)
            newObject.save()
        except Exception as e:
            print("Exception: ", e)

    def do_update(self, args: str):
        """
            Update an instance based on class name and id
            Update: add or update instance attribute
            Only one attribute can be updated at a time

            Usage: update <ClassName> <id> <attribute name> <attribute value>
        """

        cmds = args.split()

        # Validate class name input
        if len(cmds) == 0:
            print("** class name missing **")
            return
        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return
        # Validate instance id input
        if len(cmds) == 1:
            print("** instance id missing **")
            return

        storage.reload()
        obj = storage.all()
        key = f"{cmds[0]}.{cmds[1]}"
        instance = obj.get(key)

        if not obj.get(key, None):
            print("** no instance found **")
            return
        if len(cmds) == 2:
            print("** attribute name missing **")
            return
        if len(cmds) == 3:
            print("** value missing **")
            return

        try:
            cmds[3] = cmds[3].strip('"')
            attr_type = type(getattr(instance, cmds[3]))
            cmds[3] = attr_type(cmds[3])
        except AttributeError:
            pass

        # Update the given instance attribute and save json file
        setattr(instance, cmds[2], cmds[3])
        storage.save()

    def do_show(self, args: str):
        """
            Print string representation of an instance based on:
            <ClassName> <obj id>

            Usage: show <ClassName> <obj id>
            Example: show BaseModel 3fde12f9-4002-4cd7-869c-c4c019eedae4
        """

        # Initialise a list for commands
        cmds = args.split()

        # Validate class name input
        if len(cmds) == 0:
            print("** class name missing **")
            return
        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        # Validate instance id input
        if len(cmds) == 1:
            print("** instance id missing **")
            return

        # Reload all objects in json file
        storage.reload()
        obj = storage.all()
        key = f"{cmds[0]}.{cmds[1]}"

        if obj.get(key, None):
            print(obj[key])
        else:
            print("** no instance found **")
        return

    def do_all(self, args: str):
        """
            Print all string representation
            of all instances if no class is given
            Print all string representation
            of all instances of a given class

            Usage 1: all
            Usage 2: all <ClassName>
        """

        # Load json file data
        storage.reload()
        obj = storage.all()

        # Initialise a list for commands
        cmds = args.split()

        if len(cmds) == 0:
            output = [f"{str(obj[key])}" for key in obj]
            print(output)
            return
        if len(cmds) == 1:
            try:
                eval(cmds[0])
            except NameError:
                print("** class doesn't exist**")
                return

            output = [f"{str(obj[key])}" for key in obj if cmds[0] in key]
            print(output)

    def do_destroy(self, args: str):
        """
            Deletes an instance using the given instance class and ID:
            <ClassName> <obj id>

            Usage: destroy <ClassName> <obj id>
            Example: destroy BaseModel 3fde12f9-4002-4cd7-869c-c4c019eedae4
        """

        # Initialise a list for commands
        cmds = args.split()

        # Validate class name input
        if len(cmds) == 0:
            print("** class name missing **")
            return
        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        # Validate instance id input
        if len(cmds) == 1:
            print("** instance id missing **")
            return

        try:
            storage.reload()
            obj = storage.all()
            key = f"{cmds[0]}.{cmds[1]}"
            del obj[key]
        except KeyError:
            print("** no instance found **")
            return

        # Save and Update json file
        storage.save()

    def do_quit(self, line):
        """ Exit Console """
        return True

    def emptyline(self) -> bool:
        """
            Invoked when empty line is entered in the prompt
            THe console does not execute anything
        """
        pass

    def do_EOF(self, line):
        """
            End of File Marker: Exit
        """
        return True

    def default(self, line: str) -> None:
        """
            Invoked when command is not recognised
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
