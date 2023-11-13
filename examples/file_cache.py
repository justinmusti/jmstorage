import concurrent.futures

from jmstorage import Cache

c = Cache(namespace="filelib", engine="disk", path="./test_dir")
c.set("test", "hello world")
print('TEST VALUE', c.get("test"))
c.delete("test")
c.truncate()


# Try threading to see if thread-lock is working.
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(c.set, "my_key", i): i for i in range(1, 1000)}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('Processed %s' % url)
