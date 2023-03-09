maiornumero = -999999999
number = int(input('Entre com o número ou digite -1 para parar:'))

while number != -1:
    if number > maiornumero:
        maiornumero = number
    number = int(input('Entre com um número e digite =1 para parar:'))
    
    
print('O maior numero é:', maiornumero)