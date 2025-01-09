def ip_to_int(ip_s):
    '''
    Input: IP 문자열.
    Output: IP에 해당하는 정수.
    '''
    octets = ip_s.split(".")         # 옥텟들을 나누어 리스트에 저장
    zeros = 24                       # 붙일 0의 수
    ip= 0                            
    for o in octets:                 # 옥텟마다...
        ip += int(o)<<zeros          # 정수로 바꾼 뒤 0을 붙인다.
        zeros -=8                    # 0의 수가 24, 16, 8, 0으로 감소한다.        
    return ip

def int_to_ip(n):
    '''
    Input: 0<=n<2^32을 충족하는 정수
    Output: n을 IP로 바꾼 것
    '''
    octets = []
    for i in range(4):               
        octet = str(n&255)           # n의 마지막 8비트를 문자열로 저장.
        octets.insert(0,octet)       # 옥텟 리스트의 가장 앞에 넣는다.
        n = n>>8                     # n의 마지막 8비트를 탈락시킴.
    return '.'.join(octets)          # 옥텟 리스트를 IP 형태로 만든다.

def cidr_to_int(cidr):
    '''
    Input: CIDR 형태의 넷마스크
    Output: 넷마스크를 정수로 바꾼 것
    '''
    cidr = int(cidr)
    n = (1<<cidr)-1
    n = n<<(32-cidr)
    return n

def netmasking(ip_s, netmask_s, cidr = False):
    '''
    Input: 네 개의 옥텟으로 된 IP 주소와 서브넷 마스크 OR 네 개의 옥텟으로 된 IP 주소, CIDR 서브넷 마스크, cidr = True
    Output: {네트워크 ID, 브로드캐스트 주소, 호스트 수}
    '''
    ip = ip_to_int(ip_s)                    # ip 주소를 정수로 변환한다.
    if cidr:                                # 넷마스크가 CIDR일 경우:
        netmask = cidr_to_int(netmask_s)
    else:                                   # 넷마스크가 CIDR이 아닐 경우:
        netmask = ip_to_int(netmask_s)

    network_id = ip & netmask                  # 네트워크 ID는 ip & netmask다.
    netmask_neg = netmask^((1<<32)-1)          # 넷마스크를 반전시킨다.
    broadcast_addr = network_id + netmask_neg  # 브로드캐스트 주소를 구한다. 
    
    d = {'네트워크 ID': int_to_ip(network_id), '브로드캐스트 주소': int_to_ip(broadcast_addr), '호스트 수': netmask_neg -1} 
    return d


#print(ip_to_int("192.168.1.1"))

if __name__ =="__main__":
    ip = input("IP: ")
    netmask = input("서브넷마스크: ")
    if '.' in netmask:
        res = netmasking(ip, netmask)
    else:
        res = netmasking(ip, netmask, cidr = True)
    
    print(" ")
    for k in res:
        print(f'{k}: {res[k]}')