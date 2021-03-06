
from simple_db import SimpleDB

class TransactionManager:
    transactions = []
    active_tx = []
    cur_tx_index = 0
    default_db = SimpleDB()
    def handle_set(self, key, val):
        if self.cur_tx_index > 0:
            cmd = []
            cur_val = self.default_db.get(key)
            if cur_val is None:
                cmd = ["UNSET", key]
            else:
                cmd = ["SET", key, cur_val]
            self.active_tx.append(cmd)
        
        self.default_db.set(key, val)


    def handle_get(self, key):
        return self.default_db.get(key)

    def handle_num_equal_to(self, val):
        return self.default_db.num_equal_to(val)

    def handle_unset(self, key):
        if self.cur_tx_index > 0:
            cur_val = self.default_db.get(key)
            if cur_val:
                cmd = ["SET", key, cur_val]
                self.active_tx.append(cmd)
        
        self.default_db.unset(key)
    
    def handle_begin(self):
        if self.cur_tx_index > 0:
            self.transactions.append(self.active_tx)
        self.active_tx = []
        self.cur_tx_index += 1
        

    def handle_rollback(self):
        if self.cur_tx_index is 0:
            return "NO TRANSACTION"

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
        return None

    def handle_commit(self):
        self.transactions[:] = []
        self.active_tx[:] = []
        self.cur_tx_index = 0
        return
