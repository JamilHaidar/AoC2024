def is_safe(level: list):
    level_diff = [level[elem_idx]-level[elem_idx-1] for elem_idx in range(1,len(level))]
    return all([-3 <= elem <0 for elem in level_diff]) or all([0 < elem <=3 for elem in level_diff])


with open('input/2A.txt','r') as f:
    data = [list(map(int,elem.split())) for elem in f.read().splitlines()]
    counter = 0
    for level in data:
        if is_safe(level):
            counter += 1
            continue
        for i in range(len(level)):
            if is_safe(level[:i]+level[i+1:]):
                counter += 1
                break
    print(counter)
