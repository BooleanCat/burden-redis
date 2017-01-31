import time
import tempfile
import subprocess

import redis
from radish import before, after


class RedisServer:
    def __init__(self):
        self.dir = tempfile.TemporaryDirectory()
        self.server = None

    def start(self):
        self.server = subprocess.Popen(
            ['redis-server', '--dir', self.dir.name],
            stdout=subprocess.DEVNULL
        )
        self.wait_for_redis_up()

    def stop(self):
        self.server.kill()
        self.server.wait()

    def wait_for_redis_up(self):
        for i in range(100):
            if self.redis_is_pingable():
                return
            time.sleep(0.05)
        raise TimeoutError('timed out waiting for redis to start')

    def redis_is_pingable(self):
        client = redis.StrictRedis()
        try:
            return client.ping()
        except redis.ConnectionError:
            return False


REDIS_SERVER = None


@before.all
def start_redis_server(features, marker):
    global REDIS_SERVER
    REDIS_SERVER = RedisServer()
    REDIS_SERVER.start()


@after.all
def stop_redis_server(features, marker):
    global REDIS_SERVER
    REDIS_SERVER.stop()
