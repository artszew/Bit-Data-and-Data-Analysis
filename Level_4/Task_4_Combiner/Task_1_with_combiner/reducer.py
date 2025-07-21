#!/usr/bin/env python3
"""reducer"""
import sys

current_country = None
total_vaccinated = 0
population = 0

for line in sys.stdin:
    country, data = line.strip().split('\t')
    vaccinated, pop = map(int, data.split(','))
    
    if current_country == country:
        total_vaccinated += vaccinated
    else:
        if current_country:
            percentage = (total_vaccinated / population) * 100 if population else 0
            print(f"{current_country}\t{percentage:.2f}%")
        current_country = country
        total_vaccinated = vaccinated
        population = pop

if current_country:
    percentage = (total_vaccinated / population) * 100 if population else 0
    print(f"{current_country}\t{percentage:.2f}%")
