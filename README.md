# jmstorage


![Unit Tests](https://github.com/justinmusti/jmstorage/actions/workflows/run_tests.yml/badge.svg) [![JMStorage on PyPI](https://badge.fury.io/py/jmstorage.svg 'JM Storage PyPI')](https://pypi.org/project/jmstorage/)

Thread safe key:value storage with multiple back-end options.

## Install 

```shell
pip install jmstorage

```


## Storage Options

1. disk(local file system)  
   * Currently, this is the only supported option.
   * This is thread safe as the library acquires a thread lock during write operations.
2. Redis  
   * In Development, will update as it becomes available.
3. Sqlite
   * In Development, will update as it becomes available.
4. MySQL
   * In Development, will update as it becomes available.
5. PostgreSQL
    * In Development, will update as it becomes available.


## How to Use

```python
from jmstorage import Cache

c = Cache(namespace="namespace-value", path="./path_to_local_disk_file/")

# Set Value
c.set("my_key", "my_value")

# Read Value
my_val = c.get("my_key")
# > "my_value"

# Pop Value
my_val = c.pop("my_key")
# > "my_value"
c.get("my_key")
# > None


# Delete Value
c.delete("my_key")
c.get("my_key")
# > None

# Truncate Storage
c.truncate()
c.get("my_key")
# > None
```
