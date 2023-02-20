
import sys

def sqrt(x):
    """ calcula raiz quadrada
    """
    guess = x
    i = 0
    while (guess * guess != x) and (i < 20):
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print("sqrt(9) >>> ", sqrt(9))
        print("sqrt(2) >>> " , sqrt(2))
        # excepcao divisao por zero
        print("sqrt(-1) >>> " , sqrt(-1))
        print("esta linha nunca vai ser escrita se der erro ao chamar a funcao sqrt()....")
    except ZeroDivisionError:
        print("nao se pode calcular raiz quadrada de um numero negativo.")
    #except ValueError as e:
    #    print("o programa deu erro grave" + e, file=sys.stderr)
    print("continuando....")

if __name__ == '__main__':
    main()
