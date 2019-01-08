# Toolkits

Many small toolkits written in MATLAB, Python, R, and C in the past few years.

## MATLAB

* merge_pictures
    - Aims to merge pictures more conveniently.
    - Syntax: `merged_picture = merge_pictures(working_directory)`
* Towers.of.Hanoi
    - Animation of the solutions to Towers of Hanoi.
    - Syntax: `toh(N)` or `toh_Ch(N)`
* DIY_Logo: some programs handling with the pictures
    - run.m
        + Start demonstrate all the programs.
        + Syntax: `run`
    - letterz.m, letterj.m, letteru.m, and lettert.m (letter*.m)
        + Draw the shape of letters Z, J, U, T respectively.
        + Syntax: `letter*(N)`, N ranges from 0 to 255
    - diylogo_gray.m and diylogo_rgb.m
        + Combine letters and generate a picture.
        + Syntax: 
            1. `diylogo_gray(string, depth)`
            2. `diylogo_rgb(string, depth, RGB)`

## R

* area_classification: the project to participate in Alibaba big data contest.

## C

* [`permute.c`](https://github.com/jinlibao/toolkits/blob/master/C/permute.c): implementation of permutation using recursion.
* [`merge_sort.c`](https://github.com/jinlibao/toolkits/blob/master/C/merge_sort.c): very concise implementation of merge sort using recursion.
* [`hash_table.c`](https://github.com/jinlibao/toolkits/blob/master/C/hash_table.c): implementation of hash table based on linked list.
* [`count_days.c`](https://github.com/jinlibao/toolkits/blob/master/C/count_days.c): to calculate the day of the year.
* [`sort_chars.c`](https://github.com/jinlibao/toolkits/blob/master/C/sort_chars.c): to sort characters/letters.
* [`student_scores.c`](https://github.com/jinlibao/toolkits/blob/master/C/stduent_scores.c): to calculate the average scores by courses/students.

# Python

* Computer.Performance: to see the performance of Python on a certain platform by the runtime.
* Forgetting.Curve: to visualize the forgetting curve.
* `Get_PDF.py`: to download files (in PDF, PPT, and etc.) from course websites of CMU, Standfor, and etc.
* Numpy: an simple demo for using Numpy.
* Project.Euler: solutions for little portions of Project Euler.
* Crawler.Python: basic template for scraping written in Python.
* X-rates: to scrap the exchange rate of two currencies during a specific period of time and visualize the result.
* Zjut: to get the login information from the Teachers Data Center of ZJUT and to use brutal force to collect accounts with weak password such as `123456`, `321123`.
* MySQL-docs: to scrap the documentation from MySQL webiste.
