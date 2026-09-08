horas=float(input('digite a quantidade planejada de horas semanais: '))

if horas<10:
    print('quantidade muito baixa')

elif horas>40:
    print('quantidade muito alta')

else:
    print(f'plano configutado com {horas} horas.')
