import numpy
from checalogica import checa

#logica = [[1,3],[2]]
estados = ( (1,	0,	1,	0,	0,	0,	0),\
            (1,	0,	0,	0,	0,	0,	1),\
            (1,	0,	0,	1,	0,	0,	1),\
            (0,	0,	0,	1,	1,	0,	1),\
            (0,	1,	0,	1,	1,	0,	1),\
            (0,	0,	0,	1,	1,	0,	0),\
            (1,	0,	0,	1,	0,	0,	0),\
            (1,	0,	0,	0,	0,	1,	0),\
            (1,	0,	1,	0,	0,	1,	0))

saida = (0, 0, 1, 1, 1, 0, 0, 0, 0)

#logica = [[[3,0]],[[6,0]]]

logica = [[[0,0]]]

resultado = checa(estados,saida,logica)

print(resultado)

a = 1



