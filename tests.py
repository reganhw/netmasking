from netmasking import *

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
    test_cidr_to_int()