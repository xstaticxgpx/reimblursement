#!/usr/bin/python

import yaml
import sys

class Project:
    def __init__(self, project):
        # Yuck! I had no idea python yaml did this - quote your strings!
        # In this case I'll abuse this for simplicity...
        # >>> yaml.safe_load("mykey: 2010-10-09")
        #{'mykey': datetime.date(2010, 10, 9)}
        # This is assuming we don't cross yearly boundaries, will allow arbitary ranges within any given year
        # https://docs.python.org/3/library/time.html#time.struct_time
        self.start = project['start'].timetuple().tm_yday
        self.end = project['end'].timetuple().tm_yday
        self.city = project['city']
        self.travel_day = project['city']['travel_day']
        self.full_day = project['city']['full_day']
        self.desc = project['city']['desc']
    def __repr__(self):
        return str(f"Project(start: {self.start}, end: {self.end}, city: {self.city})")
    def duration(self):
        return range(self.start, self.end+1)

class ProjectDay:
    def __init__(self, project):
        self.project = project
        self.val = 0
    def __iadd__(self, val):
        self.val += val
        return self
    # Missing some black magic for `sum()` usage
    def __add__(self, other):
        return ProjectDay(self.val + other)
    def __int__(self):
        return self.val
    def __repr__(self):
        return str(f"{self.val}")
    # We only need gt for `max()` 
    def __gt__(self, other):
        return self.val > other.val

def calculate(debug, parsed):
    min_start = min([project['start'].timetuple().tm_yday for project in parsed])
    max_end = max([project['end'].timetuple().tm_yday for project in parsed])

    # Each day is only counted once, use a dict of `day: [ProjectDay, ..]`
    # which is subequently flattened with `max` using list comprehension
    results = {day: [] for day in range(min_start, max_end+1)}
    for project in parsed:
        project = Project(project)
        if debug: print(project)
        for day in project.duration():
            pdc = ProjectDay(project)
            if day == project.start:
                # Assume start is travel day
                cost = project.travel_day
                # If we overlapped, take a full day, will take highest cost
                if len(results[day]) > 0:
                    if debug: print(day, "--> overlap (full day)")
                    cost = project.full_day
                # Or if we worked the previous day
                elif day > min_start and len(results[day-1]) > 0:
                    if debug: print(day, "--> pushed up against (full day)")
                    # We also want to bump previous day to that projects full day?
                    previous_day = results[day-1][-1]
                    previous_day.val = previous_day.project.full_day
                    cost = project.full_day
                if debug: print(day, 'start', project.desc)
                pdc += cost
            elif project.start < day < project.end:
                # Assume full day in the middle
                if debug: print(day, 'middle', project.desc)
                pdc += project.full_day
            elif day == project.end:
                # Assume end is travel day
                if debug: print(day, 'end', project.desc)
                pdc += project.travel_day
            results[day].append(pdc)

    if debug: print(results)
    return [max(day) for day in results.values() if len(day) > 0]

def main():
    debug = "--debug" in sys.argv[1:]
    with open("./sets_with_time.yaml") as f:
        sets = yaml.safe_load(f)
    print("Calculating project sets...\n")
    for s in sets['sets']:
        if debug: print("---")
        results = calculate(debug, sets['sets'][s])
        total = 0
        for result in results:
            # Ugh why can't we get inferred int representation here (ie. to use sum() directly)
            total += int(result)
        print(f"{s} {results} = ${total} ({len(results)} days)")

if __name__ == '__main__':
    main()
