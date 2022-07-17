import ctypes
from unittest import result


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
    for i in range(0, LIMIT):
        # save all data related in each hex str
        num_bytes    = read[i][1:3]
        hex_addr = int(read[i][3:7], 16)
        record_type  = read[i][7:9]
        checksum     = read[i][-2:]
        _bytes       = read[i][9:-2]

        while n < len(_bytes): 
            # add 0xff when new addr comes in
            while current_addr < hex_addr:
                byte_to_save = '0xff'    #stuff
                byte_list.append(byte_to_save)
                current_addr += 2
            
            byte_to_save = '0x' + str(_bytes[n:n+2])
            byte_list.append(byte_to_save)
            n += 2
        n = 0
        current_addr = 0
        # print(f"addr: {hex_addr} - bytes {_bytes}")
    
    # print(byte_list)

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