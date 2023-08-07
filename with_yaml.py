#!/usr/bin/python

import yaml
import sys

def calculate(debug, parsed):
    min_start = min([project['start'] for project in parsed])
    max_end = max([project['end'] for project in parsed])

    # Each day is only counted once, use a dict of `day: [cost, ..]`
    results = {day: [] for day in range(min_start, max_end+1)}
    for project in parsed:
        start_day  = project['start']
        end_day    = project['end']
        full_day   = project['city']['full_day']
        travel_day = project['city']['travel_day']
        for day in range(start_day, end_day+1):
            if day == start_day:
                # Assume start is travel day
                cost = travel_day
                # If we overlapped, take a full day
                if len(results[day]) > 0:
                    if debug: print(day, "--> overlap (full day)")
                    cost = full_day
                # Or if we worked the previous day
                elif day > 1 and len(results[day-1]) > 0:
                    # TODO: this doesn't take high cost of previous day (if needed?)
                    if debug: print(day, "--> pushed up against (full day)")
                    # TODO: also this overrrides low cost full days with high
                    results[day-1].append(full_day)
                    cost = full_day
                if debug: print(day, 'start', project['city']['desc'])
                results[day].append(cost)
            elif day == end_day:
                # Assume end is travel day
                if debug: print(day, 'end', project['city']['desc'])
                results[day].append(travel_day)
            elif start_day <= day <= end_day:
                # Assume full day in the middle
                if debug: print(day, 'middle', project['city']['desc'])
                results[day].append(full_day)

    if debug: print(results)
    return [max(day) for day in results.values() if len(day) > 0]

def main():
    debug = "--debug" in sys.argv[1:]
    with open("./sets.yaml") as f:
        sets = yaml.safe_load(f)
    print("Calculating project sets...\n")
    for s in sets['sets']:
        if debug: print("---")
        results = calculate(debug, sets['sets'][s])
        print(f"{s} {results} = ${sum(results)}")

if __name__ == '__main__':
    main()
