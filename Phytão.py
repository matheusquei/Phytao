# O Básico sobre Phytão

# 1 ---------------- Variáveis ------------- #


# Podemos pensar em variáveis como palavras que guardam um valor. Simples assim.
# Em Python, é facinho definir uma variável e atribuir um valor à ela. Vamos imaginar que queremos armazenar um valor (1) em uma variável chamada one:

one = 1

# Prontinho! Simples, não? A gente atribuiu o valor 1 à variável one.
# E conseguimos ter inúmeras variáveis.

two = 2
some_number = 10000

# Como vimos no código acima, temos a variável two e atribuímos o valor 2 (um número inteiro). E nossa outra variável some_number com o valor 10000 armazenado.
# Além disso, conseguimos atribuir vários tipos de valores em nossas variáveis, além de números inteiros. Conseguimos lidar com valores booleanos (True / False), strings, números reais e outros tipos de dados.

# booleans
true_boolean = True
false_boolean = False

# string
my_name = "Leandro Tk"

# float
book_price = 15.80

# Os valores booleanos são True e False. Temos a variável true_boolean e false_boolean que vão representar esses valores. A variável my_name guarda o valor do tipo string, que no caso, o valor é Leandro Tk. E, por último, um número com ponto flutuante armazenado na variável book_price.






# 2 -----------------------Controle de fluxo: condicionais---------------- #

# A expressão if avalia se a declaração é True ou False. Se a declaração for True, o código dentro do if é executado. Vamos ver um exemplo:

if True:
  print("Hello Python If")

if 2 > 1:
 print("2 is greater than 1")


# No primeiro código, temos a declaração com o valor True. Ou seja, nosso print("Hello Python If") é executado.
# Já no segundo, temos a declaração com a "pergunta" 2 é maior que 1?. A resposta óbvia é que sim, ou seja, é avaliada para True. Logo nosso código dentro do if é executado.

# Temos o else também. E esse código é apenas executado, caso a expressão seja False.

if 1 > 2:
  print("1 is greater than 2")
else:
  print("1 is not greater than 2")

# Nesse caso, 1 é menor que 2, então o código dentro do if não é executado. E o código do else é executado.

# Temos também o elif, que basicamente significa else if, ou seja, espera uma expressão, como nesse próximo exemplo:

if 1 > 2:
  print("1 is greater than 2")
elif 2 > 1:
  print("1 is not greater than 2")
else:
  print("1 is equal to 2")

# * if pergunta se 1 é maior que 2?: False, então não executa o código e passa para o elif.
# * elif pergunta se 2 é maior que 1?: True, logo o código print("1 is not greater than 2") é executado.

# Caso o elif também tivesse um valor False, o código executado seria o else.






# 3 -----------------------Looping / Iterador---------------- #

# Em Python, temos várias formas de iterar, ou seja, fazer uma repetição do código. Vamos conversar aqui sobre 2 deles: while e for.
# Iterando com while: Enquanto a declaração tiver o valor True, o código dentro do bloco vai continuar a ser executado.

# Nesse exemplo debaixo, nosso código vai fazer o print dos números de 1 a 10.

num = 1

while num <= 10:
    print(num)
    num += 1

# O while precisa de um loop condition, ou seja, uma condição, uma declaração que significa continuar ou parar a iteração. Se o loop condition for True, continua o loop. Se for False, o loop para de executar o código dentro do bloco do while.
# Nesse exemplo, o num é inicializado com 1 e o primeiro loop condition é 1 <= 10 e o resultado é True, ou seja, continuamos a executar o bloco. Para cada iteração o num é incrementado.

# Quando o num chega à 11, o loop condition se torna False e chega a hora de deixar o bloco de código.


# Outro código para entendermos melhor o while:

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False

# O loop_condition é inicializado com True, logo continua a iterar, até que atualizamos a variável loop_condition para ser False e saírmos do loop.

# Iterando com for: definimos uma variável que representará o valor de cada iteração. Vamos ver esse exemplo:

for i in range(1, 11):
print(i)





# 4 -----------------------Listas (ou coleções, ou vetores, ou arrays)---------------- #

