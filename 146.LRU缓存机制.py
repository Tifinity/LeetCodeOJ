from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        self.hash = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.hash:
            return - 1
        self.hash.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self.hash:
            self.hash.move_to_end(key)
        self.hash[key] = value
        if len(self.hash) > self.capacity:
            self.popitem(last = False)