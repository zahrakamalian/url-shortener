from contextvars import ContextVar
from pathlib import Path
import time
import uuid

from redis import Redis


class SemaphoreLimitExceeded(Exception):
    pass


class RedisSemaphore:
    def __init__(self, redis: Redis, key: str, limit: int, timeout: int,):
        self.redis = redis
        self.key = key
        self.limit = limit
        self.timeout = timeout

        self._token = ContextVar("redis_semaphore_token")

        script = (Path(__file__).parent.joinpath(
            "scripts", "acquire.lua").read_text())
        self.acquire_script = self.redis.register_script(script)

    def acquire(self) -> bool:
        token = str(uuid.uuid4())
        success = self.acquire_script(
            keys=[self.key],
            args=[
                token,
                int(time.time()),
                self.timeout,
                self.limit
            ]
        )

        if success == 0:
            return False
        self._token.set(token)
        return True

    def release(self) -> None:
        token = self._token.get(None)
        if token is None:
            return
        self.redis.zrem(
            self.key,
            token,
        )

    def __enter__(self):
        if not self.acquire():
            raise SemaphoreLimitExceeded()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()
