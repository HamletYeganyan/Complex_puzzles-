import random
import random
# random map generator by Rova 
y = 10 
x = 10 
list1 = []
choice = '001' 
map = []
island = 0
for i in range(10):
    tox = []
    if i == 0:
        for j in range(10):
            point = random.choice(choice)
            if point == '1':
                tox.append(point)
            elif point == '0':
                tox.append(point)
        map.append(tox)
    else:
        for j in range(10):
            point = random.choice(choice)
            if point == '1':
                tox.append(point)       
            elif point == '0':
                tox.append(point)
        map.append(tox)
for i in range(len(map)):
    for j in range(len(map[i])):
        map[i] = ''.join(map[i])
        list1.append([map[i]])
        break
# zronerov shrjapakum enq vor nmanvi covi
for el in range(len(list1[0][0])):
    if '1' in list1[0][0]:
        list1.insert(0, ['0' * len(list1[0][0])])
    if '1' in list1[-1][0]:
        list1.append(['0' * len(list1[0][0])])
for k in range(len(list1)):
    if list1[k][0][0] == '1':
        for l in range(len(list1)):
            obe = list(list1[l][0])
            obe.insert(0, '0')
            list1[l] = [''.join(obe)]
    if list1[k][0][-1] == '1':
        for l in range(len(list1)):
            obe = list(list1[l][0])
            obe.append('0')
            list1[l] = [''.join(obe)]
# sahmanum enq yuraqancur '1' in shrjapakox 8 nshannery sksac szaxic jamslakin hakarak    
_1 = []
_2 = []
_3 = []
_4 = []
_5 = []
_6 = []
_7 = []
_8 = []
one = []

for hi in range(len(list1)):
    for le in range(len(list1[0][0])):
        if list1[hi][0][le] == '1':
            _1.append(list1[hi][0][le - 1])
            _2.append(list1[hi + 1][0][le - 1])
            _3.append(list1[hi + 1][0][le])
            _4.append(list1[hi + 1][0][le + 1])
            _5.append(list1[hi][0][le + 1])
            _6.append(list1[hi - 1][0][le + 1])
            _7.append(list1[hi - 1][0][le])
            _8.append(list1[hi - 1][0][le - 1])

for num in range(len(_1)):
    one.append([])
for u in range(len(_1)):
    one[u].append(_1[u])
    one[u].append(_2[u])
    one[u].append(_3[u])
    one[u].append(_4[u])
    one[u].append(_5[u])
    one[u].append(_6[u])
    one[u].append(_7[u])
    one[u].append(_8[u])
# kxzineri tpelu fory
for i in range(len(list1)):
    for j in range(len(list1[0][0])):
        if list1[i][0][j] == '0':
            print('🌊', end='')
        elif list1[i][0][j] == '1':
            print('🟨', end='')
    print()
# talis enq amen andami koordinatnery skzbum toxi indexy heto ira indexy
name = []
indexes = []
cord = []
crd = []
for _ in range(len(list1)):
    indexes.append([])
    cord.append([])
       
for i in range(len(list1)):
    for j in range(len(list1[i][0])):
        if list1[i][0][j] == '1':
            indexes[i].append(j)
for sub in range(len(indexes)):
    for su in range(len(indexes[sub])):
        cord[sub].append(sub)
        cord[sub].append(indexes[sub][su])
for y in range(len(cord)):
    for x in range(len(cord[y])):
        if x % 2 == 0:
            pgp = [cord[y][x], cord[y][x + 1]]
            crd.append(pgp)

#  sahmanum enq bararan vortex kgrenq iranc koordinatnern u shrjapatox nshannery

dict_matrix = {}
dict_pra = {}
pra = []
for numb in range(len(one)):
    name.append(numb)
for numbe in range(len(one)):
    pra.append(f'{crd[numbe]}')
for pz , zp in zip(name, one):
    dict_matrix[pz] = zp
for vp, pv in zip(pra, one):
    dict_pra[vp] = pv
# gtnum enq amen andamin shrjapatox 1 eri koordinatnery
def CRD(I,J):
    if J == 0:
        return [crd[I][0], crd[I][1] - 1]
    if J == 1:
        return [crd[I][0] + 1, crd[I][1] - 1]
    if J == 2:
        return [crd[I][0] + 1, crd[I][1]]
    if J == 3:
        return [crd[I][0] + 1, crd[I][1] + 1]
    if J == 4:
        return [crd[I][0], crd[I][1] + 1]
    if J == 5:
        return [crd[I][0] - 1, crd[I][1] + 1]
    if J == 6:
        return [crd[I][0] - 1, crd[I][1]]
    if J == 7:
        return [crd[I][0] - 1, crd[I][1] - 1]
# bararanic vercnum enq 1 i arjeqy ev texadrum verevi funkciai mej
def island_logic(n):
    flag = []
    for j in range(8):
            if dict_matrix[n][j] == '1':
                flag.append(CRD(n,j))
    return flag
# sahmanum enq nor cucakner
frag = [] # hamapatasxanum e crd cucaki andamnerin
deep = [] # aystex grvum e skzbum 1 i indexy crd cucakum heto stugvum e ir harevanneri indexnery [ira index, harevani index]
force = [] # forcei mej texavorvum en bolor hnaravor kombinacianery deep i andamneri orinak [0, 1] [0, 6] [0, 12] vortex grvac e 0 andami bolor harevannei indexnery 
for s in range(len(crd)):                
    frag.append(island_logic(s))
for p in range(len(crd)):
    for q in range(len(frag)):
        if crd[p] in frag[q]:
          deep.append([p, q])
for _ in range(len(frag)):
    force.append([])
for t in range(len(deep)):
    for n in range(len(deep)): 
        if deep[t][0] == n:
            force[n].append(deep[t][1])

# force i mej havaqvum en bolor liarjeq kxzinery u apahovutyan hamar kody krknvum e
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])
for i in range(len(force)):
    for j in range(len(force[i])):
        for k in range(len(force[force[i][j]])):
            if force[force[i][j]][k] not in force[i]:
                force[i].append(force[force[i][j]][k])

for f in range(len(force)):
    force[f] = sorted(force[f])
for d in force.copy():
    if force.count(d) > 1 and d != []:
        force.remove(d)

print('islands =' , len(force))
print(force)


