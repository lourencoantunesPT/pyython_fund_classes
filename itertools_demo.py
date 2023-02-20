
def take(contagem,iteravel):
    contador = 0
    for item in iteravel:
        if contador == contagem:
            return
        contador +=1
        yield item



def distinct(iteravel):
    visto = set()
    for item in iteravel:
        if item in visto:
            continue
        yield item
        visto.add(item)


#escolhe n elementos de uma lista iteravel
l = [12,13,14,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]*1000
print(l)

#cria lista com a escolha dos primeiros 4 elementos de l
nova = list(take(4,l))
print(nova)

#islice() - carrega os primeiros n de um iterador
from itertools import islice
print(list(islice(take(15,l), 5)))
print(list(islice(take(15,l), 10)))
print(list(islice(take(15,l), 12)))

#contar

# neste exemplo, pego numa lista de 20.000 elementos, e obtenho os 10 ultimos das contagens multiplas de 7
from itertools import count, islice

lista2 = islice( (x for x in count() if x%7 == 0), 100)
print (lista2)
print(list(lista2)[-10:])

#any() and all()
#zip()
# permite fazer calculos par a par entre 2 iterables






