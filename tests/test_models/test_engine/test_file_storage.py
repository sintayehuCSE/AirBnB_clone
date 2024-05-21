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
    
    def test_FileStorage_all(self):
        """Check if all method is defined for the Storage class."""
        self.assertIsNotNone(FileStorage.all)
    
    def Test_FileStorage_new(self):
        """Check for presence of new() method in FileStorage class."""
        self.assertIsNotNone(FileStorage.new)

    def Test_FileStorage_save(self):
        """Check for presence of save() method in FileStorage class."""
        self.assertIsNotNone(FileStorage.save)

    def Test_FileStorage_reload(self):
        """Check for presence of reload() method in FileStorage class."""
        self.assertIsNotNone(FileStorage.reload)

    def test_doc(self):
        """Check if sTorage function are documented or not."""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_type__file_path(self):
        """check for file_path type as only string."""
        self.assertIs(str, type(FileStorage._FileStorage__file_path))

    def test_type__objects(self):
        """Test if private __object is a dictionary of live objects."""
        self.assertIs(dict, type(FileStorage._FileStorage__objects))


if __name__ == "__main__":
    unittest.main()        