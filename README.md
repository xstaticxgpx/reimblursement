### Usage

1. Define the sets in YAML

2. Run the program
```
$ ./with_yaml.py
Calculating project sets...

set1 [45, 75, 45] = 165
set2 [75, 85, 85, 85, 85, 75, 75, 45] = 610
set3 [45, 75, 45, 55, 85, 55, 85] = 445
set4 [75, 85, 55] = 215
```

Optionally with debugging:
```
$ ./with_yaml.py --debug
Calculating project sets...

1 start low cost city
2 middle low cost city
3 end low cost city
{1: [45], 2: [75], 3: [45]}
set1 [45, 75, 45] = 165
1 1_full_day low cost city
2 start high cost city
pushed up against
3 middle high cost city
4 middle high cost city
5 middle high cost city
6 end high cost city
6 start low cost city
overlap
7 middle low cost city
8 end low cost city
{1: [75], 2: [85], 3: [85], 4: [85], 5: [85], 6: [55, 75], 7: [75], 8: [45]}
set2 [75, 85, 85, 85, 85, 75, 75, 45] = 610
1 start low cost city
2 middle low cost city
3 end low cost city
5 start high cost city
6 middle high cost city
7 end high cost city
8 1_full_day high cost city
{1: [45], 2: [75], 3: [45], 4: [], 5: [55], 6: [85], 7: [55], 8: [85]}
set3 [45, 75, 45, 55, 85, 55, 85] = 445
1 1_full_day low cost city
1 1_full_day low cost city
2 1_full_day high cost city
2 start high cost city
overlap
3 end high cost city
{1: [75, 75], 2: [85, 85], 3: [55]}
set4 [75, 85, 55] = 215
```
