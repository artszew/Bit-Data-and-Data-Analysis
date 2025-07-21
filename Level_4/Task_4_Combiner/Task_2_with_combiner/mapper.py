#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) < 7:
        continue
    country = parts[0]
    date = parts[5]
    new_cases = parts[6] 
    try:
        new_cases = int(new_cases)
    except:
        continue
    print('%s\t%s\t%s' % (country, new_cases, 1))