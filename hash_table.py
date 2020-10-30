class HashTable:
    def __init__(self, max: int = 100):
        self.max = max
        self.array = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self,key):
        h = self.get_hash(key)
        if self.array[h] is None:
            self.array[h] = []
            self.array[h].append(key)
        else:
            for keyAlreadyThere in self.array[h]:
                if keyAlreadyThere == key:
                    break
            else:
                self.array[h].append(key)

        return h

    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.array[h] is None:
            return None
        else:
            for k in self.array[h]:
                if k == key:
                    return h
            return None

    def __str__(self):
        return str(self.array)
