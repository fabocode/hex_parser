import ctypes
from unittest import result

MAX_ARRAY_SIZE = 43

def main(filename):
    # load the hexfile you have 
    f = open(filename, "r")
    read = f.read().split("\n")
    if read[-1] == '':
        read = read[:-1]

    '''
        read = [':040000009CEF00F081', 
        ':100008004882FACF0EF0FBCF0FF0D9CF10F0DACF3D',
        ...]
    '''
    # parse all data from each array
    byte_list = []
    n = 0
    current_addr = 0
    LIMIT = 4
    past_addr = 0
    next_addr = 0
    for index, arr in enumerate(range(0, LIMIT)):
        if len(read[arr]) < 19:
            continue
        # save all data related in each hex str
        num_bytes    = read[arr][1:3]
        hex_addr     = int(read[arr][3:7], 16)
        record_type  = read[arr][7:9]
        checksum     = read[arr][-2:]
        _bytes       = read[arr][9:-2]

        print(f"arr: {read[arr]} - len: {len(read[arr])}")

        if len(read[arr]) == MAX_ARRAY_SIZE:
            while n < len(_bytes):                 
                byte_to_save = '0x' + str(_bytes[n:n+2])
                byte_list.append(byte_to_save)
                n += 2

            past_addr = hex_addr
            n = 0

        elif len(read[arr]) < MAX_ARRAY_SIZE:

            
            while n < len(_bytes):                 
                byte_to_save = '0x' + str(_bytes[n:n+2])
                byte_list.append(byte_to_save)
                n += 2
                current_addr += 1

            past_addr = hex_addr
            n = 0

            next_addr =  int(read[arr+1][3:7], 16)
            diff_between_addr = int((next_addr - hex_addr) / 2) # calculates the items (0xff) I need to add 
            print(f"next_addr {next_addr} - hex_addr {hex_addr} - diff {diff_between_addr}")
            
            for ff in range(0, diff_between_addr):
                byte_to_save = '0xff'
                byte_list.append(byte_to_save)



    # add each element as hex int inside another array
    result_list = []
    for item in byte_list:
        an_integer = int(item, 16)
        result_list.append(an_integer)
    
    print(len(result_list))
    seq = ctypes.c_int * len(result_list)
    arr = seq(*result_list)
    print("PIC8 HEX: { ", end='')
    for index, x in enumerate(arr):
        # if last element, print a new line
        if index == len(arr)- 1:
            print(hex(x), end=" };\n")
        else:
            print(hex(x), end=', ')

if __name__ == '__main__':
    main("HEV_18F13K50_v8.X.production.hex")