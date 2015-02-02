
from simple_db import default_db

class TransactionManager:
    transactions = []
    active_tx = []
    cur_tx_index = 0
    
    def handle_set(self, key, val):
        if self.cur_tx_index > 0:
            cmd = []
            cur_val = default_db.get(key)
            if cur_val is "NULL":
                cmd = ["UNSET", key]
            else:
                cmd = ["SET", key, cur_val]
            self.active_tx.append(cmd)
        
  #      print key,val
        default_db.set(key, val)
   #     print default_db.get(key)


    def handle_get(self, key):
        return default_db.get(key)

    def handle_num_equal_to(self, val):
        return default_db.num_equal_to(val)

    def handle_unset(self, key):
        default_db.unset(key)
    
    def handle_begin(self):
        if len(self.active_tx) is not 0:
            self.transactions.append(self.active_tx)
        self.active_tx = []
        self.cur_tx_index += 1
        

    def handle_rollback(self):
#        print self.transactions
 #       print self.active_tx
        if self.cur_tx_index is 0:
            print "NO TRANSACTION"
            return

        for cmd in reversed(self.active_tx):
            if cmd[0] == "SET":
                self.handle_set(cmd[1], cmd[2])
            elif cmd[0] == "UNSET":
                self.handle_unset(cmd[1])
        
        self.active_tx = []
        self.cur_tx_index -= 1
        if self.cur_tx_index > 0:
            self.active_tx = self.transactions[-1]
            self.transactions.pop(-1)
    

    def handle_commit(self):
        if self.cur_tx_index is 0:
            return

        self.cur_tx_index -= 1
        self.active_tx = []
        if self.cur_tx_index > 0:
            self.active_tx = self.transactions[-1]
            self.transactions.pop(-1)
    


