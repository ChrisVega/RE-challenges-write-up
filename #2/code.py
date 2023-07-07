def main(value):
    value = ((value & 0xFF000000) >> 24) | ((value & 0x00FF0000) >> 8) | ((value & 0x0000FF00) << 8) | ((value & 0x000000FF) << 24) #bswap
    print("{0:b}".format(value, '016b').zfill(32))
    value = ((value & 0xF0F0F0F) << 4) | ((value & 0xF0F0F0F0) >> 4)
    print("{0:b}".format(value, '016b').zfill(32))
    value = ((value & 0x33333333) << 2) | ((value & 0xCCCCCCCC) >> 2)
    print("{0:b}".format(value, '016b').zfill(32))
    valuea = ((value) & 0x55555555)
    valueb =((value & 0xAAAAAAAA) >> 1)
    valuea = valuea + valuea
    value = valuea | valueb
    print("{0:b}".format(value, '016b').zfill(32))
    return value
    
if __name__ == '__main__':
    testval = 11254
    print("{0:b}".format(testval, '016b').zfill(32))
    print("{0:b}".format(main(testval), '016b').zfill(32))
    