from collections import Counter
with open('input/1A.txt','r') as f:
    data = f.read().replace('\n',' ').split()
    list1 = map(int,data[::2])
    list2 = Counter(map(int,data[1::2]))
    ans = sum([elem*list2[elem] for elem in list1])
    print(ans)