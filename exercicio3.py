

numero = int(input('Digite um numero inteiro: '))

numero1 = numero / 3
numero3 = numero // 3
numero4 = numero1 - numero3

if numero4>0:
    numero4 = 1

match numero4:
    case 1:
        print('Numero não é multiplo de 3!')
    case 0:
        print('Numero é multiplo de 3!')
