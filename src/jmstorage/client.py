from jmstorage.storage import CacheStorage


class CacheManager:

    def __init__(self, namespace, storage="disk", *args, **kwargs):
        self.storage = CacheStorage(namespace=namespace, engine=storage, *args, **kwargs)

    def get(self, key):
        return self.storage.get(key)

    def set(self, key, value):
        return self.storage.set(key, value)

    def delete(self, key):
        return self.storage.delete(key=key)
