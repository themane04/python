import re


def is_localhost_address(url):
    pattern = r'^.*(80[0-7]\d)'
    return bool(re.search(pattern, url))


# Test the function
print(is_localhost_address("http://127.0.0.1:8000"))
print(is_localhost_address("http://127.0.0.1:8080"))
print(is_localhost_address("http://127.0.0.1:8010"))
print(is_localhost_address("http://127.0.0.1:8090"))
print(is_localhost_address("http://127.0.0.1:8079"))