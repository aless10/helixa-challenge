from redis import StrictRedis


def setup_redis_connection(_app):
    global redis_connection

    redis_connection = StrictRedis(
        host=_app.config['REDIS_HOST'],
        port=_app.config['REDIS_PORT'],
        db=0
    )
