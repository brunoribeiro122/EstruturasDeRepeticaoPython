numero_secreto = 42
tentativas = 1
while tentativas <= 3:
    palpite = int(input('Adivinhe o número secreto'))
    if palpite == numero_secreto:
        print('Parabens, você acertou!')
        break
    else:
        if palpite > numero_secreto:
            print('O número secreto é menor que', palpite)
        
        else:
            print('O número secreto é maior do que ', palpite)
    tentativas += 1
if tentativas > 3:
    print('Suas tentativas acabaram. O número secreto era',numero_secreto )