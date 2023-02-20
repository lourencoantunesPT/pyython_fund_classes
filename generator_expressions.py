
# é parecido com as comprehensions...mas com sequencias infinitas....


# declaracao da expressao (nao executa ainda a expressao)
million_squares = (x*x for x in range (1,1000001))
print(million_squares)

# para forçar a execucao, criar uma lista com o resultado por ex:

print(list(million_squares)[-10:])
#neste caso, calcula os 10 ultimos 'yields' do generator...

print(list(million_squares))
#a lista continua vazia...MAGIA!!!!


# CALCULO DE SOMATORIO dos QUADROADOS DE 1000000 de numeros - pelo brut force, gastaria 400 MB de RAM....e duraria bastante...

print(sum(x*x for x in range(1,10000001)))

print(sum((x*x for x in range(1,10000001))))
#o parentesis da generator expression é dispnesado, estando dentro de uma invocacao de funcao que tb tem os parentesis.

