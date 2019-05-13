from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

host = os.environ.get('DBHOST')
redis = Redis(host=host, port=6379, charset="utf-8", decode_responses=True)


@app.route('/')
def increase_entry():
    redis.incr('hits')
    return 'Hello! You have seen this page {0} times'.format(redis.get('hits'))


@app.route('/', methods=['DELETE'])
def decrease_entry():
    redis.decr('hits')
    return 'Hello! You have seen this page {0} times'.format(redis.get('hits'))


@app.route('/', methods=['POST'])
def post_entry():
    redis.delete('hits')
    return 'Flushed'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
