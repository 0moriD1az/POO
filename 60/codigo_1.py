horas=int(input("Digite as horas (caso não haja, digite 0): "))
minutos=int(input("Digite as minutos (caso não haja, digite 0): "))
segundos=int(input("Digite as segundos (caso não haja, digite 0): "))

final=horas * 3600 + minutos * 60 + segundos

print(f"O trabalho tem {final} segundos de duração")