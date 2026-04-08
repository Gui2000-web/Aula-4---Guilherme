# Estrutura If
idade = int(input('Insira a idade: '))

if idade >= 18:
    print('Você é adulto')
else:
    print('Você não é adulto')
#-----------------------------------------------------
    

pontos = int(input('Informe os pontos: '))
if pontos >= 100:
    print('Excelente!')
elif pontos >=50:
    print('Bom desempenho')
elif pontos >= 25:
    print('Satisfatório')
else:
    print('Pratique mais...')

if pontos <= 25:
    print('Pratique mais...') 
elif pontos <= 50:
    print('Satisfatório')
elif pontos <= 100:
    print('Bom desempenho')
else:
    print('Excelente')

#Operadores AND e OR
usuario = input('Nome: ')
senha = input('Senha: ')

if usuario == "admin" or senha == "1234":
    print('Login realizado com sucesso')
else:
    print('Usuário ou senha incorreto')    