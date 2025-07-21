#!/usr/bin/env python3
import sys

next(sys.stdin)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split(',')
    try:
        country = fields[0]
        vaccinated = int(fields[9]) if len(fields) > 9 and fields[9] else 0
        population = int(fields[20]) if len(fields) > 20 and fields[20] else 0
        if population > 0:
            print(f"{country}\t{vaccinated},{population}")
    except Exception:
        continue
