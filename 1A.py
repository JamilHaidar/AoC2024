with open('input/1A.txt','r') as f:
    data = f.read().replace('\n',' ').split()
    list1 = sorted(map(int,data[::2]))
    list2 = sorted(map(int,data[1::2]))
    ans = sum([abs(elem[0]-elem[1]) for elem in zip(list1,list2)])
    print(ans)