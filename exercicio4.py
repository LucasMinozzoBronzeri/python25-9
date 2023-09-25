codigo = int(input('Digite o código da palestra: '))

match codigo:
    case 1:
        print('Palestra Linux no Auditório 1!')
    case 2:
        print('Palestra Banco de dados no Auditório 2!')
    case 3:
        print('Palestra Windows Defender no Auditório 3!')
    case 4:
        print('Palestra Lógica e Programação no Auditório Principal!')
    case _:
        print('Digite um código válido!')

