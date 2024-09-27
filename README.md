# Technical Skill Assessment - AnchorzUp

Author: Endrit Sadriu

## Short Description

**Task:**

Write a program to count all valid ways of reaching from (0,0) to goal position (x,y).

**Solution:**

Since the goal coordinates are given, we already know how many steps are there to go east "E" and north "N", hence ``` x * E + y * N```. A simple permutation calculation of the string e.g "EENN" gives out ```EENN, NEEN, ENEN, NENE, ENNE, NNEE```.

## How to Run the Script

Add goal coordinates to ```input.txt``` file and then run one of the following commands in CMD:

```bash
python main.py
```
```bash
docker-compose up
```