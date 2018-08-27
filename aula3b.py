import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#    0: vazia
#    1: muro
#    2: objetivo
#    3: celula visitada

ei = (3,3,0,0,-1)
ef = (0,0,3,3,1)

listaEstados = []

#estado atual, pai, custo, aberta
listaEstados.append([ei,ei,0,1])

while not(True in [i[0]==ef for i in listaEstados]):
    listaEstados.sort(key=lambda x: (-x[3],x[2]))

    if listaEstados[0][3] == 0:
        print("estado nao encontrado")
        lst = [i[0] for i in listaEstados]
        print(lst)
        exit()

    listaEstados[0][3] = 0

    c1,m1,c2,m2,op = listaEstados[0][0]
    custoatual = listaEstados[0][2]

    print('opening and closing %d,%d,%d,%d,%d' % (c1,m1,c2,m2,op))

    searchorder = [[1,0],[0,1],[2,0],[0,2],[1,1]]

    for i in searchorder:
        dc, dm = i

        dc1 = c1 + op*dc
        dc2 = 3 - dc1
        dm1 = m1 + op*dm
        dm2 = 3 - dm1
        dop = -op 

        dxcurrent = (dc1,dm1,dc2,dm2,dop)

        if not(dc1 in range(0,4) and dm1 in range(0,4)):
            continue
        
        if True in [l[0]==dxcurrent for l in listaEstados]:
            continue

        if m1 > 0 and c1 > m1:
            continue

        if m2 > 0 and c2 > m2:
            continue

        print('adicionando %d,%d,%d,%d,%d = %d' % (dc1,dm1,dc2,dm2,dop,custoatual+1))
        listaEstados.append([dxcurrent,listaEstados[0][0],custoatual+1,1])

if (True in [i[0]==ef for i in listaEstados]):
    print('estado final encontrado')
    print(ef)
 
print(len(listaEstados))
lst = [i[0] for i in listaEstados]
print(lst) 


final =  [i for i in listaEstados if i[0]==ef]

track = [final[0][0]]
print('tracking')
while final[0][0]!= ei:    
    for i in listaEstados:
        if i[0]==final[0][1]:
            print(final[0])
            final[0] = i
            track.append(final[0][0])
            continue

track.reverse()

for i in track:
    print(i)