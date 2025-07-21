#!/usr/bin/python3
import sys

current_country = None
partial_days_closed = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        country, count = line.split('\t')
        count = int(count)
    except:
        continue

    if current_country == country:
        partial_days_closed += count
    else:
        if current_country:
            print(f"{current_country}\t{partial_days_closed}")
        current_country = country
        partial_days_closed = count

if current_country:
    print(f"{current_country}\t{partial_days_closed}")
