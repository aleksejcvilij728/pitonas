infiles = [

    "sh_cdp_n_sw1.txt",

    "sh_cdp_n_r1.txt",

    "sh_cdp_n_r2.txt",

    "sh_cdp_n_r3.txt",

]

def create_network_map(filenames):
    common = {}
    for i in filenames:
        
        with open(i, 'r') as f:
            s = f.read().split('\n')
            local_dev = ''
            for  j in s:
                if '>' in j:
                    local_dev = j.split('>')[0].strip()
                    break
            r = {}
            data_started = False
            for line in s:
                parts = line.split()
                if len(parts) >=2 and parts[0] == 'Device' and parts[1] == 'ID':
                    data_started = True
                    continue
                if data_started and len(parts) >= 6:
                    n = parts[0]
                    intf = parts[1] + parts[2]
                    remote_int = parts[-2] + parts[-1]
                    r[(local_dev, intf)] = (n, remote_int)
        common.update(r)
          
    return common
print (create_network_map(infiles))
