X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))

if X>0 and Y>0:
    print("primeiro quadrante")

elif X<0 and Y>0:
    print("segundo quadrante.")

elif X<0 and Y<0:
    print("terceiro quadrante")

elif X>0 and Y<0:
    print('quarto quadrante')
else:
    print("um ou ambos os valores estão no eixo ou na origem")
