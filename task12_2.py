import ipaddress


net = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'] 


def convert_ranges_to_ip_list(list):
    result = []
    for i in list:
        if '-' in i:
            a = i.split('-')
            start_str = a[0]
            end_str =a[1]
            if '.' not in end_str:
                prefix = '.'.join(start_str.split('.')[:3])
                end_str = prefix + '.' + end_str
            start = ipaddress.ip_address(start_str)
            end = ipaddress.ip_address(end_str)
            current = start
            
            while current <= end:
                result.append(str(current)) 
                current += 1
            
        else:
            result.append(i)
    return result
             
print(convert_ranges_to_ip_list(net))
