### High Level

We define the exercise as described in `sets.yaml` - using references ([anchors](https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet#anchors)) to the 2 different city types.

In `with_yaml.py` we take a purely procedural approach, with many short comings, such as:
- inability to determine properties of the previous day(s)

In `with_yaml_v2.py` we introduce classes in order to more easily work with the "day" objects

By extending a new object with the relevant properties we can work on that object directly "at a distance" - ie. during future iterations.

### Usage

1. See the defined sets in YAML

2. Run the program

This shouldn't require any special python packages besides `pytest`
```
# Try tests first:
$ python -m pytest test.py
..

$ ./with_yaml_v1.py
Calculating project sets...

set1 [45, 75, 45] = $165
set2 [85, 85, 85, 85, 85, 75, 75, 45] = $620 # <-- full day high cost city for Day 1 (wrong I think)
set3 [45, 75, 45, 55, 85, 85, 85] = $475
set4 [85, 85, 55] = $225 # <-- ditto

$ ./with_yaml_v2.py
Calculating project sets...

set1 [45, 75, 45] = $165
set2 [75, 85, 85, 85, 85, 75, 75, 45] = $610 # <-- full day low cost city for Day 1 (as expected?)
set3 [45, 75, 45, 55, 85, 85, 85] = $475
set4 [75, 85, 55] = $215 # <-- ditto

# With legitimate datetime parsing!
$ ./with_yaml_v3.py
Calculating project sets...

set1 [45, 75, 45] = $165 (3 days)
set2 [75, 85, 85, 85, 85, 75, 75, 45] = $610 (8 days)
set3 [45, 75, 45, 55, 85, 85, 85] = $475 (7 days)
set4 [75, 85, 55] = $215 (3 days)
set5 [45, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 55] = $3555 (45 days)
set6 [45, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 55] = $3640 (46 days)

# Optionally with debugging:
$ ./with_yaml.py --debug
Calculating project sets...

---
1 start low cost city
2 middle low cost city
3 end low cost city
{1: [45], 2: [75], 3: [45]}
set1 [45, 75, 45] = $165
---
...
```
