

import ctypes


def main(filename):
    # load the hexfile you have 
    LIMIT = 5
    f = open(filename, "r")
    read = f.read().split("\n")
    if read[-1] == '':
        read = read[:-1]

    '''
        read = [':040000009CEF00F081', 
        ':100008004882FACF0EF0FBCF0FF0D9CF10F0DACF3D',
        ...]
    '''
    # 
    for i in range(0, 2):
        num_bytes   = read[i][1:3]
        addr        = read[i][3:7]
        record_type = read[i][7:9]
        _bytes      = read[i][10:-2]
        checksum    = read[i][-2:]
        print(_bytes)
    
    # print(read)

if __name__ == '__main__':
    # run main
    main("HEV_18F13K50_v8.X.production.hex")