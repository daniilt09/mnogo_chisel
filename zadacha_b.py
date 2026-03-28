import collections

bilo = []
count = 0
top = []
bilos = set()

n = int(input())

def proverka(proshloe, chis):
    s1, s2 = str(proshloe), str(chis)
    if abs(len(s1) - len(s2)) != 1:
        return False
    if len(s1) > len(s2):
        long, short = s1, s2
    else:
        long, short = s2, s1
    for i in range(len(long)):
        if long[:i] + long[i + 1 :] == short:
            return True
    return False

prost = [q for q in range(n)]
prost[1] = 0
i = 2
while i * i <= n:
    if prost[i] != 0:
        j = i + i
        for j in range(i * i, n, i):
            prost[j] = 0
    i += 1
prost = [q for q in prost if q != 0]

sosedi = collections.defaultdict(list)
for i in range(len(prost)):
    for j in range(i + 1, len(prost)):
        if proverka(prost[i], prost[j]):
            sosedi[prost[i]].append(prost[j])
            sosedi[prost[j]].append(prost[i])

print(len(sosedi))

def poisk(sosedi, prost):
    bilo = []
    for nachalo in prost:
        bilo.append(([nachalo], {nachalo}))
    
    top = []
    if n <= 1000:
        shirina = 100
    elif n == 10000:
        shirina = 5
    elif n >= 100000:
        shirina = 2

    while bilo:
        next_bilo = []
        for put, posisheno in bilo:
            if len(put) > len(top):
                top = put
            
            seichas = put[-1]
            if seichas in sosedi:
                variki = []
                for nxt in sosedi[seichas]:
                    if nxt not in posisheno:
                        variki.append(nxt)
                
                for nxt in variki:
                    novoe_posisheno = set(posisheno)
                    novoe_posisheno.add(nxt)
                    next_bilo.append((put + [nxt], novoe_posisheno))
        
        if not next_bilo:
            break
            
        next_bilo.sort(key=lambda x: len([n for n in sosedi[x[0][-1]] if n not in x[1]]), reverse = True)
        bilo = next_bilo[:shirina]

    return top


top = poisk(sosedi, prost)

print("-".join(map(str, top)))
print(len(top))
