import numpy

def checa(listaestados,listasaida,logica):
    #(1,0,1,0,0,0,0)
    lcurrent = []
    for cs in range(0, len(listaestados)):
        clog = listaestados[cs]
        current = 1
        for i in range(0,len(logica)):
            sval = 0
            for j in logica[i]:
                if j[1]==0:
                    sval = sval + clog[j[0]]
                else:
                    sval = sval + (not(clog[j[0]]))
                        
            vatual = min(1,sval)
            print (vatual)
            current = current * vatual
        lcurrent.append(current)

    

    return lcurrent
