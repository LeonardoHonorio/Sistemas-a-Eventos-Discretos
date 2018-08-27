import matplotlib.pyplot as plt
import matplotlib.patches as patches
#    0: vazia
#    1: bloqueada
#    2: objetivo
#    3: celula visitada


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

caminhos = []

def search(x,y):
    if grid[x][y]==2:
        print("solucao encontrada em ",x,y)
        return True
    if grid[x][y]==1:
        print("obstaculo em",x,y)
        return False
    if grid[x][y]==3:
        print("caminho ja per",x,y)
        return False

    #passou pelo grid
    print("passando por",x,y)
    grid[x][y]=3

    #definindo direcoes possiveis de busca
    dbusca = [(1,0),(0,-1),(-1,0),(0,1)]

    tg = len(grid)-1

    for i in dbusca:
        dx, dy = i
        nx = x + dx
        ny = y + dy

        #verificando que esta dentro do grid
        if nx>=0 and nx <=tg and ny>=0 and ny<=tg:
            print("pos",x,y,"proc em",nx,ny)
            if search(nx,ny):
                caminhos.append((nx,ny))
                return True



# plt.axis


fig,ax = plt.subplots(1)
plt.axis([0,6,0,6])

for y in range(0,6):
    for x in range(0,6):
        if grid[x][y]==1:
            rect = patches.Rectangle((x,y),1,1,linewidth=1,edgecolor='r',facecolor='none')
            ax.add_patch(rect)





search(0,0)
print(caminhos)

caminhos.append((0,0))
caminhos.reverse()

j = 1
for i in caminhos:
    ax.text((i[0])+0.5, (i[1]+0.5), j,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10, color='red')

    j = j + 1


plt.show()




