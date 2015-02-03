from collections import defaultdict

class SimpleDB:
    table = defaultdict(lambda :None)
    inverse_table = defaultdict(set)
    
    def set(self, key, value):
        if key is None or value is None:
            return

        if key in self.table:
            previous_val = self.table[key]
            self.inverse_table[previous_val].remove(key)
            if len(self.inverse_table[previous_val]) is 0:
                del self.inverse_table[previous_val]
         
        self.table[key] = value
        self.inverse_table[value].add(key)

    def get(self, key):
     #   if key not in self.table:
      #      return "NULL"
        return self.table[key]


    def unset(self, key):
        value = self.table[key]
        if value is not None:
            self.inverse_table[value].remove(key)
            if len(self.inverse_table[value]) is 0:
                del self.inverse_table[value]

        
        del self.table[key]
        return

    def num_equal_to(self, val):
        return len(self.inverse_table[val])
            
    def get_keys(self):
        return self.table.keys()
   
