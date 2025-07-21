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
            print(f'{current_country}\t{total_cases}\t{total_days}')
        current_country = country
        total_cases = cases
        total_days = days

if current_country:
    print(f'{current_country}\t{total_cases}\t{total_days}')
