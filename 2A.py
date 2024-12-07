with open('input/2A.txt','r') as f:
    data = [list(map(int,elem.split())) for elem in f.read().splitlines()]
    counter = 0
    for level in data:
        level_diff = [level[elem_idx]-level[elem_idx-1] for elem_idx in range(1,len(level))]
        counter += int(all([-3 <= elem <0 for elem in level_diff]) or all([0 < elem <=3 for elem in level_diff]))
    print(counter)
