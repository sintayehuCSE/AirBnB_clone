#!/usr/bin/python3
"""The entry point of the command interpreter for
    ABNB Clone project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel.
            Saves it (to the JSON file) and
            Prints the id of this new object
        """
        constructor = self.find_class(arg)
        if constructor:
            obj = constructor()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
            on its class-name and its id.
        """
        class_name, obj_id = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            obj = self.find_obj(class_name, obj_id)
            if obj:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on its class-name and ID and
            Saves the change into the JSON file.
        """
        class_name, obj_id = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            obj = self.find_obj(class_name, obj_id)
            if obj:
                live_obj = storage.all()
                key = "{}.{}".format(class_name, obj_id)
                del live_obj[key]
                del obj
                storage.save()

    def do_all(self, arg):
        """Prints a list of string representation of all instance based or
            not on the class name.
        """
        live_obj = storage.all()
        str_repr = []
        if arg:
            constructor = self.find_class(arg)
            if constructor:
                for key in live_obj.keys():
                    if type(live_obj[key]).__name__ == arg:
                        str_repr.append(str(live_obj[key]))
                print(str_repr)
        else:
            for key in live_obj.keys():
                str_repr.append(str(live_obj[key]))
            print(str_repr)

    def do_update(self, arg):
        """Update an instance based on the class name and its ID
            by adding or updating attribute. Does save the change
            to JSON file.
        """
        class_name, obj_info = self.parse_arg(arg)
        constructor = self.find_class(class_name)
        if constructor:
            old_identchars = self.identchars
            self.identchars = self.identchars + '-"'
            obj_id, obj_attr = self.parse_arg(obj_info)
            obj = self.find_obj(class_name, obj_id)
            if obj:
                attr_name, attr_value = self.parse_arg(obj_attr)
                if not attr_name:
                    print("** attribute name missing **")
                elif not attr_value:
                    print("** value missing **")
                else:
                    attr_value, other_arg = self.parse_arg(attr_value)
                    attr_value = attr_value.strip('"')
                    cnst = (attr_name != 'id' and attr_name != 'created_at'
                            and attr_name != 'updated_at')
                    if cnst:
                        if hasattr(obj, attr_name):
                            try:
                                attr_type = type(obj.__dict__[attr_name])
                                setattr(obj, attr_name, attr_type(attr_value))
                            except KeyError:
                                attr_type = type(type(obj).__dict__[attr_name])
                                setattr(obj, attr_name, attr_type(attr_value))
                        else:
                            setattr(obj, attr_name, attr_value)
                        obj.save()
            self.identchars = old_identchars

    def do_User(self, arg):
        """Print List of all instances of User class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is User:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is User:
                    count += 1
            print(count)                

    def do_BaseModel(self, arg):
        """Print List of all instances of BaseModel class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is BaseModel:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is BaseModel:
                    count += 1
            print(count)

    def do_Place(self, arg):
        """Print List of all instances of Place class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Place:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Place:
                    count += 1
            print(count)

    def do_State(self, arg):
        """Print List of all instances of State class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is State:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is State:
                    count += 1
            print(count)

    def do_City(self, arg):
        """Print List of all instances of City class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is City:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is City:
                    count += 1
            print(count)

    def do_Amenity(self, arg):
        """Print List of all instances of Amenity class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Amenity:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Amenity:
                    count += 1
            print(count)

    def do_Review(self, arg):
        """Print List of all instances of Review class. OR thier count"""
        if arg == ".all()":
            inst = []
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Review:
                    inst.append(str(live_obj[key]))
            print(inst)
        elif arg == '.count()':
            count = 0
            live_obj = storage.all()
            for key in live_obj.keys():
                if type(live_obj[key]) is Review:
                    count += 1
            print(count)

    def find_class(self, arg):
        """Check if a specified class name is valid
            Args:
                arg (str): User-input class-name
            Return:
                1. Requested Class constructor if arg is valid class-name OR
                2. None if arg is not valid class-name.
        """
        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'State': State,
            'Amenity': Amenity,
            'Review': Review
        }
        if not arg:
            print("** class name missing **")
            return None
        try:
            return class_dict[arg]
        except KeyError:
            print("** class doesn't exist **")
            return None

    def parse_arg(self, arg):
        """Parse the input argument to the command of HBNB interpretor
            Divide the argument into two parts.
            Args:
                arg (str): The input argument to the HBNB interpretor
                command OR its fragment.
            Return:
                (first_arg, second_arg) (tuple): Return tuple of argument
                recieved from input or its fragment after successive call.
        """
        i, n = 0, len(arg)
        while (i < n and arg[i] in self.identchars):
            if arg[i] == '"':
                i = i + 1
                while arg[i] != '"':
                    i = i + 1
                else:
                    i = i + 1
                    break
            else:
                i = i + 1
        first_arg, second_arg = arg[:i], arg[i + 1:]
        return first_arg, second_arg

    def find_obj(self, class_name, obj_id):
        """Check if object with the specified ID is a live object.
            Args:
                class_name (str): The class of the object
                obj_id (str): The object ID
            Return:
                The live object OR None
        """
        live_obj = storage.all()

        if not obj_id:
            print("** instance id missing **")
            return None
        try:
            key = "{}.{}".format(class_name, obj_id)
            return live_obj[key]
        except KeyError:
            print("** no instance found **")
            return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
