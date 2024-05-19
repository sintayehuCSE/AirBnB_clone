#!/usr/bin/python3
""" A class for file storage Engine."""
import json
from datetime import datetime


class FileStorage():
    """Serialize project instances to a JSON file and
        Deserialize JSON file to instances.

        Attributes:
            __file_path (string): Path to the JSON file [ex: file.json]
            __objects (dict): Empty but will store all live objects by
                              <class name>.id (ex:  to store a BaseModel object
                              with id=12121212, the key will be
                               BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                new_dict = {}
                for key in FileStorage.__objects.keys():
                    new_dict[key] = FileStorage.__objects[key].to_dict()
                json.dump(new_dict, f)
        except IsADirectoryError:
            pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key in new_dict.keys():
                    kwargs = new_dict[key]
                    obj = self.create_obj(new_dict[key]['__class__'], **kwargs)
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, IsADirectoryError):
            pass

    def create_obj(self, class_name, **kwargs):
        from models.base_model import BaseModel

        class_dict = {
            'BaseModel': BaseModel,
            'User': 'User'
            }
        return (class_dict[class_name](**kwargs))
