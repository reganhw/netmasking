def ip_to_int(ip):
    octets = ip.split(".")
    
    zeros = 24
    ip_int = 0
    for o in octets:
        ip_int += int(o)<<zeros
        zeros -=8
        
    return ip_int

def int_to_ip(n):
    octets = []
    for i in range(4):
        octet = str(n&255)
        octets.insert(0,octet)
        n = n>>8
    return '.'.join(octets)

def cidr_to_int(cidr):
    n = (1<<cidr)-1
    n = n<<(32-cidr)
    return n

for i in range (1,32):
    n = cidr_to_int(i)
    nb = bin(n)[2:]
    assert(len(nb)==32)
    for j in range(i):
        assert(nb[j]=="1")
    for j in range (i, 32):
        assert(nb[j]=="0")