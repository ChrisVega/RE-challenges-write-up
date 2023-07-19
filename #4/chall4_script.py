def main(value):
    value = value - ((value >> 1) & 0x55555555)
    value = (value & 0x33333333) + ((value >> 2) & 0x33333333)
    value = ((value >> 4) + value)
    value = ((value & 0xf0f0f0f) * 0x1010101)
    return (value >> 0x18)
    
if __name__ == '__main__':
    testval = 0xFFFFFFFF
    print("{0:b}".format(testval, '016b').zfill(32))
    print("{0:b}".format(main(testval), '016b').zfill(32))