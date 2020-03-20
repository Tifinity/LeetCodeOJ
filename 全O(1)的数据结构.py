
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.help = OrderedDict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in data:
            data[key] += 1
        else:
            data.updata({key:1})

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in data:
            pass
        else:
            if data[key] == 1:
                del data[key]
            else:
                data[key] -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        


# Your AllOne object will be instantiated and called as such:
obj = AllOne()

obj.inc(9)
obj.dec(23)
obj.inc(1)
obj.inc(9)
obj.dec(23)
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()