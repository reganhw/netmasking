import random
from netmasking import *

def test_ip_to_int():
    for i in range (10000):
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
    for cidr in range (1,32):
        n = cidr_to_int(str(cidr))
        nb = bin(n)[2:]
        assert(len(nb)==32)
        for j in range(cidr):
            assert(nb[j]=="1")
        for j in range (cidr, 32):
            assert(nb[j]=="0")

TEST_VECTORS = [
    {'ip': "10.216.191.255", 'netmask': '21', 'cidr': True, '네트워크 ID': "10.216.184.0", '브로드캐스트 주소': "10.216.191.255", '호스트 수':2046 },
    {'ip': "0.0.0.0", 'netmask': '9', 'cidr': True, '네트워크 ID': "0.0.0.0", '브로드캐스트 주소': '0.127.255.255', '호스트 수':2**23-2 }
]

def test_netmasking():
    for d in TEST_VECTORS:
        d_res = netmasking(d['ip'], d['netmask'], d['cidr'])
        for k in d_res:
            assert(d_res[k] == d[k])
    
if __name__ =="__main__":
    test_netmasking()