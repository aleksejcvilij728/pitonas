import ipaddress
import subprocess

net = ipaddress.ip_network('192.168.1.0/30')

def ping_ip_addresses(network):
    bad = []
    norm = []
    for i in network:
        a =  subprocess.run(['ping', '-c', '1', str(i)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if a.returncode == 0:
            norm.append(str(i))
        else:
            bad.append(str(i))
    return norm, bad


print(ping_ip_addresses(net))
