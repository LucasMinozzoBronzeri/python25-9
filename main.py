numero = float(input('Primeiro numero: '))
numero1 = float(input('Segundo numero: '))

print('1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        resultado = numero + numero1
        print(f'A soma é de: {resultado}')
    case 2:
        resultado = numero - numero1
        print(f'O valor da subtração é de: {resultado}')
    case 3:
        resultado = numero * numero1
        print(f'O valor da multiplicação é de: {resultado}')
    case 4:
        resultado = numero/numero1
        print(f'O valor da divisão é de: {resultado}')
    case _:
        print('Opção inválida!')
