# Technical Skill Assessment - AnchorzUp

Author: Endrit Sadriu

## Short Description

**Task:**

Write a program to count all valid ways of reaching the goal position (0, 0) to (x, y).

**Solution:**

Since the goal coordinates are give, we already know how many steps should we go east "E" and north "N", hence ``` x * E + y * N```. A simple permutation calculation of the string e.g "EENN" gives out ```EENN, NEEN, ENEN, NENE, ENNE, NNEE```.

## How to Run the Script

### 1. Run the script directly via Python:

Add goal coordinates to ```input.txt``` file and then run one of the following commands in CMD:

```bash
python main.py
```
```bash
docker-compose up
```