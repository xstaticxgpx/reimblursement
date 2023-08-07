### Usage

1. Define the sets in YAML

2. Run the program

This shouldn't require any special python packages.
```
$ ./with_yaml.py
Calculating project sets...

set1 [45, 75, 45] = $165
set2 [85, 85, 85, 85, 85, 75, 75, 45] = $620
set3 [45, 75, 45, 55, 85, 85, 85] = $475
set4 [85, 85, 55] = $225

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
1 start low cost city
2 --> pushed up against (full day)
2 start high cost city
3 middle high cost city
4 middle high cost city
5 middle high cost city
6 end high cost city
6 --> overlap (full day)
6 start low cost city
7 middle low cost city
8 end low cost city
{1: [45, 85], 2: [85], 3: [85], 4: [85], 5: [85], 6: [55, 75], 7: [75], 8: [45]}
set2 [85, 85, 85, 85, 85, 75, 75, 45] = $620
---
1 start low cost city
2 middle low cost city
3 end low cost city
5 start high cost city
6 middle high cost city
7 end high cost city
8 --> pushed up against (full day)
8 start high cost city
{1: [45], 2: [75], 3: [45], 4: [], 5: [55], 6: [85], 7: [55, 85], 8: [85]}
set3 [45, 75, 45, 55, 85, 85, 85] = $475
---
1 start low cost city
1 --> overlap (full day)
1 start low cost city
2 --> pushed up against (full day)
2 start high cost city
2 --> overlap (full day)
2 start high cost city
3 end high cost city
{1: [45, 75, 85], 2: [85, 85], 3: [55]}
set4 [85, 85, 55] = $225
```
