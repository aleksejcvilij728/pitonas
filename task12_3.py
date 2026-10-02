import ipaddress
import subprocess
from tabulate import tabulate

net = ipaddress.ip_network('192.168.100.0/24')


def ping_ip_addresses(network):
    bad = []
    norm = []
    for i in network:
        a =  subprocess.run(['ping', '-c', '1', '-W', '0.5', str(i)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if a.returncode == 0:
            norm.append(str(i))
        else:
            bad.append(str(i))
    return norm, bad

colums = ['Reachable', 'Unreachable']
print(tabulate(ping_ip_addresses(net), headers=colums))
