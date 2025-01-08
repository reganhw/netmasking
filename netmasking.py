def ip_to_int(ip_s):
    '''
    Input: A valid ip address string.
    Output: The ip converted to an integer.
    '''
    octets = ip_s.split(".")         
    zeros = 24                      
    ip= 0                     
    for o in octets:
        ip += int(o)<<zeros     
        zeros -=8
        
    return ip

def int_to_ip(n):
    '''
    Input: An integer n s.t. 0<=n<2^32
    Output: n written in IP form
    '''
    octets = []
    for i in range(4):
        octet = str(n&255)
        octets.insert(0,octet)
        n = n>>8
    return '.'.join(octets)

def cidr_to_int(cidr):
    '''
    Input: A netmask in cidr format.
    Output: The netmask converted to an integer
    '''
    cidr = int(cidr)
    n = (1<<cidr)-1
    n = n<<(32-cidr)
    return n

def netmasking(ip_s, netmask_s, cidr = False):
    '''
    Input: An ip address and a netmask, both strings with four octets
    OR
    An ip address with four octets (string), a netmask in CIDR form (string), and 'cidr=True'
    Output: {network address, broadcast address, number of hosts}
    '''
    ip = ip_to_int(ip_s)
    if cidr:
        netmask = cidr_to_int(netmask_s)
    else: 
        netmask = ip_to_int(netmask_s)
    network_id = ip & netmask
    netmask_neg = netmask^((1<<32)-1)
    broadcast_addr = network_id + netmask_neg
    d = {'네트워크 ID': int_to_ip(network_id), '브로드캐스트 주소': int_to_ip(broadcast_addr), '호스트 수': netmask_neg -1}
    return d