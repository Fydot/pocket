#!/usr/bin/env python
# coding: utf8
import redis
import ujson


storage = None


class Storage(object):
    def __new__(self, *args, **kwargs):
        if '_inst' not in vars(self):
            self._inst = super(Storage, self).__new__(self, *args, **kwargs)
            self._redis = args[0]
        return self._inst

    def __init__(self, redis_conn):
        pass

    def set_cache(self, key, value, expire):
        self._redis.set(key, value)
        self._redis.expire(key, expire)

    def get_cache(self, key):
        return self._redis.get(key)


def config_storage(redis_conn=redis.StrictRedis("localhost", 6379)):
    global storage
    storage = Storage(redis_conn)


def idcache(app, namespace, ttl=-1):
    def _cache(func):
        def _wrap(id):
            if not storage:
                config_storage()
            print storage
            key = "%s:%s:%s" % (app, namespace, id)
            cache_obj = storage.get_cache(key)
            if cache_obj:
                return ujson.loads(cache_obj)
            result = func(id)
            if ttl == -1:
                storage.set_cache(key, ujson.dumps(result))
            else:
                storage.set_cache(key, ujson.dumps(result), ttl)
            return result
        return _wrap
    return _cache
