
def max_value(lis,num, indexPar):
    if len(lis) < 2:
        return lis[0], str(lis[0])

    best_score = -float('inf')
    LC = []
    RL = []
    index = int(len(lis)/2)
    j = index
    for i in range(index):
        LC.append(lis[i])
        RL.append(lis[j])
        j += 1
    if j < len(lis):
        RL.append(lis[j])

    ind = indexPar
    indexPar = (indexPar*2) + 1

    n1, yal1 = min_value(LC, num, indexPar)
    n2, yal2 = min_value(RL, num, indexPar+1)
    best_score = max(n1, n2, best_score)

    if best_score == n1:
        yal = chr(num+ind) + " <- " + yal1
    else:
        yal = chr(num+ind) + " <- "+yal2

    return best_score, yal


def min_value(lis,num, indexPar):
    if len(lis) < 2:
        return lis[0], str(lis[0])

    best_score = float('inf')
    LC = []
    RL = []
    index = int(len(lis)/2)
    j = index
    for i in range(index):
        LC.append(lis[i])
        RL.append(lis[j])
        j += 1
    if j < len(lis):
        RL.append(lis[j])

    inde = indexPar
    indexPar = (2*indexPar) + 1
    n1, yal1 = max_value(LC, num, indexPar)
    n2, yal2 = max_value(RL, num, indexPar+1)
    best_score = min(n1, n2, best_score)

    if best_score == n1:
        yal = chr(num+inde)+" <- " + yal1
    else:
        yal = chr(num+inde)+" <- " + yal2

    return best_score, yal

def minimax(lis, num, indexPar):
    return max_value(lis, num, indexPar)


lis = [int(x) for x in input().split()]
x , yal = minimax(lis, 65, 0)
print(x)
print(yal)