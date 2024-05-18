#!/usr/bin/python3
"""This is a module that define a base model class of the project."""
import uuid
from datetime import datetime


class BaseModel():
    """A basemodel for all the object of this project."""
    def __init__(self):
        """Initialize the common attributes of this project's objet."""
        self.id = str(uuid.uuid4())
        self.created_at = (datetime.now())
        self.updated_at = (datetime.now())

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        attribute_dict = self.__dict__.copy()
        attribute_dict['created_at'] = attribute_dict['created_at'].isoformat()
        attribute_dict['updated_at'] = attribute_dict['updated_at'].isoformat()
        attribute_dict['__class__'] = type(self).__name__
        return (attribute_dict)

    def __str__(self):
        """Return a nice printable string representation of the object."""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))
