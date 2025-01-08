import random
from netmasking import *

def test_ip_to_int():
    for i in range (10):
        octets_int = [random.randint(0,255) for j in range(4)]
        ip ='.'.join([str(o) for o in octets_int])

        ip_int = ip_to_int(ip)
        ip_int_b = format(ip_int, '032b')

        for k in range(4):
            ob = format(octets_int[k], '08b')
            byte_in_ip = ip_int_b[k*8: k*8+8]
            if not (ob==byte_in_ip):
                print('octets_int: ',octets_int)
                print('ip_int: ',ip_int)
                print('k: ', k)
                print('ob: ', ob)
                print('byte_in_ip: ',byte_in_ip )

def test_cidr_to_int():
    for i in range (1,32):
        n = cidr_to_int(i)
        nb = bin(n)[2:]
        assert(len(nb)==32)
        for j in range(i):
            assert(nb[j]=="1")
        for j in range (i, 32):
            assert(nb[j]=="0")

if __name__ =="__main__":
    test_ip_to_int()