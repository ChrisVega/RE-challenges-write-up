import binascii

def crc16(data: bytes, poly=0x8408):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    
    return crc & 0xFFFF


def main():
    string = "Chris Vega!!!!!"
    orig =  "Dennis Yurichev"
    newuser = bytes(string, "utf-8")
    den = bytes(orig, "utf-8")
    c = bytearray(newuser)
    comp = hex(crc16(den))
    print(comp)
    c[len(c)-1] = 31
    c[len(c)-2] = 31
    c[len(c)-3] = 31
    c[len(c)-4] = 31
    c[len(c)-5] = 31
    for j in range(95):
        c[len(c)-5] = c[len(c)-5]+1
        for k in range(95):
            c[len(c)-4] = c[len(c)-4]+1
            for m in range(95):
                c[len(c)-3] = c[len(c)-3]+1
                for n in range(95):
                    c[len(c)-2] = c[len(c)-2]+1
                    for i in range(95):
                        c[len(c)-1] = c[len(c)-1]+1
                        print(bytes(c))
                        new = hex(crc16(bytes(c)))
                        if(comp == new):
                            print("done")
                            return c
                    c[len(c)-1] = 32
                c[len(c)-2] = 32
            c[len(c)-3] = 32
        c[len(c)-4] = 32
    c[len(c)-5] = 32

if __name__ == '__main__':
    print(main())
    