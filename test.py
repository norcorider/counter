import counter
import unittest
from redis import Redis
import os


host = os.environ.get('localhost')


class CounterTestCase(unittest.TestCase):
    def setUp(self):
        redis = Redis(host=host, port=6379)
        redis.delete('hits')
        self.app = counter.app.test_client()

    def test_init_counter(self):
        rv = self.app.get('/')
        assert b"Hello! You have seen this page 1 times" in rv.data

    def test_reset_counter(self):
        rv = self.app.post('/')
        assert b"Flushed" in rv.data

    def test_decrease_counter(self):
        rv = self.app.delete('/')
        assert b"Hello! You have seen this page -1 times" in rv.data


if __name__ == '__main__':
    unittest.main()

