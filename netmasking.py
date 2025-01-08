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

def netmasking(ip_s, netmask_s, cidr = False):
    ip = ip_to_int(ip_s)
    if cidr:
        netmask = (1<<netmask_s) -1
        netmask = netmask << (32-netmask_s)
    else: 
        netmask = ip_to_int(netmask_s)
    network_addr = ip & netmask
    netmask_neg = netmask^((1<<32)-1)
    broadcast_addr = network_addr + netmask_neg
    d = {'네트워크 주소': int_to_ip(network_addr), '브로드캐스트 주소': int_to_ip(broadcast_addr), '호스트 수': netmask_neg -2}
    return d
