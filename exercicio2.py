numero = float(input('Digite um numero: '))

print('1 - Calcular o dobro')
print('2 - Calcular a metade')
print('3 - Calcular o 10% do numero')

opcao = int(input('Escolha o tipo de calculo: '))

match opcao:
    case 1:
        resultado = numero * 2
        print(f'O valor do dobro é de: ')
    case 2:
        resultado = numero / 2
        print(f'O valor da metade é de: ')
    case 3:
        resultado = numero/10
        print(f'O valor dos 10% é de: ')
    case _:
        print('Opção invalida!')
