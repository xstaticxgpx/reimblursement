#!/usr/bin/python

import yaml

def calculate(name, parsed):
    start = min([project['start'] for project in parsed])
    end = max([project['end'] for project in parsed])

    # Each day is only counted once, use a dict of `day: cost`
    # each day initialized at `0`
    results = {day: 0 for day in range(start, end+1)}
    for project in parsed:
        for day in range(start, end+1):
            # Gap days will be 0
            cost = 0
            if day == project['start'] == project['end']:
                # Assuming 1 day project is full day?
                print(day, '1_full_day', project['city']['desc'])
                cost = project['city']['full_day']
            elif day == project['start']:
                # Assume start is travel day
                print(day, 'start', project['city']['desc'])
                cost = project['city']['travel_day']
                # Unless we worked the previous day
                if day-1 > 0 and results[day-1] > 0:
                    # TODO: this doesn't assume previous high cost day?
                    cost = project['city']['full_day']
                # Or if we overlapped, take a full day
                elif results[day] > 0:
                    cost = project['city']['full_day']
            elif day == project['end']:
                # Assume end is travel day
                print(day, 'end', project['city']['desc'])
                cost = project['city']['travel_day']
            elif project['start'] <= day <= project['end']:
                # Assume full day in the middle
                print(day, 'middle', project['city']['desc'])
                cost = project['city']['full_day']
            # Assuming highest cost?
            if cost > results[day]:
                results[day] = cost
    print(results.values(), "=", len(results.values()), "days", "=", sum(results.values()))
    print("---")

def main():
    with open("./sets.yaml") as f:
        sets = yaml.safe_load(f)
    for s in sets['sets']:
        calculate(s, sets['sets'][s])

if __name__ == '__main__':
    main()
