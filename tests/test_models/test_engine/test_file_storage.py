#!/usr/bin/python3
"""
Test for storage engine class.
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage Engine class."""
    def test_obje_creation(self):
        """Check cretion of Storage object."""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_FileStorage__objects(self):
        """Test the type of __object container holding live objecct."""
        self.assertIs(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage__file_path(self):
        """Test the type of __file_path of Storage engine."""
        self.assertIs(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_all(self):
        """check presence of all() method in Engine file."""
        self.assertIsNotNone(FileStorage().all())

    def test_FileStorage_new(self):
        """check presence of new() method in Engine file."""
        b = BaseModel()
        self.assertIsNone(FileStorage().new(b))

    def test_FileStorage_save(self):
        """check presence of save() method in Engine file."""
        self.assertIsNone(FileStorage().save())

    def test_reload(self):
        """check presence of reload() method in Engine file."""
        self.assertIsNone(FileStorage().reload())

    def test_method_documented(self):
        """Check if method of thee class are documented."""
        self.assertIsNotNone(FileStorage.all.__dict__)
        self.assertIsNotNone(FileStorage.new.__dict__)
        self.assertIsNotNone(FileStorage.save.__dict__)
        self.assertIsNotNone(FileStorage.reload.__dict__)


if __name__ == "__main__":
    unittest.main()
