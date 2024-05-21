#!/usr/bin/python3
"""
Test the fILE STORAGE Engine.
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage

class Test_FileStorage(unittest.TestCase):
    """Test File Storage Engine class."""
    def test_instance(self):
        """Test creation of storage class object."""
        store_obj = FileStorage()
        self.assertIsInstance(store_obj, FileStorage)

    def test_doc(self):
        """Check if sTorage function are documented or not."""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_type__file_path(self):
        """check for file_path type as only string."""
        self.assertIs(str, type(FileStorage._FileStorage__file_path))

    def test_type__objects(self):
        """Test if private __object is a dictionary of live objects."""
        self.assertIs(dict, type(FileStorage._FileStorage__objects))


if __name__ == "__main__":
    unittest.main()        