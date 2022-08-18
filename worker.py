import os

import redis
from rq import Worker, Queue, Connection
from worker import conn
from . import policy_functions as pf

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

q = Queue(connection=conn)

result = q.enqueue(count_words_at_url, 'http://heroku.com')

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()