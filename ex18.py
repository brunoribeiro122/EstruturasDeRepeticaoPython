#imprimir apenas os números pares de 1 a 10 
# que sao maiores que 4 ou menores que 8

for i in range(1, 11):
    if i % 2 == 0 and (i > 4 or i < 8):
        print(i)
        #imprimir apenas números impares de 1 a 10
        #que são menores que 3 ou maiores que 7
        
for i in range(1,11):
    if i % 2 != 0 and (i < 3 or i >7):
        print (i)