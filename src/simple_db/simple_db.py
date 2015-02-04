from collections import defaultdict

class SimpleDB:
    table = defaultdict(lambda :None)
    inverse_table = defaultdict(set)
    
    def set(self, key, value):
        if not key or not value:
            return
        previous_val = self.table[key]
        if previous_val:
            self.inverse_table[previous_val].remove(key)
            if not self.inverse_table[previous_val]:
                del self.inverse_table[previous_val]
         
        self.table[key] = value
        self.inverse_table[value].add(key)

    def get(self, key):
        return self.table[key]


    def unset(self, key):
        value = self.table[key]
        if value:
            self.inverse_table[value].remove(key)
            if not self.inverse_table[value]:
                del self.inverse_table[value]
            del self.table[key]
        return

    def num_equal_to(self, val):
        return len(self.inverse_table[val])
            
    def get_keys(self):
        return self.table.keys()
   