# Imaginemos que vamos armazenar o número inteiro 1 em alguma variável. Mas talvez queiramos armazenar o inteiro 2 também. E o 3, 4, 5…
# Será que temos alguma outra maneira de armazenar valores inteiros sem precisar de 1 milhão de variáveis? Yeap! Vamos falar sobre listas.

my_integers = [1, 2, 3, 4, 5]

# Bem simples, não?! Aqui criamos uma lista com nome my_integers com o valores inteiros de 1 a 5.
# Mas você pode estar perguntando: "como podemos pegar um valor dessa lista?"
# Boa pergunta! A lista tem o conceito de índice (ou index). O primeiro valor da lista tem o índice 0. O segundo tem o 1. E assim por diante.

# Aqui temos uma lista com os valores 5, 7, 1, 3 e 4. O valor 5 tem o índice 0 e assim por diante.
# Vamos usar Python para entender melhor essa ideia na prática:

my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4

# Armazenamos os valores na lista my_integers. E usamos o código my_integer[0] para acessar o valor que está no índice 0, ou seja, o valor 5. Testamos para o índice 1 e 4 também.
# Agora vamos imaginar que não queremos apenas armazenar números inteiros. Vamos guardar uma lista com os nomes das pessoas da minha família:

relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print(relatives_names[4]) # Kaio

# Criamos a lista relatives_names e guardamos todos os nomes. Depois acessamos o nome que está no índice 4, nesse caso, o Kaio. Legal, funcional igualmente aos números inteiros.
# Bom, acabamos de aprender como os índices de uma lista funcionam. Mas ainda preciso mostrar como adicionar mais valores para uma lista.
# O método mais comum para adicionar um novo elemento na lista se chama append. Vamos ver como funciona:

bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week

# append é super simples. Só precisamos passar o novo valor como parâmetro do método.
# Nesse exemplo, definimos a lista bookshelf. Uma lista vazia, nenhum valor pré-adicionado. Depois usamos o método append 2 vezes. Um para adicionar o livro The Effective Engineer e depois para adicionar outro livro The 4 Hour Work Week. Se acessarmos o valor no índice 0, vamos obter o livro The Effective Engineer, por exemplo.

# Bom, por hora é o suficiente sobre listas. Agora vamos falar sobre outra estrutura de dados.





# 4 -----------------------Dicionário: Estrutura de Dados de chave-valor---------------- #

# Agora sabemos que as listas usam números inteiros como índices. Mas e se não quisermos usar números inteiros nos nossos índices? Alguma estrutura de dados que possamos usar índices como número, string ou outro tipo de valor.
# Vamos aprender sobre Dicionários. Um dicionário é uma estrutura de dados, uma coleção de pares chave-valor. Vamos ver como funciona na prática:

dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

# A chave é o "índice" que aponta para um valor. Nesse exemplo, a chave "key1" aponta para o valor "value1".
# Como acessamos o valor no dicionário? Usando a chave.

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian

# Aqui criamos um dicionário dictionary_tk. Com informações sobre mim: meu nome, apelido e nacionalidade. Cada atributo é uma chave no dicionário.
# Assim como aprendemos como acessar um valor da lista usando índices, também podemos usar índice (no caso dos dicionários — chaves) para acessar um valor do dicionário.


# Outro conceito legal de dicionários, é que podemos usar qualquer outro tipo de dados como valor. Nesse próximo exemplo vamos usar um inteiro como valor:

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])) # And by the way I'm Brazilian

# Complementando aquele primeiro exemplo, agora adicionamos a chave "age" e colocamos 24 como valor.

# E assim como adicionamos novos valores na lista, podemos fazer isso também em dicionários. Lembra que uma chave sempre aponta para um valor? Esse conceito é uma parte essencial do dicionário. E isso também é verdade quando falamos sobre adicionar novos valores para essa estrutura de dados.

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

dictionary_tk['age'] = 24

print(dictionary_tk) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}

# Nesse exemplo temos o dicionário dictionary_tk com os valores name, nickname e nationality. Mas agora queremos adicionar um novo par age com o valor 24. Simplesmente atribuímos o valor 24 para a chave age no dicionário dictionary_tk. Nada muito complicado aqui.