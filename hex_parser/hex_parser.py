

import ctypes


def main(filename):
    # load the hexfile you have 
    LIMIT = 5
    f = open(filename, "r")
    read = f.read().split("\n")
    if read[-1] == '':
        read = read[:-1]
    
    # after get the bytes in list, let's append the bytes 
    # after the 9th byte
    bytes_not_converted = []
    cnt = 0
    enough = 0
    for i in read:
        # Iterate over the string
        if enough == LIMIT:
            break
        cnt = 0
        for element in i:
            if cnt == 9:
                bytes_not_converted.append(i[cnt:-2])
                break
            else:
                cnt += 1
        enough += 1

    # print(bytes_not_converted)
    byte_list = []
    cnt = 0   
    n = 0
    for i, item in enumerate(bytes_not_converted):
        # print(i, item)
        while n < len(item):
            byte_to_save = '0x' + str(item[n:n+2])
            byte_list.append(byte_to_save)
            # print(byte_to_save)
            n += 2
        n = 0
        # print("")
    
    result_list = []
    for item in byte_list:
        an_integer = int(item, 16)
        result_list.append(an_integer)

    # seq = ctypes.c_int * len(result_list)
    # arr = seq(*result_list)
    # print("{ ", end='')
    # for i in arr:
    #     print(hex(i), end=', ')
    # print("}")
    # print(len(arr))

if __name__ == '__main__':
    # run main
    main("HEV_18F13K50_v8.X.production.hex")
    # list_bytes = [0x9c, 0xce, 0xef, 0xf0, 0x0, 0xf, 0xf0, 0x0, 0x48, 0x88, 0x82, 0x2f, 0xfa, 0xac, 0xcf, 0xf0, 0xe, 0xef, 0xf0, 0xf, 0xfb, 0xbc, 0xcf, 0xf0, 0xf, 0xff, 0xf0, 0xd, 0xd9, 0x9c, 0xcf, 0xf1, 0x10, 0xf, 0xf0, 0xd, 0xda, 0xac, 0xcf, 0xf, 0x11, 0x1f, 0xf0, 0xf, 0xf3, 0x3c, 0xcf, 0xf1, 0x12, 0x2f, 0xf0, 0xf, 0xf4, 0x4c, 0xcf, 0xf1, 0x13, 0x3f, 0xf0, 0xf, 0xf6, 0x6c, 0xcf, 0xf1]
    # print(list_bytes)