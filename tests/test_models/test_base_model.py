#!/usr/bin/python3
"""This a unittest module for testing the BaseModel class.
   The number in the test_NO_method indicate the task each method is testing
"""
import unittest
import uuid
import time
import re
import os
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class will test the BaseModel class against various
       cases
    """
    def test_3_instatiation(self):
        """Tests instantiation of BaseModel class."""
        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))
         
    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "BaseModel.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_datetime_created(self):
        """Tests if updated_at and created_at time are current at creation."""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_unique_id(self):
        """Tests for creation of unique id for each instance."""
        id_list = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(id_list)), len(id_list))

    def test_3_save(self):
        """Tests the public instance method save()."""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_str(self):
        """Tests for __str__ magic method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_3_to_dict(self):
        """Tests the public instance method to_dict()."""
        b = BaseModel()
        b.name = "Sintayehu Mulugeta Kebede"
        b.age = 27
        d = b.to_dict()
        self.assertEqual(d['id'], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)
    
    def test_3_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "BaseModel.to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)
    
    def test_3_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "BaseModel.to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

if __name__ == "__main__":
    unittest.main()
