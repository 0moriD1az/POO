n=int(input("Digite N (positivo e inteiro): "))
x=int(input("Digite X (positivo e inteiro): "))

if n<0 or x<0:
    print('\nos numeros devem ser positivos')
    exit()

res=n**x

print(f"\nO valor é de {res}")