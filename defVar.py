#Tarefa
#1.-Escreva um script python que define duas variáveis do tipo inteiro (int) e atribui um valor positivo para elas. Imprima as duas variáveis.
num2=1
num_1=2
print('Number',num_1,'Number',num2)

#2.-Seja x = 2 + 4j, descubra qual é tipo associado a essa variável pelo interpretador.
print('ingrese valor de j')
j=3
# j=input()
x = 2 + 4 * int(j)
print('valor de x es',x)

#3-Experimente a inicialização de variáveis como segue:
#urnas = {}
#sessao = { "escola municipal", 103 }
#descubra qual é o tipo da variável urnas e da variável sessao. Explique se necessário a razão dos tipos serem distintos.
urnas = {}
sessao = { "escola municipal", 103 }
print('Urnas es de tipo',type(urnas)) 
print('Sessao es de tipo',type(sessao)) 


#4.- Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos
# ola = "mundo"  ======> valido  
# _ola = "mundo" ======>  não valido (Não deve iniciar com _ )
# _1_ola = "mundo" ======> não valido (Não deve iniciar com _ )
# 1_ola = "mundo" ======> não valido (Não deve iniciar com números )
# ola_1 = "mundo"  ======> valido
# meu mundo = "ola"  ======> valido
#aponte as razões para os nomes inválidos, indicando o item e a razão da violação das regras de nomeação de variável.


#5 .- No seguinte comando de atribuição
casa, senha = "minha", "ola" # Funciona, coloca valor na segundo a ordem das variaveis
#casa, senha = "minha" # Não funciona, tem muitos valores para empaquetar em uma variavel so
casa = "minha"  # Funciona, coloca valor "minha" na variavel casa
# Quais foram as atribuições que funcionaram e quais não funcionaram? Explique a razão dos problemas.

#6-  Considere as seguintes operações matemáticas, e indique o resultado de cada uma:

print('1.- ',(10 - 6)**2)
# resultado : 16

print('2.- ',10 - 6**2)
# resultado .-  -26

print('3.- ',10 - 3 // 2)
# resultado .-  9

print('4.- ',10 - 3 / 2)
# resultado .-  8.5

#7- Qual a importância de se criar ambiente virtuais para o desenvolvimentos de projetos usando Python?
# A importancia de criar ambientes virtuais para desenvolvimentos de projetos é que permite  isolar 
# um projeto assim como suas dependências e bibliotecas em um único lugar. o que permite poder excluir 
# o modificar o projeto sem afetar outros.

#8- Descubra e responda qual versão do python está instalado no seu ambiente de desenvolvimento. Que comando você usou para obter essa informação?
# python --version

#9- Uma tupla é um tipo imutável, portanto qualquer variável desse tipo pode ser alterada desde que os seus elementos sejam individualizados, como no código abaixo:
comprado = ("carro", "GM", "20K")
# comprado[1] = "Ford"
# você concorda com essa afirmação? justifique sua resposta.
# Não, porque uma tupla não suporta asinação de item individualizados


#10 - Considere o código abaixo:
numero = input()
print(numero*3)
# se o valor 3(três) for informado como entrada e armazenado na variável número.
# Não, é armazenada como string

# Revise o código disponibilizado em src/primeiro.py.
# Em seguida altere o programa para que ele se torne generalista, i.e.,
# aceite qualquer quantidade de notas que cada aluno pode ter.


# Tarefa 2

# 1-Elabore um programa que realize a leitura de uma data e um número de telefone, e armazene os valores lidos em um dicionário que tem a seguinte estrutura:{
# {
#    "data":"dd/mm/aaaa",
#    "telefone":"(92)999879876"
# }
# dictionary = {}
# for i in range(0, 3):
#     print('digite data')
# data = input()
# telefone = input()