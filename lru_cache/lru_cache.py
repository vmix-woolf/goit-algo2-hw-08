from collections import OrderedDict


class LRUCache:
    """
    Реалізація LRU-кешу з фіксованою місткістю.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        # Переміщаємо ключ у кінець як нещодавно використаний
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        # Видаляємо найстаріший елемент при перевищенні місткості
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
