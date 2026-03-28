import collections
import sys

sys.setrecursionlimit(9999999)

bilo = []
top = []
bilos = set()

n = int(input())


def proverka(a, b):
    c1, c2 = [0] * 10, [0] * 10
    for d in str(a):
        c1[int(d)] += 1
    for d in str(b):
        c2[int(d)] += 1
    return sum(abs(c1[i] - c2[i]) for i in range(10)) == 2


m = int("1" + "0" * n) - 1
prost = [q for q in range(m)]
prost[1] = 0
i = 2
while i * i <= m:
    if prost[i] != 0:
        j = i + i
        for j in range(i * i, m, i):
            prost[j] = 0
    i += 1
prost = [q for q in prost if q != 0 and q >= int("1" + "0" * (n - 1))]

sosedi = collections.defaultdict(list)
buckets = collections.defaultdict(list)

for p in prost:
    s = sorted(list(str(p)))
    for i in range(len(s)):
        mask = tuple(s[:i] + s[i+1:])
        buckets[mask].append(p)

for mask in buckets:
    nodes = buckets[mask]
    if len(nodes) > 1:
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                sosedi[nodes[i]].append(nodes[j])
                sosedi[nodes[j]].append(nodes[i])

print(len(sosedi))

def poisk(sosedi, prost):
    bilo = []
    for nachalo in prost:
        bilo.append(([nachalo], {nachalo}))

    top = []
    if n <= 3:
        shirina = 100
    elif n == 4:
        shirina = 10
    elif n >= 5:
        shirina = 1

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

        next_bilo.sort(key=lambda x: len(
            [n for n in sosedi[x[0][-1]] if n not in x[1]]))
        bilo = next_bilo[:shirina]

    return top

top = poisk(sosedi, prost)

print("-".join(map(str, top)))
print(len(top))
