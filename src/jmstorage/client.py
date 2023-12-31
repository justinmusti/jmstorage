from jmstorage.constants import STORAGE_ENGINE_DISK, STORAGE_ENGINE_REDIS
from jmstorage.storage import DiskStorageManager, RedisStorageManager
from jmstorage.storage.base import BaseCacheStorageManager


class Cache(BaseCacheStorageManager):

    storage_engine_map = {
        STORAGE_ENGINE_DISK: DiskStorageManager,
        STORAGE_ENGINE_REDIS: RedisStorageManager
    }

    def __init__(self, namespace: str, engine: str = STORAGE_ENGINE_DISK, *args, **kwargs):

        # Check that engine is a supported integration
        if engine not in self.storage_engine_map:
            raise ValueError("Unsupported storage engine: %s. Supported values: %s" %
                             (engine, ", ".join(self.storage_engine_map.keys())))
        self.engine = self.storage_engine_map[engine](namespace, *args, **kwargs)

    def get(self, key):
        return self.engine.get(key)

    def set(self, key, value):
        return self.engine.set(key, value)

    def delete(self, key):
        return self.engine.delete(key)

    def pop(self, key):
        return self.engine.pop(key)

    def truncate(self):
        return self.engine.truncate()
