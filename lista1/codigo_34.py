A = float(input("Digite A: "))
B = float(input("Digite B: "))
C = float(input("Digite C: "))

delta=(B**2)-(4*A*C)

if delta>0:

    raiz1=((-B+(delta**0.5))/(2*A))
    raiz2=((-B-(delta**0.5))/(2*A))

    print(f'delta: {delta:.2f}\nraiz 1: {raiz1:.2f}\nraiz 2: {raiz2:.2f}')

elif delta==0:
	raiz=-B/(2*A)
	print(f'raiz unica: {raiz}')
	
else:
	print("não ha raizes")
