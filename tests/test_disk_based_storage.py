from unittest import TestCase

from jmstorage import Cache


class DiskBaseStorageTestCase(TestCase):

    def test_cache_init(self):

        # Must require `namespace` param
        with self.assertRaises(TypeError):
            Cache()
