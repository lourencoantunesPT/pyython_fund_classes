

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



def run_pipeline():
    items = [3,6,6,2,1,1]
    for item in take(3,distinct(items)):
        print(item)


run_pipeline()
