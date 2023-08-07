#!/usr/bin/python

import yaml

def calculate(name, parsed):
    days = []
    start = min([project['start'] for project in parsed])
    end = max([project['end'] for project in parsed])

    # Each day is only counted once
    result = []
    for day in range(start, end+1):
        for project in parsed:
            if project['start'] == day:
                result.append(project['city']['travel_day'])
            elif project['end'] == day:
                result.append(project['city']['travel_day'])
            elif project['start'] <= day:
                result.append(project['city']['full_day'])
    print(result, "=", sum(result))

def main():
    with open("./sets.yaml") as f:
        sets = yaml.safe_load(f)
    print("Found %d sets." % len(sets['sets']))
    for s in sets['sets']:
        calculate(s, sets['sets'][s])

if __name__ == '__main__':
    main()
