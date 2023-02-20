

### Laziness of generators

# calcula a serie de lucas 

#The first few Lucas numbers are
#
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, ... . (sequence A000032 in the OEIS)
#
# As with the Fibonacci numbers, each Lucas number is defined to be the sum of its two immediately previous terms, 
# thereby forming a Fibonacci integer sequence. The first two Lucas numbers are 
# L{0}=2 and L_{1}=1, 
# which differs from the first two Fibonacci numbers. 
# Though closely related in definition, Lucas and Fibonacci numbers exhibit distinct properties.


# Executa até CTRL-C por parte do utilizador.
# 2023. teste-

def lucas_infinite_sequence():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a,b = b, a+b

i=0
for x in lucas_infinite_sequence():
    print(i, '=====> ', x)
    i += 1
    print("\n------------------------\n\n\n")



