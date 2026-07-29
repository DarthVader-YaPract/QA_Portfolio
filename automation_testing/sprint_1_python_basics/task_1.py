raw_time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_m = 0
raw_time.split(',')
for time in raw_time.split(','):
    for part in time.split(' '):
        if 'h' in part:
            res_h = int(part.replace('h',''))*60
            total_m += res_h
        elif 'm' in part:
            res_m = int(part.replace('m', ''))
            total_m += res_m
        elif 's' in part:
            res_s = int(part.replace('s', ''))//60
            total_m += res_s
print(total_m)