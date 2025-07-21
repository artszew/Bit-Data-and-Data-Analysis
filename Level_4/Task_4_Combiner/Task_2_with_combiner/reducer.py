#!/usr/bin/python3
import sys

current_country = None
total_cases = 0
total_days = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) != 3:
        continue
    country, cases, days = parts
    try:
        cases = int(cases)
        days = int(days)
    except:
        continue

    if current_country == country:
        total_cases += cases
        total_days += days
    else:
        if current_country:
            avg = float(total_cases) / total_days if total_days > 0 else 0
            print('%s\t%.2f' % (current_country, avg))
        current_country = country
        total_cases = cases
        total_days = days

if current_country:
    avg = float(total_cases) / total_days if total_days > 0 else 0
    print('%s\t%.2f' % (current_country, avg))
