import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#    0: vazia
#    1: muro
#    2: objetivo
#    3: celula visitada

grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

gmax = len(grid) -1

listaEstados = []

#estado atual, pai, custo, aberta
listaEstados.append([(0,0),(0,0),0,1])

while not(True in [i[0]==(5,5) for i in listaEstados]):
    listaEstados.sort(key=lambda x: (-x[3],x[2]))

    if listaEstados[0][3] == 0:
        print("estado nao encontrado")
        lst = [i[0] for i in listaEstados]
        print(lst)
        exit()

    listaEstados[0][3] = 0

    x,y = listaEstados[0][0]

    print('opening and closing %d,%d' % (x, y))

    searchorder = [[1,0],[0,-1],[-1,0],[0,1]]

    for i in searchorder:
        dx, dy = i

        nx = x + dx
        ny = y + dy

        #print('analisando %d,%d' % (nx, ny))

        #verifica se esta dentro do grid
        if nx>=0 and nx<=gmax and ny>=0 and ny<=gmax:    
            if True in [i[0]==(nx,ny) for i in listaEstados]:
                #print('no ja adicionado %d,%d' % (nx, ny))
                continue

            if grid[nx][ny]== 1:
                print( 'no bloqueado %d,%d' % (nx, ny))
                continue
            elif grid[nx][ny]== 2:
                print( 'estado final encontrado %d,%d' % (nx, ny))
                listaEstados.append([(nx,ny),(x,y),nx+4*ny,1])
                continue

            print('adicionando %d,%d' % (nx, ny))
            listaEstados.append([(nx,ny),(x,y),(5-nx)**2+(5-ny)**2,1])


print(len(listaEstados))
lst = [i[0] for i in listaEstados]
print(lst) 


final =  [i for i in listaEstados if i[0]==(5,5)]

track = [final[0][0]]

while final[0][0]!= (0,0):    
    for i in listaEstados:
        if i[0]==final[0][1]:
            #print(final[0])
            final[0] = i
            track.append(final[0][0])
            continue

track.reverse()

fig,ax = plt.subplots(1)
plt.axis([0,6,0,6])

for y in range(0,6):
    for x in range(0,6):
        if grid[x][y]==1:
            rect = patches.Rectangle((x,y),1,1,linewidth=1,edgecolor='r',facecolor='none')
            ax.add_patch(rect)

j = 1
for i in track:
    ax.text((i[0])+0.5, (i[1]+0.5), j,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10, color='red')

    j = j + 1

plt.show()

final = [i for i in listaEstados if i[0]==final[0][1]]

    


