"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e 
o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""


def sequencia_fibo(n):
    sequencia = [0,1]
    while sequencia[-1] < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def faz_parte(n, sequencia):
    return n in sequencia



numero = int(input("Digite um Numero para saber se faz parte da sequência de Fibonacci:\n"))


sequencia = sequencia_fibo(numero)
if faz_parte(numero, sequencia):
    print(f'O número {numero} faz parte da sequência de Fibonacci.')
else:
    print(f'O número {numero} não faz parte da sequência de Fibonacci.')