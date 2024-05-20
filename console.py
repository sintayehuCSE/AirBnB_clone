#!/usr/bin/python3
"""The entry point of the command interpreter for
    ABNB Clone project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A simple framework for line-oriented command interpretor
        of Abnb Clone project
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Make the interpretor passive and do nothing
            on recieving emptly line + keyboard ENTER hit.
        """
        pass
    
    def do_quit(self, arg):
        """Qiuts the command interpretor session."""
        return True
    
    def do_EOF(self, arg):
        """Qiuts the command interpretor session."""
        print(arg)
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
