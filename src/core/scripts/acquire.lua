local key = KEYS[1]

local token = ARGV[1]
local now = tonumber(ARGV[2])
local timeout = tonumber(ARGV[3])
local limit = tonumber(ARGV[4])

redis.call(
    "ZREMRANGEBYSCORE",
    key,
    "-inf",
    now - timeout
)

local current = redis.call(
    "ZCARD",
    key
)

if current >= limit then
    return 0
end

redis.call(
    "ZADD",
    key,
    now,
    token
)

return 1