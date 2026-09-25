def parse_cdp_neighbors(comand_output):
    


    s =  comand_output.split('\n')
    local_device = ''
    for line in s:
        if '>' in line:
            local_device = line.split('>')[0].strip()
            break



    r = {}
    data_started = False
    for line in s:
        parts  = line.split()
        
        if len(parts) >= 2 and parts[0] == 'Device' and parts[1] == 'ID':
            data_started = True
            continue
        if data_started and len(parts) >= 6:

            n = parts[0]
            int = parts[1] + parts[2]
            remote_int = parts[-2] + parts[-1]
            r[(local_device, int)] = (n, remote_int)
    return r
if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        print(parse_cdp_neighbors(f.read()))

