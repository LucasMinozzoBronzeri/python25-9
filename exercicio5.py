from unittest import case

print('1 - Picanha 25,00')
print('2 - Lasanha 20,00')
print('3 - Strogonoff 20,00')
print('4 - Bife Acebolado 15,00')
print('5 - Pão com ovo 5,00')

picanha = 25
lasanha = 20
strogonoff = 20
bifeacebolado = 15
paocomovo = 5

opcao = int(input('Escolha o seu prato: '))

match opcao:
    case 1:
        opcao = 25
    case 2:
       opcao = 20
    case 3:
        opcao = 20
    case 4:
        opcao = 15
    case 5:
        opcao = 5
    case _:
        print('Digite uma opção valida!')


print('1 - Sim, eu pagarei a gorjeta!')
print('2 - Não, não quero pagar a gorjeta!')

gorjeta = int(input('Aceita pagar a gorjeta? :'))

match gorjeta:
    case 1:
        divisao = opcao / 10
        resultado = opcao + divisao
        print(f'O valor é de: {resultado}')
    case 2:
        print(f'O valor é de {opcao}')

