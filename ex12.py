palavra_sem_vogais = ''
usuariopalavra = input('Entre com uma palavra:')
usuariopalavra = usuariopalavra.upper()

for letra in usuariopalavra:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        palavra_sem_vogais += letra
        

    print(palavra_sem_vogais)