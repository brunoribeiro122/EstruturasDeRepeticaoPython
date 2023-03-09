tentativas = 0
while tentativas < 3:
    senha = input('digite a senha:')
    if senha == 'senha123':
        print('Acesso Concedido!')
        break
    else:
        print('senha incorreta. Tente novamente.')
        tentativas += 1
else:
    print('você excedeu o número máximo de tentativas.')