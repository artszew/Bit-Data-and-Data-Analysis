#!/usr/bin/env python3
import sys

current_country = None
total_vaccinated = 0
population = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        country, data = line.split('\t')
        vaccinated, pop = map(int, data.split(','))

        if current_country == country:
            total_vaccinated += vaccinated
        else:
            if current_country:
                print(f"{current_country}\t{total_vaccinated},{population}")
            current_country = country
            total_vaccinated = vaccinated
            population = pop  # zakładamy, że populacja się nie zmienia
    except:
        continue

if current_country:
    print(f"{current_country}\t{total_vaccinated},{population}")
