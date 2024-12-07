import re

with open("temp.txt") as f:
    data = f.read() # data is xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    # match all "do" string
    data = re.findall(r"\bdo\b", data) 
    print(data)
    ans = sum([int(elem)*int(elem2) for elem, elem2 in data])
    print(ans)