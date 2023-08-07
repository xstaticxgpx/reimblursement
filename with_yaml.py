#!/usr/bin/python

import yaml

def calculate(name, parsed):
    start = min([project['start'] for project in parsed])
    end = max([project['end'] for project in parsed])

    # Each day is only counted once, use a dict of `day: cost`
    # each day initialized at `0`
    results = {day: 0 for day in range(start, end+1)}
    for project in parsed:
        start_day = project['start']
        end_day = project['end']
        travel_day = project['city']['travel_day']
        full_day = project['city']['full_day']
        for day in range(start, end+1):
            # Gap days will be 0
            cost = 0
            if day == start_day == end_day:
                # Assuming 1 day project is full day?
                print(day, '1_full_day', project['city']['desc'])
                cost = full_day
            elif day == start_day:
                # Assume start is travel day
                print(day, 'start', project['city']['desc'])
                cost = travel_day
                # If we overlapped, take a full day
                if results[day] > 0:
                    print("overlap")
                    cost = full_day
                # Or if we worked the previous day
                elif day-1 > 0 and results[day-1] > 0:
                    # TODO: this doesn't take high cost of previous day (if needed?)
                    cost = full_day
            elif day == end_day:
                # Assume end is travel day
                print(day, 'end', project['city']['desc'])
                cost = travel_day
            elif start_day <= day <= end_day:
                # Assume full day in the middle
                print(day, 'middle', project['city']['desc'])
                cost = full_day
            # Assuming highest cost?
            if cost > results[day]:
                results[day] = cost
    return results

def main():
    with open("./sets.yaml") as f:
        sets = yaml.safe_load(f)
    print("Calculating project sets...")
    for s in sets['sets']:
        results = calculate(s, sets['sets'][s])
        print(results.values(), "=", len(results.values()), "days", "=", sum(results.values()))
        print("---")

if __name__ == '__main__':
    main()
