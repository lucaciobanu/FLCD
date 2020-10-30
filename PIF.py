class PIF:
    def __init__(self):
        self.data = []

    def __setitem__(self,key,position):
        self.data.append((key,position))

    def __str__(self):
        return "\n".join(map(str,self.data))
