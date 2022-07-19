# import ctypes
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
    
    for arr in read:
        num_bytes            = arr[1:3]
        current_addr_hex     = arr[3:7]
        current_addr         = int(arr[3:7], 16)
        record_type          = arr[7:9]
        checksum             = arr[-2:]
        _bytes               = arr[9:-2]
        # print(f"num_bytes = {num_bytes}  - hex_addr = {hex_addr} - record_type = {record_type} - checksum = {checksum} - _bytes = {_bytes}")
        # print(f"{_bytes} - {current_addr_hex}")

        i = 0
        while i < len(_bytes):                 # loop through all bytes in the array

            if _bytes[i] == ':':               # if the byte is a colon
                i += 1                         # skip the colon
                continue                       # skip it
            
            # packet every 2 characters
            byte_list.append(_bytes[i:i+2])    # add the byte to the list
            i += 2
        i = 0
    print(byte_list)


    
    # # add each element as hex int inside another array
    # result_list = []
    # for item in byte_list:
    #     an_integer = int(item, 16)
    #     result_list.append(an_integer)
    
    # print(len(result_list))
    # seq = ctypes.c_int * len(result_list)
    # arr = seq(*result_list)
    # print("PIC8 HEX: { ", end='')
    # for index, x in enumerate(arr):
    #     # if last element, print a new line
    #     if index == len(arr)- 1:
    #         print(hex(x), end=" };\n")
    #     else:
    #         print(hex(x), end=', ')

if __name__ == '__main__':
    main("HEV_18F13K50_v8.X.production.hex")