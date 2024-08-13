import requests

def for_test():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(for_test().json())

def test_me(response_mock):

    with response_mock('GET https://jsonplaceholder.typicode.com/todos/1 -> 404 :Not found ', bypass=False):

        result = for_test()

        assert result.status_code == 404
        assert result.content == b'Not found'