#!/usr/bin/python
from simple_db import tx_manager

while True:
    input_cmd = raw_input().strip().split()

    len_input = len(input_cmd)

    if len_input is 1:
        if input_cmd[0] ==  "END":
            break
        if input_cmd[0] == "BEGIN":
            tx_manager.handle_begin()
        elif input_cmd[0] == "COMMIT":
            tx_manager.handle_commit()
        elif input_cmd[0] == "ROLLBACK":
            ret = tx_manager.handle_rollback()
            if ret:
                print ret
        else:
            print "INVALID CMD"

    elif len_input is 2:
        if input_cmd[0] == "NUMEQUALTO":
            print  tx_manager.handle_num_equal_to(input_cmd[1])        
        elif input_cmd[0] == "GET":
            val = tx_manager.handle_get(input_cmd[1])
            if val is None:
                print "NULL"
            else:
                print val
        elif input_cmd[0] == "UNSET":
            tx_manager.handle_unset(input_cmd[1])
        else:
            print "INVALID CMD"
    elif len_input is 3 and input_cmd[0] == "SET":
        tx_manager.handle_set(input_cmd[1], input_cmd[2])
    else:
        print "INVALID CMD"
        
