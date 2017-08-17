#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage

State = state.State
Base = base_model.Base
DBStorage = engine.db_storage.DBStorage
storage = storage

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ' Database engine '
        actual = db_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = ' returns a dictionary of all objects '
        actual = DBStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ' adds objects to current database session '
        actual = DBStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = ' commits all changes of current database session '
        actual = DBStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ' creates all tables in database & current session from engine '
        actual = DBStorage.reload.__doc__
        self.assertEqual(expected, actual)

    def test_doc_delete(self):
        """... documentation for delete function"""
        expected = ' deletes obj from current database session if not None '
        actual = DBStorage.delete.__doc__
        self.assertEqual(expected, actual)

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestBaseFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('......... Testing DBStorage .;.......')
        print('........ For DBStorage Class ........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new storage object for testing"""
        DBStorage.session.close()
        self.storage = DBStorage()
        self.bm_obj = Base()

    def test_instantiation(self):
        """... checks proper DBStorage instantiation"""
        self.assertIsInstance(self.storage, DBStorage)

    def test_new(self):
        """ test if new instance is created """
        s = State(name="California")
        s.save()
        self.reload()
        self.assertEqual(s.save(), self.reload())

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        bm_id = self.bm_obj.id
        all_obj = storage.all()
        actual = 0
        for k in all_obj.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        s = State(name="California")

        # self.bm_obj.save()
        # bm_id = self.bm_obj.id
        # actual = 0
        # new_storage = FileStorage()
        # new_storage.reload()
        # all_obj = new_storage.all()
        # for k in all_obj.keys():
        #     if bm_id in k:
        #         actual = 1
        # self.assertTrue(1 == actual)

    def test_save_reload_class(self):
        """... checks proper usage of class attribute in file storage"""

        # self.bm_obj.save()
        # bm_id = self.bm_obj.id
        # actual = 0
        # new_storage = FileStorage()
        # new_storage.reload()
        # all_obj = new_storage.all()
        # for k, v in all_obj.items():
        #     if bm_id in k:
        #         if type(v).__name__ == 'BaseModel':
        #             actual = 1
        # self.assertTrue(1 == actual)

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('.......... User  Class ..........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()
        self.bm_obj = BaseModel()

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        u_id = self.user.id
        all_obj = storage.all()
        actual = 0
        for k in all_obj.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        # self.user.save()
        # u_id = self.user.id
        # actual = 0
        # with open(F, mode='r', encoding='utf-8') as f_obj:
        #     storage_dict = json.load(f_obj)
        # for k in storage_dict.keys():
        #     if u_id in k:
        #         actual = 1
        # self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""

        # self.bm_obj.save()
        # u_id = self.bm_obj.id
        # actual = 0
        # new_storage = FileStorage()
        # new_storage.reload()
        # all_obj = new_storage.all()
        # for k in all_obj.keys():
        #     if u_id in k:
        #         actual = 1
        # self.assertTrue(1 == actual)


if __name__ == '__main__':
    unittest.main