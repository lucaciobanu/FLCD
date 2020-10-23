class HashTable:
    def __init__(self, max: int = 100):
        self.max = max
        self.array = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.array[h].append((key,value))

