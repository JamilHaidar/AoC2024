import re

with open("input/3A.txt") as f:
    data = f.read()
    data = re.findall(r'mul\((\d+),(\d+)\)', data)
    ans = sum([int(elem)*int(elem2) for elem, elem2 in data])
    print(ans)