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
    
    index = 0
    end = False
    for arr in read:
        num_bytes            = arr[1:3]
        str_current_addr_hex     = arr[3:7]             # this is a string, which shows a hex value
        int_current_addr         = int(arr[3:7], 16)    # this is converted from hex to int
        record_type          = arr[7:9]
        checksum             = arr[-2:]
        _bytes               = arr[9:-2]

        # if num_bytes == '02' or num_bytes == '08' or num_bytes == '0E':
        #     continue

        # when I get to the end of the file, I want to set int_current_addr = 0x1DFF
        if arr == ":00000001FF" or ((num_bytes == '02' or num_bytes == '08' or num_bytes == '0E') and str_current_addr_hex == '0000'):        # is this item is the last in the 
            int_current_addr = 0x1E00

        # print(f"num_bytes = {num_bytes}  - hex_asddr = {hex_addr} - record_type = {record_type} - checksum = {checksum} - _bytes = {_bytes}")
        # print(f"{_bytes} - {str_current_addr_hex}")

        # if index < str_current_addr_hex, then do a bit stuffing. while 
        while index < int_current_addr:
            # bit stuffing 
            # print(f"bit stuffing at index = {index}")
            byte_list.insert(index, "0xFF")    # add the byte to the list
            index += 1
            if index >= 0x1DFF:
                #print("the program is larger than the memory size!")
                end = True
                break

        if not end: 
            n = 0
            while n < len(_bytes):                 # loop through all bytes in the array

                if _bytes[n] == ':':               # if the byte is a colon
                    n += 1                         # skip the colon
                    continue                       # skip it
                
                # packet every 2 characters
                one_byte = _bytes[n:n+2]

                # print(f"index = {index} -- n = {n} -- two bytes = {one_byte} -- addr = {str_current_addr_hex}")
                byte_list.insert(index, "0x" + one_byte)    # add the byte to the list
                index += 1                            # add 1 to index here

                #if index >= 0x1DFF, then stop, and send error message that the program is larger than the memory size!
                if index > 0x1DFF:
                    print("the program is larger than the memory size!")
                    break

                n += 2

            n = 0   # reset 

    # this executes after the array has been filled - for display only.
    row_counter = 0
    row_index = 0
    while row_counter < index/16:
        while(row_index < 16):
            print(byte_list[row_counter*16 + row_index], end=", ")
            row_index += 1

        
        
        # carriage return + newline
        print("", end=f"    // address = {str(hex((row_counter)*16)).zfill(3)}\r\n")
        row_counter += 1
        row_index = 0


    #print(byte_list)


    
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