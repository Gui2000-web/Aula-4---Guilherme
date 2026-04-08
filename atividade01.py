#Realizar o programa que assegura que o cliente possa realikzar uma compra de R$250,00, junto com o desconto de 16%, caso o contrário, o valor da compra deverá permanecer o mesmo:

valor = float(input('Informe o valor: '))

if valor > 250:
    desconto = valor * 0.16
    valor_novo = valor - desconto
    print(f'O total a pagar{valor_novo}')
else:
    print(f'Sem desconto. Valor a pagar {valor}')    



