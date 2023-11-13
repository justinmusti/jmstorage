import shutil
from datetime import datetime
from unittest import TestCase

from jmstorage import Cache


class DiskBaseStorageTestCase(TestCase):

    def setUp(self):
        self.test_path = "./test_tmp"

    def test_cache_init(self):

        # Must require `namespace` param
        with self.assertRaises(TypeError):
            Cache()

        # When `engine` is disk, require, `path`
        with self.assertRaises(TypeError):
            Cache(namespace="hello", engine="disk")

    def test_setting_values(self):
        c = Cache(namespace="test_namespace", path=self.test_path)
        # Test string storage
        val = "Test Value"
        key = "test_key"
        c.set(key, val)
        self.assertEqual(c.get(key), val)

        # Test int storage
        val = 1
        key = "test_key"
        c.set(key, val)
        self.assertEqual(c.get(key), val)

        # Test dict with dates storage
        val = dict(date=datetime.now())
        key = "test_key"
        c.set(key, val)
        self.assertEqual(c.get(key), val)

        # Test class object(local class object) storage
        class A:
            date = datetime.now()
            hello = "world"
        val = A()
        key = "test_key"
        c.set(key, val)
        self.assertEqual(c.get(key).date, val.date)

        # Test type object storage
        obj = type("TestClassObject", (), dict(date=datetime.now(), hello="world"))
        val = obj()
        key = "test_key"
        c.set(key, val)
        self.assertEqual(c.get(key).date, val.date)

    def test_pop_values(self):
        """
        {cache} object must provide value for the key with `pop` method and remove the value at the same time.
        querying for the key after must return None
        """
        obj = type("TestClassObject", (), dict(date=datetime.now(), hello="world"))
        val = obj()
        key = "test_key"
        c = Cache(namespace="test_namespace", path=self.test_path)
        c.set(key, val)
        popped_val = c.pop(key)
        self.assertEqual(popped_val.date, val.date)
        self.assertEqual(popped_val.hello, val.hello)
        self.assertEqual(c.get(key), None)

    def test_delete_value(self):
        """
        Remove the key:value from the storage.
        """
        obj = type("TestClassObject", (), dict(date=datetime.now(), hello="world"))
        val = obj()
        key = "test_key"
        c = Cache(namespace="test_namespace", path=self.test_path)
        c.set(key, val)
        self.assertEqual(c.get(key).date, val.date)
        c.delete(key)
        self.assertEqual(c.get(key), None)

    def test_truncate_method(self):
        """
        This will remove everything from the storage under the namespace.
        """

        obj = type("TestClassObject", (), dict(date=datetime.now(), hello="world"))
        o_key, o_val = "o_key",  obj()
        s_key, s_val = "s_key", "s_value"
        i_key, i_val = 11, 9999
        c = Cache(namespace="test_namespace", engine="disk", path=self.test_path)
        c.set(o_key, o_val)
        c.set(s_key, s_val)
        c.set(i_key, i_val)
        c.truncate()
        self.assertEqual(c.get(o_key), None)
        self.assertEqual(c.get(s_key), None)
        self.assertEqual(c.get(i_key), None)

    def tearDown(self):
        # Remove Cache storage path after tests are done.
        shutil.rmtree(self.test_path, ignore_errors=True)
