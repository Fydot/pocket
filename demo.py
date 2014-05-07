import pocket.cache
import time
import sys


@pocket.cache.idcache("test", "member", ttl=5)
def get_member(id):
    time.sleep(1)
    return id


print get_member(sys.argv[1])
print get_member(sys.argv[1])
print get_member(sys.argv[1])
print get_member(sys.argv[1])
print get_member(sys.argv[1])
