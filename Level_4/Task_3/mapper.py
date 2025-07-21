#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) < 14:
        continue
    country = parts[0]
    try:
        school_closing = int(parts[12])  # school_closing
        workplace_closing = int(parts[13])  # workplace_closing
    except:
        continue
        
    if school_closing > 0 and workplace_closing > 0:
        print('%s\t1' % country)
