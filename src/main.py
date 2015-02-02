#!/usr/bin/python
from transaction_mananger import TransactionManager
tx_manager = TransactionManager()

while True:
    input_cmd = raw_input().strip().split()

    #print input_cmd
    len_input = len(input_cmd)

    if len_input is 1:
        if input_cmd[0] ==  "END":
            break
        if input_cmd[0] == "BEGIN":
            tx_manager.handle_begin()
        elif input_cmd[0] == "COMMIT":
            tx_manager.handle_commit()
        elif input_cmd[0] == "ROLLBACK":
            tx_manager.handle_rollback()
        else:
            print "INVALID CMD"

    elif len_input is 2:
        if input_cmd[0] == "NUMEQUALTO":
            print  tx_manager.handle_num_equal_to(input_cmd[1])        
        elif input_cmd[0] == "GET":
            print tx_manager.handle_get(input_cmd[1])
        elif input_cmd[0] == "UNSET":
            tx_manager.handle_unset(input_cmd[1])
        else:
            print "INVALID CMD"
    elif len_input is 3 and input_cmd[0] == "SET":
        tx_manager.handle_set(input_cmd[1], input_cmd[2])
    else:
        print "INVALID CMD"
        
