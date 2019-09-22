import logging
from _md5 import md5
from argparse import Namespace
from functools import wraps

from flask import current_app, request
from redis import exceptions as redis_exceptions

log = logging.getLogger(__name__)

redis_connection = Namespace(get=None, set=None)


def call_redis(cmd, *args, **kwargs):
    try:
        return cmd(*args, **kwargs)
    except (redis_exceptions.ConnectionError, redis_exceptions.TimeoutError):
        log.error(
            'connection to redis server failed: '
            'host=%s port=%s' % (
                current_app.config["REDIS_HOST"],
                current_app.config["REDIS_PORT"]))
        return None


def build_key_from_request(body, *args, **kwargs):
    body_part = ":".join([f"{k}|{v}" for k, v in body.items()])
    args_part = ":".join([str(i) for i in args])
    result = ":".join([args_part, body_part])
    return md5(result.encode('utf-8')).hexdigest()


def cache(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        request_body = request.get_json(force=True)
        cache_key = build_key_from_request(request_body, *args)
        from_cache = call_redis(redis_connection.get, cache_key)

        if from_cache is None:
            result = fn(*args, **kwargs)
            log.debug('cache get MISS setting key %s to value %s', cache_key, result)
            call_redis(redis_connection.set, cache_key, result.data)
        else:
            log.debug('cache get HIT got value %s from key %s', from_cache, cache_key)
            result = from_cache
        return result
    return wrapper
