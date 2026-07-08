from src.core.redis import redis_client
from src.core.semaphore import RedisSemaphore

redirect_semaphore = RedisSemaphore(
    redis=redis_client,
    key="redirect_semaphore",
    limit=100,
    timeout=60,
)
