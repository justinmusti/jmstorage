import dill


# Define an interface that enforces structure
class BaseCacheStorageManager:
    """
    This is more of an interface than anything
    Enforce unison of methods across all types of cache
    """

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def pop(self, key):
        raise NotImplementedError

    def truncate(self):
        raise NotImplementedError

    def serialize(self, data):
        return dill.dumps(data)

    def deserialize(self, data):
        return dill.loads(data)
