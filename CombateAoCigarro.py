#Nome: Gabriel Felipe Montoni dos Santos
#RM : 552271
#Nome: Gabriel Soares Da Cruz
#RM: 97902
#Nome: Giovanni Bruno Silva Ferreira
#RM: 98084
#Nome: Pedro Henrique Santos Lombardi
#RM: 99598

tempoFumante = float(input("Tempo como fumante (em anos).....: "))
valorCig = float(input("Valor do maço....................: "))
qntdCig = float(input("Quantidade de maços por dia......: "))

gastoTotal = (tempoFumante*12*30)*qntdCig*valorCig
if gastoTotal < 20000:
    print(f"Com o valor R${gastoTotal:.2f}, você poderia ter dado entrada em um carro.")
elif gastoTotal>20000 and gastoTotal<50000:
    print(f"Com o valor R${gastoTotal:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R${gastoTotal:.2f}, você poderia ter comprado um carro zero.")