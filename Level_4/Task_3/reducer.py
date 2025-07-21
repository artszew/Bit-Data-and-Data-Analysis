#!/usr/bin/python3
import sys

current_country = None
days_closed = 0

for line in sys.stdin:
    line = line.strip()
    country, count = line.split('\t')
    try:
        count = int(count)
    except:
        continue

    if current_country == country:
        days_closed += count
    else:
        if current_country:
            print('%s\t%d' % (current_country, days_closed))
        current_country = country
        days_closed = count

if current_country:
    print('%s\t%d' % (current_country, days_closed))
