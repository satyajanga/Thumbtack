
class SimpleDB:
    table = {}
    inverse_table = {}
    
    def set(self, key, value):
        if key is None or value is None:
            return

        if key in self.table:
            previous_val = self.table[key]
            previous_keys = self.inverse_table[previous_val]
            new_keys = [x for x in previous_keys if x is not key]
            if len(new_keys) is not 0:
                self.inverse_table[previous_val] = new_keys
            else:
                del self.inverse_table[previous_val]
         
        self.table[key] = value
        
        if value in self.inverse_table:
            self.inverse_table[value].append(key)
        else:
            self.inverse_table[value] = [key]

    def get(self, key):
        if key is None:
            return "NULL"
        if key in self.table:
            return self.table[key]

        return "NULL"

    def unset(self, key):
        if key is None:
            return
        if key in  self.table:
            value = self.table[key]
            previous_keys = self.inverse_table[value]
            new_keys = [x for x in previous_keys if x is not key]
            if len(new_keys) is not 0:
                self.inverse_table[value] = new_keys
            else:
                del self.inverse_table[value]
            del self.table[key]

        return 

    def num_equal_to(self, val):
        if val is not None and val in self.inverse_table:
            return len(self.inverse_table[val])
        return 0
            
    def get_keys(self):
        return self.table.keys()
   
